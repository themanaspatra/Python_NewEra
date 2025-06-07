from selenium import webdriver
from utilities.generic import SeleniumWrapper


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)


driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

login_click = ("link text", "Log in")
login_email = ("xpath", "//input[@id='Email']")
login_password = ("xpath", "//input[@id='Password']")
login_button = ("xpath", "//input[@class='button-1 login-button']")


class Login(SeleniumWrapper):
    def click_on_login_link(self):
        self.click_on_element(login_click)

    def email(self):
        self.enter_text(login_email, value="themanas@company.com")

    def password(self):
        self.enter_text(login_password, value="Bbs@123")

    def click_on_login_button(self):
        self.click_on_element(login_button)

