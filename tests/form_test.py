from pages.form_page import PracticeForm


class TestFormPage:
    class TestPracticeForm:
        def test_student_registration_form(self, driver):
            link = 'https://demoqa.com/automation-practice-form'
            form_page = PracticeForm(driver, link)
            form_page.open()
            form_page.add_padding_to_body(120)
            input_data = form_page.fill_form_fields()
            output_data = form_page.form_result()
            assert input_data == output_data, 'name or email does not match'