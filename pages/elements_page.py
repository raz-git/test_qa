import time
from random import randint

import requests
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import Select
from generator.generator import generated_person
from pages.locators import ElementsPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, WebTablePageLocators, \
    ButtonPageLocators, LinkPageLocators, DynamicPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

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

class WebTablePage(BasePage):
    locators = WebTablePageLocators

    def add_new_person(self, ):
        count = randint(1, 4)
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.firstname
            last_name = person_info.lastname
            email = person_info.email
            salary = person_info.salary
            age = person_info.age
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -=1
        return [first_name, last_name, str(age), email, str(salary), department]


    def check_new_person(self):
        people_list = self.element_are_present(self.locators.GET_FULL_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, keywrod):
        self.element_is_present(self.locators.SEARCH_INPUT).send_keys(keywrod)

    def check_search_person(self):
        delete = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete.find_element(*WebTablePageLocators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age_updated = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age_updated)
        self.element_is_visible(self.locators.SUBMIT).click()
        return age_updated

    def delete_person(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        msg = self.element_is_present(self.locators.NO_ROWS_MESSAGE).text
        assert msg.lower() == 'no rows found', 'person still present'

    def select_pagination(self):
        count =  [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            pagination = self.element_is_visible(self.locators.SELECT_ALL)
            self.go_to_element(pagination)
            pagination.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.element_are_present(self.locators.GET_FULL_LIST)
        return len(list_rows)

class ButtonPage(BasePage):
    locators = ButtonPageLocators

    def click_on_all_buttons(self):
        double = self.element_is_visible(self.locators.DOUBLE_CLICK)
        self.double_click(double)
        right = self.element_is_visible(self.locators.RIGHT_CLICK)
        self.right_click(right)
        self.element_is_visible(self.locators.CLICK_ME).click()
        result_double = self.element_is_visible(self.locators.DOUBLE_CLICK_RESULT).text
        right_result = self.element_is_visible(self.locators.RIGHT_CLICK_RESULT).text
        single_result = self.element_is_visible(self.locators.CLICK_ME_RESULT).text
        success = 'have done'
        assert success in result_double, 'double click faulure'
        assert success in right_result, 'right click failure'
        assert success in single_result, 'failure click'

class LinksPage(BasePage):
    locators = LinkPageLocators

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code

class DynamicPage(BasePage):
    locators = DynamicPageLocators

    def check_chenged_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC)
        except TimeoutException:
            return False
        return True

    def enable_after_five_sec(self):
        try:
            status = self.element_is_clicable(self.locators.ENABLE_AFTER_FIVE_SEC)
            status.click()
        except TimeoutException:
            return False
        return True