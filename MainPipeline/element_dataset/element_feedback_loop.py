# element_feedback_loop.py
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

from UID_Generator import UIDGenerator

# ---------- Selenium helpers ----------

def _open_local_in_chrome(local_html: Path, headless: bool = True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    driver.get(local_html.resolve().as_uri())  # file:// URL
    return driver

MEANINGFUL = {
    "a","button","input","select","textarea","label","img","svg","video","audio",
    "nav","header","footer","main","aside","section","article","form","fieldset","legend",
    "h1","h2","h3","h4","h5","h6","li","ul","ol","table","thead","tbody","tfoot","tr","td","th",
    "div","span"
}

def _collect_elements(driver) -> List[WebElement]:
    elems = driver.find_elements(By.XPATH, "//*")
    # same filter as initializer
    elems = [e for e in elems if (e.tag_name or "").lower() in MEANINGFUL]
    # OPTIONAL: only visible, to avoid 0x0 or hidden nodes
    # elems = [e for e in elems if e.is_displayed()]
    return elems

# ---------- Feedback loop using stable IDs ----------

def feedback_loop(reviewable_html: Path, dataset_json: Path, headless: bool = True) -> None:
    # Load existing dataset (or start new)
    if dataset_json.exists():
        data = json.loads(dataset_json.read_text(encoding="utf-8"))
    else:
        data = {"Elements": []}

    # Index current JSON by ID for quick updates
    idx: Dict[str, Dict[str, Any]] = {e["ID"]: e for e in data.get("Elements", [])}

    driver = _open_local_in_chrome(reviewable_html, headless=headless)
    try:
        elems = _collect_elements(driver)

        print("\nFeedback loop")
        print("For each element below, type feedback and press Enter.")
        print("Press Enter on an empty line or type 'no' to skip.\n")

        for i, el in enumerate(elems, 1):
            # Compute stable UID from Selenium WebElement
            uid = UIDGenerator.id_for_element(driver, el)

            # Ensure the element exists in the JSON with required fields only
            if uid not in idx:
                elem_type = UIDGenerator.element_type(el)
                descriptor = UIDGenerator.heuristic_descriptor(el)  # lightweight label (non-GPT)
                idx[uid] = {
                    "ID": uid,
                    "Element_descriptor": descriptor,
                    "Element_type": elem_type,
                    "Neighbor_elements": [],
                    "Element feedback": []
                }
                data["Elements"].append(idx[uid])

            # Show descriptor to user and collect feedback
            desc = idx[uid].get("Element_descriptor", "")
            print(f"[{i}/{len(elems)}] {desc}")
            while True:
                fb = input(" - Feedback (or 'no' / empty to continue): ").strip()
                if fb.lower() in {"no", "n", ""}:
                    break
                idx[uid]["Element feedback"].append(fb)
            print()

        # Persist updates
        dataset_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Saved feedback updates to {dataset_json}")

    finally:
        driver.quit()

if __name__ == "__main__":
    reviewable = Path("reviewable_page.html")
    dataset = Path("element_dataset.json")
    feedback_loop(reviewable, dataset, headless=True)
