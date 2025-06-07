# pytest
import pytest
from pom.registration_page import RegistrationPage
from utilities.config import Config
import read_excel
"""
1. module name: test_*.py or *_test.py
2. class name: Test_Class_name
3. function/method: test_method()
"""


# __init__ should not be present inside the test class (while using pytest)
# i.e. pytest automatically pytest will call it

# data = [("steve", "jobs", "steve@jobs.com", "steve123", "steve123"),
#         ("bill", "gates", "bill@gates.com", "bill123", "bill123")]

data = read_excel.get_data()


# @pytest.mark.usefixtures("driver_")
class TestRegister:

    @pytest.mark.parametrize("fname, lname, mail, pwd, cpwd", data)
    def test_register(self, fname, lname, mail, pwd, cpwd, driver_):
        try:
            rp = RegistrationPage(driver_)
            rp.click_registration_link()
            rp.select_male_radio()
            rp.enter_firstname(fname)
            rp.enter_lastname(lname)
            rp.enter_email(mail)
            rp.enter_password(pwd)
            rp.enter_confirm_password(cpwd)
            # rp.click_registration_button()

        except Exception as msg:
            from datetime import datetime
            dt = datetime.now()

            # driver_.save_screenshot("ss1.png")
            driver_.save_screenshot(Config.SCREEN_SHOT + f"screenshot-{dt.day}-{dt.hour}.png")
            # driver_.get_screenshot_as_file(Config.SCREEN_SHOT + f"screenshot-{dt.date()}-{dt.time()}.png")
            raise msg


# driver.quit()
