import random
import time

from generator.generator import generated_color
from pages.base_page import BasePage
from pages.locators import AccordianPageLocators, AutoCompletePageLocators

from selenium.webdriver.common.keys import Keys


class AccordianPage(BasePage):
    locators = AccordianPageLocators

    def check_accordion(self):
        first = self.element_is_present(self.locators.SECTION_CONTENT_1).text
        self.element_is_present(self.locators.SECTION_2).click()
        second = self.element_is_present(self.locators.SECTION_CONTENT_2).text
        find = self.element_is_visible(self.locators.SECTION_3)
        self.go_to_element(find)
        find.click()
        thirt = self.element_is_present(self.locators.SECTION_CONTENT_3).text
        assert 'Lorem Ipsum is simply dummy text of the printing and' in first
        assert 'Contrary to popular belief, Lorem Ipsum is not simply random text' in second
        assert 'It is a long established fact that a reader will be' in thirt

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            multi = self.element_is_clicable(self.locators.MULTIPLE)
            multi.send_keys(color)
            multi.send_keys(Keys.ENTER)
        return colors

    def remove_element_from_multi(self):
        len_before = len(self.element_are_visible(self.locators.MULTIPLE_ITEM))
        remove_item = self.element_are_visible(self.locators.MULTIPLE_CLOSE)
        for value in remove_item:
            value.click()
            break
        len_after = len(self.element_are_visible(self.locators.MULTIPLE_ITEM))
        return len_before, len_after

    def check_input_in_multi(self):
        color_list = self.element_are_present(self.locators.MULTIPLE_ITEM)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def remove_all_elements_from_multi(self):
        len_before = len(self.element_are_present(self.locators.MULTIPLE_ITEM))
        self.element_is_present(self.locators.MULTIPLE_CLOSE_ALL_ELEMENTS).click()
        items = self.element_are_present(self.locators.MULTIPLE)
        len_after = []
        for item in items:
            len_after.append(item.text)
        return len_before, len_after

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clicable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_CONTAINER)
        return color.text