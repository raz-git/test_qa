import time

from selenium.common import UnexpectedAlertPresentException

from generator.generator import generated_person
from pages.base_page import BasePage
from pages.locators import BrowserAlertsLocators, FramePageLocators, NestedFramePageLocators, ModalDialogPageLocators
import time


class BrowserAlerts(BasePage):
    locators = BrowserAlertsLocators

    def check_alert_appear_five_sec(self):
        self.element_is_visible(self.locators.CLICK_AFTER_FIVE_SEC).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CLICK_ALERT_CONFIRM).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.RESULT_CONFIRM).text
        return text_result

    def check_prompt(self):
        person = next(generated_person())
        text = person.firstname
        self.element_is_visible(self.locators.CLICK_ALERT_PROMPT).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.RESULT_PROMPT).text
        assert text.lower() in text_result.lower()

class FramePage(BasePage):
    locators = FramePageLocators

    def check_frame(self, frame_num):
        if frame_num == 1:
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]
        self.driver.switch_to.default_content()
        if frame_num == 2:
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]
        self.driver.switch_to.default_content()


class NestedFramePage(BasePage):
    locators = NestedFramePageLocators

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        print(parent_text, child_text)
        return parent_text, child_text

class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators

    def check_small_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_OPEN).click()
        text = self.element_is_visible(self.locators.SMALL_BODY_TEXT).text
        title = self.element_is_visible(self.locators.SMALL_TITLE_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE).click()
        return text, title

    def check_large_modal_dialogs(self):
        self.element_is_visible(self.locators.LARGE_MODAL_OPEN).click()
        text = self.element_is_visible(self.locators.LARGE_BODY_TEXT).text
        title = self.element_is_visible(self.locators.LARGE_TITLE_TEXT).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE).click()
        return text, title

