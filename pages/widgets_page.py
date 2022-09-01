from tests.widgets_test import AccordianPage


class TestWidgets:
    class TestWidgetsAccordian:
        def test_widgets_accordioan(self, driver):
            link = 'https://demoqa.com/accordian'
            accordian_page = AccordianPage(driver, link)
            accordian_page.open()
            accordian_page.check_accordion()
