#!/usr/bin/env python3
"""
Overview: This file will load up the selenium injections and will 
add injection scripts based on a human reviwers feedback
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

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


def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    ap.add_argument("--injection_json", type=str, required=True)
    ap.add_argument("--out_json", type=str, required=True)
    ap.add_argument("--headless", action="store_true")
    ap.add_argument("--page_load_timeout_s", type=int, default=30)
    ap.add_argument("--post_inject_wait_s", type=float, default=1.0)
    ap.add_argument("--screenshot_dir", type=str, default=None)
    return ap


def resolve_paths(args: argparse.Namespace) -> Tuple[Path, Path, Optional[Path]]:
    inj_path = Path(args.injection_json).expanduser().resolve()
    out_json = Path(args.out_json).expanduser().resolve()
    out_json.parent.mkdir(parents=True, exist_ok=True)

    screenshot_dir: Optional[Path] = None
    if args.screenshot_dir:
        screenshot_dir = Path(args.screenshot_dir).expanduser().resolve()
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    return inj_path, out_json, screenshot_dir


def take_screenshot(
    driver: webdriver.Chrome,
    screenshot_dir: Optional[Path],
    idx: int,
    rule_id: str,
) -> Optional[Path]:
    if screenshot_dir is None:
        return None

    safe_name = f"{idx:05d}_{rule_id}".replace("/", "_")
    shot_path = screenshot_dir / f"{safe_name}.png"
    try:
        driver.save_screenshot(str(shot_path))
        print(f"[OK] Screenshot -> {shot_path}")
        return shot_path
    except WebDriverException:
        return None
    

def prompt_human_decision() -> str:
    """
    Returns one of: "y", "n", "q"
    """
    while True:
        ans = input("Include this injected example in final dataset? [y/n/q]: ").strip().lower()
        if ans in {"y", "n", "q"}:
            return ans
    

def run_human_review_loop(
    driver: webdriver.Chrome,
    inj_list: List[Dict[str, Any]],
    *,
    post_inject_wait_s: float,
    screenshot_dir: Optional[Path],
) -> List[Dict[str, Any]]:
    """
    Runs the Selenium + injection + screenshot + human prompt loop.
    Returns the accepted_records list.
    """
    accepted_records: List[Dict[str, Any]] = []

    for idx, item in enumerate(inj_list):
        url = item.get("url")
        rule_id = (item.get("WCAG_technique") or {}).get("technique_id")
        js = (item.get("injection") or {}).get("injection_js")

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

        time.sleep(post_inject_wait_s)
        injected_html = driver.page_source

        # Take Screenshot
        shot_path = take_screenshot(driver, screenshot_dir, idx, rule_id)

        # Human-in-the-loop decision
        ans = prompt_human_decision()

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
    return accepted_records


def main() -> None:
    args = build_arg_parser().parse_args()
    inj_path, out_json, screenshot_dir = resolve_paths(args)

    with open(inj_path, "r", encoding="utf-8") as f:
        inj_obj = json.load(f)
    inj_list: List[Dict[str, Any]] = inj_obj.get("injections", [])

    driver = build_driver(headless=args.headless)
    driver.set_page_load_timeout(args.page_load_timeout_s)

    # print("INJ LIST SIZE: ", len(inj_list))

    try:
        accepted_records = run_human_review_loop(
            driver,
            inj_list,
            post_inject_wait_s=args.post_inject_wait_s,
            screenshot_dir=screenshot_dir,
        )
    finally:
        driver.quit()

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({"final_dataset": accepted_records}, f, indent=2)

    print(f"\nFinal dataset written to -> {out_json} (count={len(accepted_records)})")


if __name__ == "__main__":
    main()
