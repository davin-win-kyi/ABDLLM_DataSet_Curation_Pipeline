# element_dataset_pipeline.py
from pathlib import Path
from typing import Dict, Any
import json

from initialize_element_dataset import (
    build_initial_dataset,
    _open_local_in_chrome,   # reuse Selenium helper
    _collect_elements,       # reuse element collector
)
from element_neighbors import add_neighbors
from element_feedback_loop import feedback_loop
from UID_Generator import UIDGenerator


def _load_element_dataset(out_json: Path) -> Dict[str, Dict[str, Any]]:
    """
    Load element_dataset.json and return a mapping:
        ID -> element record
    """
    data = json.loads(out_json.read_text(encoding="utf-8"))
    elements = data.get("Elements", [])
    by_id: Dict[str, Dict[str, Any]] = {}
    for elem in elements:
        uid = elem.get("ID")
        if uid:
            by_id[uid] = elem
    return by_id


def inspect_elements_with_metadata(html: Path, out_json: Path) -> None:
    """
    After the dataset has been fully constructed (neighbors + feedback),
    open the page with Selenium, loop all meaningful elements,
    recompute UID, and fetch metadata from element_dataset.json.
    Prints and exposes variables for each element.
    """
    # Load dataset into memory, keyed by ID
    dataset_by_id = _load_element_dataset(out_json)

    # Open the HTML via the same helper used in initialize_element_dataset
    driver = _open_local_in_chrome(html, headless=True)
    try:
        elems = _collect_elements(driver)
        print(f"Total meaningful elements: {len(elems)}")

        for el in elems:
            uid = UIDGenerator.id_for_element(driver, el)
            meta = dataset_by_id.get(uid)

            if not meta:
                # If we didn't record this element earlier, just skip
                print(f"[WARN] No dataset entry found for UID {uid}")
                continue

            # --- These are the variables you asked for ---
            element_id = uid
            element_descriptor = meta.get("Element_descriptor")
            element_type = meta.get("Element_type")
            neighboring_elements = meta.get("Neighbor_elements", [])

            # Example: print them out
            print(f"ID: {element_id}")
            print(f"  Element_type: {element_type}")
            print(f"  Element_descriptor: {element_descriptor}")
            print("  Neighbor_elements:")
            for n in neighboring_elements:
                print(f"    - {n}")
            print("-" * 60)

            # At this point you can do anything with:
            # element_id, element_descriptor, element_type, neighboring_elements
            # e.g., feed them into RAG, prompt the user, etc.

    finally:
        driver.quit()


def main():
    html = Path("reviewable_page.html")
    out = Path("element_dataset.json")

    """
    Steps to take
    - do nessecary RAG calls (init_profile and element_dataset.json)
    - go over each of the elements and along with information,
      guide the queries to the user
    - update the UI through the feedback and show the UI when 
      it is being changed
    - save this information in the elements_dataset.json
    """

    # 1) Initialize dataset (IDs, types, base descriptors via Selenium)
    build_initial_dataset(html, out)

    # 2) Find neighbors spatially and add their DESCRIPTORS
    add_neighbors(html, out, k=5)

    # 3) Collect interactive feedback in terminal and persist
    # feedback_loop(html, out)

    # 4) Re-open the page, iterate all elements, and pull metadata
    inspect_elements_with_metadata(html, out)


if __name__ == "__main__":
    main()
