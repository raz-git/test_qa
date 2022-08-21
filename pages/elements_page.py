import time
from random import randint

from generator.generator import generated_person
from pages.locators import ElementsPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = ElementsPageLocators

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_adress = person_info.current_adress
        permanent_adress = person_info.permanent_adress
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys(current_adress)
        self.element_is_visible(self.locators.PERMANENT_ADRESS).send_keys(permanent_adress)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_adress, permanent_adress

    def check_field_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_present(self.locators.CREATED_CURRENT_ADRESS).text.split(':')[1]
        permanent_adress = self.element_is_present(self.locators.CREATED_PERMANENT_ADRESS).text.split(':')[1]
        #print(full_name, email, current_adress, permanent_adress)
        return full_name, email, current_adress, permanent_adress

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    def click_random_checkbox(self):
        item_lsit = self.element_are_visible(self.locators.ITEM_LIST)
        cnt = 20
        while cnt > 0:
            item = item_lsit[randint(1, len(item_lsit) - 1)]
            self.go_to_element(item)
            item.click()
            cnt -=1

    def get_checked_items(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()


    def get_output_result(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_button_and_check_selected(self):
        self.element_is_present(self.locators.RADIOBUTTON_FIRST).click()
        selected = self.element_is_present(self.locators.SELECTED).text
        assert selected == 'Yes', 'Radiobutton "YES" is not selected '
        self.element_is_present(self.locators.RADIOBUTTON_SECOND).click()
        selected = self.element_is_present(self.locators.SELECTED).text
        assert selected == 'Impressive', 'Radiobutton "IMPRESSIVE" is not selected '
        self.element_is_present(self.locators.NO_RADIOBUTTON).click()
        selected = self.element_is_present(self.locators.SELECTED).text
        assert selected == 'No', 'Radiobutton "NO" is not selected '

