from pages.alerts_frame_window_page import BrowserAlerts, FramePage, NestedFramePage, ModalDialogPage


class TestAlertFrameWindow:
    class TestBrowserAlerts:
        def test_alert(self, driver):
            link = 'https://demoqa.com/alerts'
            alert_page = BrowserAlerts(driver, link)
            alert_page.open()
            alert = alert_page.check_alert_appear_five_sec()
            assert alert == 'This alert appeared after 5 seconds'

        def test_confirm_box(self, driver):
            link = 'https://demoqa.com/alerts'
            alert_page = BrowserAlerts(driver, link)
            alert_page.open()
            alert = alert_page.check_confirm_alert()
            assert 'ok' in alert.lower()

        def test_prompt(self, driver):
            link = 'https://demoqa.com/alerts'
            alert_page = BrowserAlerts(driver, link)
            alert_page.open()
            alert_page.check_prompt()

    class TestFramePage:
        def test_frames(self, driver):
            link = 'https://demoqa.com/frames'
            frame_page = FramePage(driver, link)
            frame_page.open()
            data_frame1 = frame_page.check_frame(1)
            data_frame2 = frame_page.check_frame(2)
            assert data_frame1 == ['This is a sample page', '500px', '350px']
            assert data_frame2 == ['This is a sample page', '100px', '100px']

    class TestNestedFramePage:
        def test_nested_frame(self, driver):
            link = 'https://demoqa.com/nestedframes'
            nested_page = NestedFramePage(driver, link)
            nested_page.open()
            data_parent, data_child = nested_page.check_nested_frame()
            assert data_parent == 'Parent frame'
            assert data_child == 'Child Iframe'

    class TestModalDialogPage:
        def test_modal_dialog(self, driver):
            link = 'https://demoqa.com/modal-dialogs'
            modal_page = ModalDialogPage(driver, link)
            modal_page.open()
            data_text, data_title = modal_page.check_small_modal_dialogs()
            assert data_title == 'Small Modal', 'small modal window is broken, or title is changed'
            assert 'small modal' in data_text, 'small modal window is broken, or text in body is changed'
            data_text, data_title = modal_page.check_large_modal_dialogs()
            assert data_title == 'Large Modal', 'large modal window is broken, or title is changed'
            assert 'Lorem Ipsum is simply dummy text' in data_text, 'large modal window is broken, or text in body is changed'
