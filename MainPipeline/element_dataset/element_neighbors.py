# element_neighbors.py
import json, math
from pathlib import Path
from typing import Dict, Any, List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

from UID_Generator import UIDGenerator

def _open_local_in_chrome(local_html: Path, headless: bool = True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    driver.get(local_html.resolve().as_uri())
    return driver

def _collect_elements(driver) -> List[WebElement]:
    return driver.find_elements(By.XPATH, "//*")

_JS_RECT = "return arguments[0].getBoundingClientRect();"

def _center(rect) -> Tuple[float, float]:
    return (rect["x"] + rect["width"]/2.0, rect["y"] + rect["height"]/2.0)

def _distance(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def add_neighbors(reviewable_html: Path, dataset_json: Path, k: int = 5) -> None:
    data = json.loads(dataset_json.read_text(encoding="utf-8"))
    idx: Dict[str, Dict[str, Any]] = {e["ID"]: e for e in data.get("Elements", [])}

    driver = _open_local_in_chrome(reviewable_html, headless=True)
    try:
        elems = _collect_elements(driver)

        # Precompute (uid, descriptor, center) for elements present in dataset
        records: List[Tuple[str, str, Tuple[float,float]]] = []
        for el in elems:
            uid = UIDGenerator.id_for_element(driver, el)
            if uid not in idx:
                continue
            rect = driver.execute_script(_JS_RECT, el)
            ctr = _center(rect)
            desc = idx[uid].get("Element_descriptor", "")
            records.append((uid, desc, ctr))

        # Build neighbor lists by distance
        for i, (uid, _, ctr) in enumerate(records):
            dists: List[Tuple[float, int]] = []
            for j, (uid2, _, ctr2) in enumerate(records):
                if i == j:
                    continue
                dists.append(( _distance(ctr, ctr2), j ))
            dists.sort(key=lambda t: t[0])
            top = [records[j][1] for _, j in dists[:k]]  # neighbor DESCRIPTORS
            idx[uid]["Neighbor_elements"] = top

        dataset_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Updated neighbors in {dataset_json}")
    finally:
        driver.quit()

if __name__ == "__main__":
    add_neighbors(Path("reviewable_page.html"), Path("element_dataset.json"), k=5)
