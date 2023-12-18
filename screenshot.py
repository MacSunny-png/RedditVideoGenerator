import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# Config
screenshotDir = "/Users/msundgren/RedditStuff/Screenshots"  # Update this path

# Specify the path to chromedriver using the Service class
s = Service('/Users/msundgren/WebDrivers/chrome-mac-x64/Google Chrome for Testing')
driver = webdriver.Chrome(service=s)

def getPostScreenshots(filePrefix, script):
    print("Taking screenshots...")
    driver = __setupDriver(script.url)

    try:
        # Screenshot of the post title
        __takeScreenshot(driver, f"{filePrefix}-Post.png", By.TAG_NAME, 'h1')

        # Locating the comments
        comments = __findTopComments(driver, script)

        # Screenshot of top 3 comments
        for i, comment in enumerate(comments[:3]):  # Limit to top 3 comments
            __takeScreenshot(driver, f"{filePrefix}-Comment-{i}.png", By.XPATH, f"//*[@id='{comment}']")

    finally:
        driver.quit()

def __setupDriver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def __takeScreenshot(driver, filename, by, identifier):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, identifier)))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)  # Allow time for scrolling to finish
        element.screenshot(os.path.join(screenshotDir, filename))
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def __findTopComments(driver, script):
    # Use 'commentId' attribute from the ScreenshotScene objects
    return [comment.commentId for comment in script.frames]

# Example usage (assuming 'script' object is provided as in your existing setup)
# getPostScreenshots('filePrefixExample', script)
