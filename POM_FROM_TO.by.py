from selenium.webdriver.common.by import By


# Defining the page class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    # Method that fills out the From field
    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

        # Method that fills out the To field

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)