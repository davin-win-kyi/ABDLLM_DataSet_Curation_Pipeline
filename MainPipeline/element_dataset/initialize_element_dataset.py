# initialize_element_dataset.py
import os, json, time
from pathlib import Path
from typing import Dict, Any, List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

from openai import OpenAI  # pip install openai>=1.0.0

from UID_Generator import UIDGenerator

MEANINGFUL = {
    "a","button","input","select","textarea","label","img","svg","video","audio",
    "nav","header","footer","main","aside","section","article","form","fieldset","legend",
    "h1","h2","h3","h4","h5","h6","li","ul","ol","table","thead","tbody","tfoot","tr","td","th",
    "div","span"
}

def _open_local_in_chrome(local_html: Path, headless: bool = True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    driver.get(local_html.resolve().as_uri())  # file:// URL
    return driver

def _collect_elements(driver) -> List[WebElement]:
    elems = driver.find_elements(By.XPATH, "//*")
    return [e for e in elems if (e.tag_name or "").lower() in MEANINGFUL]

# ---------- GPT describer (function-only, with safe fallback) ----------

def _safe_client() -> Optional[OpenAI]:
    try:
        if not os.getenv("OPENAI_API_KEY"):
            return None
        return OpenAI()
    except Exception:
        return None

def _build_snapshot(el: WebElement) -> Dict[str, Any]:
    try:
        tag = (el.tag_name or "").lower()
    except Exception:
        tag = ""

    def ga(name: str) -> Optional[str]:
        try:
            return el.get_attribute(name)
        except Exception:
            return None

    attrs = {}
    for name in ["id","class","name","type","href","value","placeholder","title","aria-label","role","alt"]:
        v = ga(name)
        if v:
            attrs[name] = v

    try:
        text = (el.text or "").strip()
    except Exception:
        text = ""

    try:
        size = el.size or {}
        loc = el.location or {}
        bbox = {"x": int(loc.get("x", 0)), "y": int(loc.get("y", 0)),
                "w": int(size.get("width", 0)), "h": int(size.get("height", 0))}
    except Exception:
        bbox = {"x": 0, "y": 0, "w": 0, "h": 0}

    try:
        outer = ga("outerHTML") or ""
        outer_short = outer if len(outer) <= 1200 else ""
    except Exception:
        outer_short = ""

    snap = {"tag": tag, "text": text, "attrs": attrs, "bbox": bbox}
    if outer_short:
        snap["outerHTML"] = outer_short
    return snap

def gpt_describer(el: WebElement) -> str:
    snapshot = _build_snapshot(el)
    client = _safe_client()
    if not client:
        return UIDGenerator.heuristic_descriptor(el)

    system_msg = (
        "You are an accessibility-savvy UI describer. "
        "Given an element snapshot, write ONE concise, human-friendly descriptor (<= 20 words). "
        "Prefer user-facing semantics over technical markup. "
        "If link or button, summarize purpose using visible text/aria/alt. "
        "If image, prefer alt text; if missing, summarize visible content. "
        "Avoid raw IDs/classes or code. No quotes. No trailing punctuation."
    )
    user_msg = "Element snapshot (JSON):\n" + json.dumps(snapshot, ensure_ascii=False)

    try:
        resp = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
        )
        desc = (resp.choices[0].message.content or "").strip()
        if not desc:
            raise ValueError("Empty description")
        words = desc.split()
        if len(words) > 20:
            desc = " ".join(words[:20])
        return desc
    except Exception:
        return UIDGenerator.heuristic_descriptor(el)
    finally:
        time.sleep(0.03)

# ---------- Computed styles (color/size/saturation/etc.) ----------

