#!/usr/bin/env python3
"""
04_selenium_inject_and_label_json.py

- Opens each Url with Selenium
- Injects provided JS (Injection_js)
- Lets the user approve (y/n) whether to include it in final dataset
- Stores accepted examples as ONE JSON file:
  {
    "final_dataset": [
      { "Url": ..., "Rule_id": ..., "Injected_html": ..., "Injection_js": ... }
    ]
  }
"""

from __future__ import annotations
import argparse
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


def build_driver(headless: bool) -> webdriver.Chrome:
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,900")
    opts.add_argument("--lang=en-US")
    return webdriver.Chrome(options=opts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--injection_json", type=str, required=True)
    ap.add_argument("--out_json", type=str, required=True)
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--page_load_timeout_s", type=int, default=30)
    ap.add_argument("--post_inject_wait_s", type=float, default=1.0)
    ap.add_argument("--screenshot_dir", type=str, default=None)
    args = ap.parse_args()

    inj_path = Path(args.injection_json).expanduser().resolve()
    out_json = Path(args.out_json).expanduser().resolve()
    out_json.parent.mkdir(parents=True, exist_ok=True)

    screenshot_dir = None
    if args.screenshot_dir:
        screenshot_dir = Path(args.screenshot_dir).expanduser().resolve()
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    with open(inj_path, "r", encoding="utf-8") as f:
        inj_obj = json.load(f)

    inj_list: List[Dict[str, Any]] = inj_obj.get("injection_list", [])

    driver = build_driver(headless=args.headless)
    driver.set_page_load_timeout(args.page_load_timeout_s)

    accepted_records: List[Dict[str, Any]] = []

    try:
        for idx, item in enumerate(inj_list):
            url = item.get("Url")
            rule_id = item.get("Rule_id")
            js = item.get("Injection_js")

            if not (url and rule_id and js):
                continue

            print(f"\n[{idx+1}/{len(inj_list)}] URL={url} RULE={rule_id}")

            try:
                driver.get(url)
            except WebDriverException as e:
                print(f"[WARN] Failed to load {url}: {e}")
                continue

            try:
                driver.execute_script(js)
            except WebDriverException as e:
                print(f"[WARN] Injection failed for {url} ({rule_id}): {e}")
                continue

            time.sleep(args.post_inject_wait_s)
            injected_html = driver.page_source

            # Screenshot
            shot_path = None
            if screenshot_dir is not None:
                safe_name = f"{idx:05d}_{rule_id}".replace("/", "_")
                shot_path = screenshot_dir / f"{safe_name}.png"
                try:
                    driver.save_screenshot(str(shot_path))
                    print(f"[OK] Screenshot -> {shot_path}")
                except WebDriverException:
                    shot_path = None

            # Human-in-the-loop decision
            while True:
                ans = input("Include this injected example in final dataset? [y/n/q]: ").strip().lower()
                if ans in {"y", "n", "q"}:
                    break

            if ans == "q":
                print("[STOP] Quitting early.")
                break

            if ans == "y":
                accepted_records.append({
                    "Url": url,
                    "Rule_id": rule_id,
                    "Rule_filename": item.get("Rule_filename"),
                    "Injection_js": js,
                    "Injected_html": injected_html,
                    "Screenshot_path": str(shot_path) if shot_path else None,
                    "Timestamp_unix": time.time(),
                })
                print(f"[OK] Accepted ({len(accepted_records)} total)")
            else:
                print("[SKIP] Not included.")

    finally:
        driver.quit()

    # Write once at the end → valid JSON
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({"final_dataset": accepted_records}, f, indent=2)

    print(f"\n[DONE] Final dataset written to {out_json} (count={len(accepted_records)})")


if __name__ == "__main__":
    main()
