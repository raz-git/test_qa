import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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



