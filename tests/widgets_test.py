import time
from pages.widgets_page import AccordianPage, AutoCompletePage, SliderPage, ProgressBarPage, TabsPage


class TestWidgets:
    class TestWidgetsAccordian:
        def test_widgets_accordioan(self, driver):
            link = 'https://demoqa.com/slider'
            accordian_page = AccordianPage(driver, link)
            accordian_page.open()
            accordian_page.check_accordion()

    class TestAutoComplete:
        def test_fill_multiple_color_names(self, driver):
            link = 'https://demoqa.com/slider'
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

    class TestSlider:
        def test_change_data(self, driver):
            link = 'https://demoqa.com/slider'
            slider_page = SliderPage(driver, link)
            slider_page.open()
            slider_page.delete_footer()
            data = slider_page.change_slider_value()
            assert data[0] != data[1], 'slider value has not been changed'


    class TestProgressBar:
        def test_change_progress_bar(self, driver):
            link = 'https://demoqa.com/progress-bar'
            progress_bar_page = ProgressBarPage(driver, link)
            progress_bar_page.open()
            v_before, v_after = progress_bar_page.chage_progress_bar_value()
            assert v_before != v_after, 'the progress bar value has not been changed'


    class TestTabsPage:
        def test_check_text_in_tabs(self, driver):
            link = 'https://demoqa.com/tabs'
            tabs_page = TabsPage(driver, link)
            tabs_page.open()
            w_title, w_text = tabs_page.check_tabs('what')
            o_title, o_text = tabs_page.check_tabs('origin')
            u_title, u_text = tabs_page.check_tabs('use')
            assert w_title == 'what' and w_text != 0
            assert o_title == 'origin' and o_text != 0
            assert u_title == 'use' and u_text != 0

