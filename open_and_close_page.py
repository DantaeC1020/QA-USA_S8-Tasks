from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get("https://cnt-31181238-0c08-45ab-ac57-488ae3f11916.containerhub.tripleten-services.com")

# Check url contains tripleten-services.com
assert 'tripleten-services.com' in driver.current_url

# Close the browser
driver.quit()