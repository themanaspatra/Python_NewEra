import pytest
from selenium import webdriver
from pom.login_page import Login


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

data = [("steve@jobs.com", "steve123")]

class TestLoginPage:

    @pytest.mark.parametrize("mail pwd", data)
    def test_login(self, mail, pwd, driver_):
        l = Login(driver_)
        l.click_on_login_link()
        l.email(mail)
        l.password(pwd)
        l.click_on_login_button()

