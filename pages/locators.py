from selenium.webdriver.common.by import By

class ElementsPageLocators():

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators():
    EXPAND_ALL = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')