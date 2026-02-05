import time

from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://cnt-80ac471e-ea60-4e66-9925-c1c2e6385c8a.containerhub.tripleten-services.com")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the title element using its CSS Selector
driver.find_element(By.CSS_SELECTOR, ".logo-disclaimer")

# Close the browser and end the WebDriver session
driver.quit()
