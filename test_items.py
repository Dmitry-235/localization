from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMain():
    def test_find__card_button(self, browser):
        browser.get(link)
        time.sleep(30)
        browser.implicitly_wait(6)
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
        assert button, "Button find"
