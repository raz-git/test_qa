import time
from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:
    class TestWidgetsAccordian:
        def test_widgets_accordioan(self, driver):
            link = 'https://demoqa.com/accordian'
            accordian_page = AccordianPage(driver, link)
            accordian_page.open()
            accordian_page.check_accordion()

    class TestAutoComplete:
        def test_fill_multiple_color_names(self, driver):
            link = 'https://demoqa.com/auto-complete'
            auto_complite_page = AutoCompletePage(driver, link)
            auto_complite_page.open()
            colors = auto_complite_page.fill_input_multi()
            colors_result = auto_complite_page.check_input_in_multi()
            assert  colors == colors_result

        def test_remove_value_from_multiple_color_names(self, driver):
            link = 'https://demoqa.com/auto-complete'
            auto_complite_page = AutoCompletePage(driver, link)
            auto_complite_page.open()
            auto_complite_page.fill_input_multi()
            color_before, color_after = auto_complite_page.remove_element_from_multi()
            assert color_before != color_after, 'added colors missing in the input'

        def test_remove_all_values_from_ulti_color_names(self, driver):
            link = 'https://demoqa.com/auto-complete'
            auto_complite_page = AutoCompletePage(driver, link)
            auto_complite_page.open()
            auto_complite_page.fill_input_multi()
            time.sleep(0.5)
            color_before, color_after = auto_complite_page.remove_all_elements_from_multi()
            assert color_before != len(color_after) and len(color_after) == 1, 'value was not deleted'

        def test_single_color_name(self, driver):
            link = 'https://demoqa.com/auto-complete'
            auto_complite_page = AutoCompletePage(driver, link)
            auto_complite_page.open()
            color = auto_complite_page.fill_input_single()
            color_result = auto_complite_page.check_color_in_single()
            assert color == color_result, 'added colors missing in the input'


