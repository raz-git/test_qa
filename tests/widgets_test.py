import time

from pages.base_page import BasePage
from pages.locators import AccordianPageLocators


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
