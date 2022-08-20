from pages.elements_page import TextBoxPage

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



