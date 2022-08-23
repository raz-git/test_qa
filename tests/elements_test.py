import time

import pytest
from random import randint

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage


class TestElements:
    class TestTextTexBox:
        def test_text_box(self, driver):
            link = 'https://demoqa.com/text-box'
            text_box_page = TextBoxPage(driver, link)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            out_full_name, out_email, out_current_address, out_permanent_address = text_box_page.check_field_form()
            assert full_name == out_full_name
            assert email == out_email
            assert current_address == out_current_address
            assert permanent_address == out_permanent_address

    class TestCheckBox:
        def test_check_box(self, driver):
            link = 'https://demoqa.com/checkbox'
            check_box_page = CheckBoxPage(driver, link)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_text = check_box_page.get_checked_items()
            output_text = check_box_page.get_output_result()
            assert input_text == output_text, 'checkbox is not selected, or does not match'

    class TestRadioButton:
        @pytest.mark.xfail()
        def test_radio_button(self, driver):
            link = 'https://demoqa.com/radio-button'
            radio_button_page = RadioButtonPage(driver, link)
            radio_button_page.open()
            radio_button_page.click_radio_button_and_check_selected()

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            link = 'https://demoqa.com/webtables'
            web_table_page = WebTablePage(driver, link)
            web_table_page.open()
            person = web_table_page.add_new_person()
            output_list = web_table_page.check_new_person()
            assert person in output_list, 'added fields are not in list'

        def test_web_table_search_person(self, driver):
            link = 'https://demoqa.com/webtables'
            web_table_page = WebTablePage(driver, link)
            web_table_page.open()
            new_person = web_table_page.add_new_person()[randint(1,5)]
            time.sleep(0.25)
            web_table_page.search_person(new_person)
            data = web_table_page.check_search_person()
            assert new_person in data, 'added person are not in table'

        def test_web_table_update_person_info(self, driver):
            link = 'https://demoqa.com/webtables'
            web_table_page = WebTablePage(driver, link)
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person_info()
            time.sleep(0.25)
            row = web_table_page.check_search_person()
            assert str(age) in row, 'person info does not updated'

        def test_web_table_delete_person(self, driver):
            link = 'https://demoqa.com/webtables'
            web_table_page = WebTablePage(driver, link)
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            web_table_page.check_deleted_person()

        def test_web_table_pagination_is_correct(self, driver):
            link = 'https://demoqa.com/webtables'
            web_table_page = WebTablePage(driver, link)
            web_table_page.open()
            count = web_table_page.select_pagination()
            assert count == [5, 10, 20, 25, 50, 100], 'pagination work incorrectly, out of vision'

    class TestButtonPage:
        def test_click_on_button(self, driver):
            link = 'https://demoqa.com/buttons'
            button_page = ButtonPage(driver, link)
            button_page.open()
            button_page.click_on_all_buttons()

    class TestLinkPage:
        def test_check_link(self, driver):
            link = 'https://demoqa.com/links'
            link_page = LinksPage(driver, link)
            link_page.open()
            href, current_url = link_page.check_new_tab_simple_link()
            assert href == current_url, 'link is broken'

        def test_broken_link(self, driver):
            link = 'https://demoqa.com/links'
            link_page = LinksPage(driver, link)
            link_page.open()
            response = link_page.check_broken_link('https://demoqa.com/bad-request')
            assert response == 400












