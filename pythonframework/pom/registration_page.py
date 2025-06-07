# from selenium import webdriver
from utilities.generic import SeleniumWrapper

# move to test_registraation_page
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=options)

# locators for registration page

register_link = ("link text", "Register")
male_radio_button = ("id", "gender-male")
firstname = ("name", "FirstName")
lastname = ("id", "LastName")
email = ("id", "Email")
password = ("id", "Password")
confirm_password = ("id", "ConfirmPassword")
registration_button = ("id", "register-button")

# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()


class RegistrationPage(SeleniumWrapper):
    def click_registration_link(self):
        # driver.find_element(*register_link).click()
        self.click_on_element(register_link)

    def select_male_radio(self):
        # driver.find_element(*male_radio_button).click()
        self.click_on_element(male_radio_button)

    def enter_firstname(self, fname):
        # driver.find_element(*firstname).send_keys("hari")
        self.enter_text(firstname, value=fname)

    def enter_lastname(self, lname):
        # driver.find_element(*lastname).send_keys("om")
        self.enter_text(lastname, value=lname)

    def enter_email(self, mail):
        # driver.find_element(*email).send_keys("themanas@company.com")
        self.enter_text(email, value=mail)

    def enter_password(self, pwd):
        # driver.find_element(*password).send_keys("Bbs@123")
        self.enter_text(password, value=pwd)

    def enter_confirm_password(self, cpwd):
        # driver.find_element(*confirm_password).send_keys("Bbs@123")
        self.enter_text(confirm_password, value=cpwd)

    def click_registration_button(self):
        # driver.find_element(*registration_button).click()
        self.click_on_element(registration_button)
