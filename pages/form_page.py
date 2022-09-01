from generator.generator import generated_person
from pages.base_page import BasePage
from pages.locators import PracticeFormLocators


class PracticeForm(BasePage):
    locators = PracticeFormLocators

    def fill_form_fields(self):
        person = next(generated_person())
        self.element_is_visible(self.locators.INPUT_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.INPUT_LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.INPUT_GENDER).click()
        self.element_is_visible(self.locators.INPUT_MOBILE_NUMBER).send_keys(person.mobile)
        submit = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(submit)
        submit.click()
        self.delete_footer()
        return person.firstname + ' ' + person.lastname, person.email

    def form_result(self):
        data = []
        result_list = self.element_are_present(self.locators.OUTPUT_TABLE)
        for i in result_list:
            data.append(i.text)
        return data[0], data[1]

