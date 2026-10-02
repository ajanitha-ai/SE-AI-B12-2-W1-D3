from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://www.cricbuzz.com/cricket-match")

    print("Cricbuzz opened successfully!")

    # Wait for the page to finish loading
    page.wait_for_load_state("domcontentloaded")

    # Check whether a live score is present
    live_scores = page.locator("div.cb-col.cb-col-100.cb-scrd-itms")

    if live_scores.count() > 0:
        score = live_scores.first.inner_text()
        print("Live score:")
        print(score)
    else:
        print("No live score currently.")

    # Save screenshot whether or not a live score exists
    page.screenshot(path="score.png")

    browser.close()
