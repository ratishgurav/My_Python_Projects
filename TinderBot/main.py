from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Setup Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Block notification popups (Tinder asks for these constantly)
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

# 2. Manual Login Pause
# The script will pause here. Log in to Tinder manually in the browser.
# Once you see the card stack, press Enter in your Python console to continue.
input("Log in manually, handle the location popup, then press Enter here to start swiping...")

# 3. The Loop
for i in range(10):
    try:
        # Wait up to 10 seconds for the button to be clickable
        # We use a CSS Selector looking for the 'aria-label' which is much more stable
        reject_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Nope']"))
        )

        reject_btn.click()

        # 4. Human Delay
        # You must wait between clicks for the animation to finish
        time.sleep(1)

    except Exception as e:
        # If a popup (like "Add to Home Screen") blocks the click, this catches it
        print(f"Error on swipe {i}: {e}")
        # Option: Try sending the Left Arrow key to the body as a backup
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
        time.sleep(1)

print("Finished swiping.")