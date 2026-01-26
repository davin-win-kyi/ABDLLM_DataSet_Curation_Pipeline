# UID_Generator.py
import hashlib, re
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

# Normalize outerHTML: collapse whitespace and strip data-* attributes so
# dynamic tracking junk doesn't break determinism.
_HTML_DATA_ATTRS = re.compile(r'\sdata-[\w\-]+="[^"]*"')
_WS = re.compile(r"\s+")

def _normalize_html(raw_html: str) -> str:
    html = _WS.sub(" ", raw_html or "").strip()
    html = _HTML_DATA_ATTRS.sub("", html)
    return html

# JS to compute a robust :nth-of-type DOM path (ignores IDs/classes to avoid flakiness).
_JS_DOM_PATH = """
return (function(el){
  if(!el) return "";
  const parts = [];
  let cur = el;
  while (cur && cur.nodeType === 1 && cur.tagName) {
    let tag = cur.tagName.toLowerCase();
    let idx = 1;
    let sib = cur.previousElementSibling;
    while (sib) {
      if (sib.tagName === cur.tagName) idx++;
      sib = sib.previousElementSibling;
    }
    parts.push(tag + ":nth-of-type(" + idx + ")");
    cur = cur.parentElement;
  }
  return parts.reverse().join(">");
})(arguments[0]);
"""

class UIDGenerator:
    """
    Deterministic, Selenium-first stable ID generator.
    ID = sha1( dom_path || normalized_outerHTML )[:16]
    """
    @staticmethod
    def id_for_element(driver: WebDriver, element: WebElement) -> str:
        dom_path: str = driver.execute_script(_JS_DOM_PATH, element) or ""
        outer: str = element.get_attribute("outerHTML") or ""
        normalized = _normalize_html(outer)
        return hashlib.sha1(f"{dom_path}||{normalized}".encode("utf-8")).hexdigest()[:16]

    @staticmethod
    def element_type(element: WebElement) -> str:
        try:
            return (element.tag_name or "").lower()
        except Exception:
            return ""

    @staticmethod
    def short_text(element: WebElement, max_len: int = 80) -> str:
        try:
            txt = element.text or ""
            txt = _WS.sub(" ", txt).strip()
            return (txt[: max_len - 1] + "…") if len(txt) > max_len else txt
        except Exception:
            return ""

    @staticmethod
    def heuristic_descriptor(element: WebElement) -> str:
        """
        Lightweight fallback 'descriptor' (you can swap in your GPT call elsewhere).
        """
        tag = UIDGenerator.element_type(element)
        cls = (element.get_attribute("class") or "").strip()
        aria = (element.get_attribute("aria-label") or "").strip()
        name = (element.get_attribute("name") or "").strip()
        placeholder = (element.get_attribute("placeholder") or "").strip()
        alt = (element.get_attribute("alt") or "").strip()
        txt = UIDGenerator.short_text(element)

        bits = [f"<{tag}>"]
        if cls: bits.append(f'class="{cls}"')
        if aria: bits.append(f'aria-label="{aria}""')
        if name: bits.append(f'name="{name}"')
        if placeholder: bits.append(f'placeholder="{placeholder}"')
        if alt: bits.append(f'alt="{alt}"')
        if txt: bits.append(f'text="{txt}"')

        return " ".join(bits) if bits else f"<{tag}>"

