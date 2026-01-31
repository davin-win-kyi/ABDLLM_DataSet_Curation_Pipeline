#!/usr/bin/env python3
"""
Overview: The following file extracts the content of the target 
websites that are provided by the user
"""

from __future__ import annotations
import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException


def build_driver(headless: bool) -> webdriver.Chrome:
    # Building the selenium driver with provided options
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,900")
    opts.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    return webdriver.Chrome(options=opts)


def wait_for_dom_ready(driver: webdriver.Chrome, timeout_s: int) -> None:
    # Used to load the webpage for the driver
    # which usually includes some amount of delay time
    WebDriverWait(driver, timeout_s).until(
        lambda d: d.execute_script("return document.readyState") in ("interactive", "complete")
    )


def build_arg_parser() -> argparse.ArgumentParser:
    """
    Configurations for webscraping
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("--in_json", type=str, required=True, help="dataset_websites.json input")
    ap.add_argument("--out_json", type=str, required=True, help="output JSON path")
    ap.add_argument("--headless", action="store_true", help="Run Chrome headless")
    ap.add_argument("--page_load_timeout_s", type=int, default=5, help="Selenium page load timeout")
    ap.add_argument("--dom_ready_timeout_s", type=int, default=5, help="Wait for document.readyState")
    ap.add_argument("--extra_wait_s", type=float, default=5, help="Extra wait after DOM ready")
    ap.add_argument("--sleep_between_sites_s", type=float, default=1.0, help="Rate limiting between sites")
    ap.add_argument("--max_sites", type=int, default=0, help="If >0, scrape only first N sites")
    ap.add_argument("--screenshot_dir", type=str, default=None, help="Optional directory to save screenshots")
    return ap


def scrape_single_site(
    driver,
    url: str,
    index: int,
    *,
    dom_ready_timeout_s: int,
    extra_wait_s: float,
    screenshot_dir: Optional[Path],
) -> Dict[str, Any]:
    entry: Dict[str, Any] = {
        "Url": url,
        "Final_url": None,
        "Title": None,
        "Source_code": None,
        "Screenshot_path": None,
    }

    # Load the page
    try:
        driver.get(url)
    except WebDriverException as e:
        entry["Source_code"] = f"<!-- ERROR loading {url}: {e} -->"
        return entry

    # Waiting time for DOM to be ready
    try:
        wait_for_dom_ready(driver, dom_ready_timeout_s)
    except TimeoutException:
        pass
    if extra_wait_s > 0:
        time.sleep(extra_wait_s)

    # Extract website information
    try:
        entry["Final_url"] = driver.current_url
        entry["Title"] = driver.title
        entry["Source_code"] = driver.page_source
    except WebDriverException as e:
        entry["Source_code"] = f"<!-- ERROR capturing page_source for {url}: {e} -->"

    # Save screenshot for later analysis
    if screenshot_dir is not None:
        shot_path = screenshot_dir / f"{index:05d}.png"
        try:
            driver.save_screenshot(str(shot_path))
            entry["Screenshot_path"] = str(shot_path)
        except WebDriverException:
            pass

    return entry


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    # this is where the source code will be stored
    with open(args.in_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # extract target URLs
    urls: List[str] = [
        x["Url"]
        for x in data.get("dataset_websites", [])
        if "Url" in x
    ]
    if args.max_sites > 0:
        urls = urls[: args.max_sites]

    # this is where the source code will be stored
    out_path = Path(args.out_json).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # this is where the screenshots will be stored
    screenshot_dir: Optional[Path] = None
    if args.screenshot_dir:
        screenshot_dir = Path(args.screenshot_dir).expanduser().resolve()
        screenshot_dir.mkdir(parents=True, exist_ok=True)

    # establishing selenium driver
    driver = build_driver(headless=args.headless)
    driver.set_page_load_timeout(args.page_load_timeout_s)

    # where the source code will be stored
    out_list: List[Dict[str, Any]] = []
    try:
        for i, url in enumerate(urls, start=1):
            print(f"[{i}/{len(urls)}] Loading {url}")

            entry = scrape_single_site(
                driver,
                url,
                i,
                dom_ready_timeout_s=args.dom_ready_timeout_s,
                extra_wait_s=args.extra_wait_s,
                screenshot_dir=screenshot_dir,
            )

            out_list.append(entry)
            time.sleep(args.sleep_between_sites_s)
    finally:
        driver.quit()
    out_obj = {"source_code_list": out_list}
    out_path.write_text(json.dumps(out_obj, indent=2), encoding="utf-8")

    print(f"Website sourcecode is in {len(out_list)} entries -> {out_path}")


if __name__ == "__main__":
    main()