# this is to get the color and the saturation of the element (hsl_)
_JS_STYLE_SNAPSHOT = """
return (function(el){
  const cs = window.getComputedStyle(el);
  const rect = el.getBoundingClientRect();

  function parseRGB(s){
    if(!s) return null;
    const m = s.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d\\.]+))?\\)/i);
    if(!m) return null;
    return {r:+m[1], g:+m[2], b:+m[3]};
  }
  function rgbToHsl(r,g,b){
    r/=255; g/=255; b/=255;
    const max=Math.max(r,g,b), min=Math.min(r,g,b);
    let h,s,l=(max+min)/2;
    if (max===min){ h=0; s=0; }
    else {
      const d=max-min;
      s = l>0.5 ? d/(2-max-min) : d/(max+min);
      switch(max){
        case r: h=(g-b)/d + (g<b?6:0); break;
        case g: h=(b-r)/d + 2; break;
        case b: h=(r-g)/d + 4; break;
      }
      h/=6;
    }
    return {h:Math.round(h*360), s:Math.round(s*100), l:Math.round(l*100)};
  }

  const fg = parseRGB(cs.color);
  const bg = parseRGB(cs.backgroundColor);
  const hsl_fg = fg ? rgbToHsl(fg.r, fg.g, fg.b) : null;
  const hsl_bg = bg ? rgbToHsl(bg.r, bg.g, bg.b) : null;

  return {
    width: Math.round(rect.width),
    height: Math.round(rect.height),
    color: cs.color,
    backgroundColor: cs.backgroundColor,
    fontSize: cs.fontSize,
    fontWeight: cs.fontWeight,
    hslFG: hsl_fg,
    hslBG: hsl_bg,
    display: cs.display,
    visibility: cs.visibility,
    opacity: cs.opacity
  };
})(arguments[0]);
"""

def _style_summary(driver, el: WebElement) -> str:
    """
    Returns a concise, readable string summarizing key style facts:
    size, colors, font, and saturation (FG/BG).
    """
    try:
        s = driver.execute_script(_JS_STYLE_SNAPSHOT, el) or {}
    except Exception:
        return ""

    def add_if(val, fmt):
        return [fmt.format(val)] if val else []

    parts: List[str] = []
    # size
    w, h = s.get("width"), s.get("height")
    if isinstance(w, int) and isinstance(h, int):
        parts += add_if(True, f"size={w}x{h}px")
    # colors
    parts += add_if(s.get("color"), "color={}")
    if s.get("backgroundColor") and s["backgroundColor"] != "rgba(0, 0, 0, 0)":
        parts += add_if(s.get("backgroundColor"), "bg={}")
    # font
    parts += add_if(s.get("fontSize"), "font-size={}")
    parts += add_if(s.get("fontWeight"), "font-weight={}")
    # saturation
    hsl_fg, hsl_bg = s.get("hslFG"), s.get("hslBG")
    if hsl_fg and isinstance(hsl_fg.get("s"), (int, float)):
        parts.append(f"saturation_fg={int(hsl_fg['s'])}%")
    if hsl_bg and isinstance(hsl_bg.get("s"), (int, float)):
        parts.append(f"saturation_bg={int(hsl_bg['s'])}%")
    # visibility/opacity if relevant
    if s.get("visibility") and s["visibility"] != "visible":
        parts.append(f"visibility={s['visibility']}")
    if s.get("opacity") and s["opacity"] != "1":
        parts.append(f"opacity={s['opacity']}")

    return ", ".join(parts)

# ---------- main dataset build ----------

def build_initial_dataset(reviewable_html: Path, out_json: Path) -> None:
    driver = _open_local_in_chrome(reviewable_html, headless=True)
    try:
        print("num elements: ", _collect_elements(driver).__len__())
        seen: Dict[str, Dict[str, Any]] = {}
        for el in _collect_elements(driver):
            uid = UIDGenerator.id_for_element(driver, el)
            if uid in seen:
                continue

            elem_type = UIDGenerator.element_type(el)

            # 1) High-level descriptor via GPT (fallback handled inside)
            base_desc = gpt_describer(el)

            # 2) Style facts via computed styles (JS)
            style_facts = _style_summary(driver, el)
            descriptor = f"{base_desc}; {style_facts}" if style_facts else base_desc

            seen[uid] = {
                "ID": uid,
                "Element_descriptor": descriptor,
                "Element_type": elem_type,
                "Neighbor_elements": [],
                "Element feedback": []
            }

        payload = {"Elements": list(seen.values())}
        out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote {out_json}")
    finally:
        driver.quit()

if __name__ == "__main__":
    reviewable = Path("reviewable_page.html")
    out_json = Path("element_dataset.json")
    build_initial_dataset(reviewable, out_json)
