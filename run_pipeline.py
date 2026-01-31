#!/usr/bin/env python3
"""
run_pipeline.py is used to run the entire dataset curation pipeline 
for WCAG errors from start to finish. 

It includes the following steps: 
1. Indexing of WCAG techniques
2. Webscraping of the souce code of target websites
3. Generation of injection script 
4. Manual dataset selection via selenium 
"""

from __future__ import annotations
import subprocess
import sys
from pathlib import Path


# ======================= CONFIGURATION VARIABLES =============================
# Output directory
OUT_DIR = "out"

# WCAG related paths
WCAG_DIR = "wcag_techniques"
WEBSITES_JSON = "out/websites.json"
DATASET_WCAG_TECHNIQUES = "out/index_wcag_techniques.json"

# Screenshots directory
SCREENSHOT_DIR = "out/screenshots"

# Scraping hyperparameters 
REQUEST_SLEEP_S = 1.0
SELENIUM_HEADLESS = True
PAGE_LOAD_TIMEOUT_S = 10
POST_INJECT_WAIT_S = 1.0
DOM_READY_TIMEOUT_S = 5
EXTRA_WAIT_S = 5.0
MAX_SITES = 2
# ===============================================================================


"""
Run the subprocess command for each of the pipeline
"""
def run(cmd: list[str]) -> None:
    print("\n>>>", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    py = sys.executable

    out_dir = Path(OUT_DIR).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # dataset curation - output related paths
    source_code_json = out_dir / "website_sourcecode_list.json"
    injection_json = out_dir / "injection_scripts.json"
    final_json = out_dir / "final_wcag_errors_dataset.json"


    # 1) Collect WCAG failure content###########################################
    run([
        py, "collect_wcag_failures.py",
        "--wcag_dir", WCAG_DIR,
        "--out_dir", str(out_dir)
    ])


    # 2) Collect website source code#############################################
    cmd2 = [
        py, "scrape_websites.py",
        "--in_json", WEBSITES_JSON,
        "--out_json", str(source_code_json),
        "--page_load_timeout_s", str(PAGE_LOAD_TIMEOUT_S),
        "--dom_ready_timeout_s", str(DOM_READY_TIMEOUT_S),
        "--extra_wait_s", str(EXTRA_WAIT_S),
        "--sleep_between_sites_s", str(REQUEST_SLEEP_S),
        "--screenshot_dir", str(SCREENSHOT_DIR)
    ]
    # speeds up dataset curation runtime
    if SELENIUM_HEADLESS:
        cmd2.append("--headless")
    # if max_sites is not set for the user
    if MAX_SITES > 0:
        cmd2.extend(["--max_sites", str(MAX_SITES)])
    run(cmd2)


    # 3) Injection script generation###############################################
    run([
        py, "injection_script_generation.py",
        "--source_code_json", str(source_code_json),
        "--index_wcag_techniques", str(DATASET_WCAG_TECHNIQUES),
        "--out_json", str(injection_json),
        "--max_sites", str(MAX_SITES),
    ])


    # 4) Selenium injection for dataset selection##################################
    cmd4 = [
        py, "selenium_injection.py",
        "--injection_json", str(injection_json),
        "--out_json", str(final_json),
        "--page_load_timeout_s", str(PAGE_LOAD_TIMEOUT_S),
        "--post_inject_wait_s", str(POST_INJECT_WAIT_S),
    ]
    # if SELENIUM_HEADLESS:
    #     cmd4.append("--headless")
    if SCREENSHOT_DIR:
        Path(SCREENSHOT_DIR).mkdir(parents=True, exist_ok=True)
        cmd4.extend(["--screenshot_dir", SCREENSHOT_DIR])
    run(cmd4)

    print("\n[PIPELINE COMPLETE]")
    print("Final dataset path ->    ", final_json)


if __name__ == "__main__":
    main()
