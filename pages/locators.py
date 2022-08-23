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

class RadioButtonPageLocators():
    RADIOBUTTON_FIRST = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    RADIOBUTTON_SECOND = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[for="noRadio"')
    SELECTED = (By.CSS_SELECTOR, 'span[class="text-success"]')

class WebTablePageLocators():
    #add person
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #check table
    GET_FULL_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')

    #update user info
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    NO_ROWS_MESSAGE = (By.CSS_SELECTOR, 'div[class="rt-noData"')

    #test pagination
    SELECT_ALL = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

class ButtonPageLocators():
    DOUBLE_CLICK = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME = (By.CSS_SELECTOR, 'div div:nth-child(3) button')

    #result
    DOUBLE_CLICK_RESULT = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_RESULT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_ME_RESULT = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

class LinkPageLocators():
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'p[id="bad-request"]')