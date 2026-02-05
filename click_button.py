import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(" https://cnt-cb6d36fe-7494-4698-bd57-d16a9096caf5.containerhub.tripleten-services.com ")

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()