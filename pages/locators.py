from selenium.webdriver.common.by import By
from random import randint

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

class DynamicPageLocators():
    ENABLE_AFTER_FIVE_SEC = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_FIVE_SEC = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')


class PracticeFormLocators:
    #required fields
    INPUT_NAME = (By.CSS_SELECTOR, 'input[id="firstName"')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"')
    INPUT_GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{randint(1,3)}"]')
    INPUT_MOBILE_NUMBER = (By.CSS_SELECTOR, 'input[id="userNumber"')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"')
    OUTPUT_TABLE = (By.CSS_SELECTOR, 'tbody td:nth-child(2n)')

class BrowserAlertsLocators:
    #alert button
    CLICK_AFTER_FIVE_SEC = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CLICK_ALERT_CONFIRM = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CLICK_ALERT_PROMPT = (By.CSS_SELECTOR, 'button[id="promtButton"]')

    RESULT_CONFIRM = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    RESULT_PROMPT = (By.CSS_SELECTOR, 'span[id="promptResult"]')

class FramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class  NestedFramePageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')

class ModalDialogPageLocators:
    SMALL_MODAL_OPEN = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_CLOSE = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    SMALL_BODY_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    SMALL_TITLE_TEXT = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_OPEN = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_CLOSE = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    LARGE_BODY_TEXT = (By.CSS_SELECTOR, '.modal-body p')
    LARGE_TITLE_TEXT = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-lg"]')

class AccordianPageLocators:
    SECTION_1 = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_1 = (By.CSS_SELECTOR, '#section1Content p')
    SECTION_2 = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_2 = (By.CSS_SELECTOR, '#section2Content p')
    SECTION_3 = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_3 = (By.CSS_SELECTOR, '#section3Content p')

class AutoCompletePageLocators:
    MULTIPLE = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_ITEM = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTIPLE_CLOSE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    MULTIPLE_CLOSE_ALL_ELEMENTS = (By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[2]/div')
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    VALUE_SLIDER = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    TITLE_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TITLE_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TITLE_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TITLE_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    CONTENT_WHAT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    CONTENT_ORIGIN = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    CONTENT_USE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    CONTENT_MORE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')

