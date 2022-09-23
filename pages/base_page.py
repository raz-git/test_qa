from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clicable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def add_padding_to_body(self, px=100):
        self.driver.execute_script(f"document.getElementsByClassName('body-height')[0].style= 'padding-bottom: {px}px';")

    def delete_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').remove();")

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def action_drag_and_drop_by_offset(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y)
        action.perform()




