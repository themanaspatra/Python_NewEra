# share the fixtures among all the testcases inside a directory package
import pytest
from selenium import webdriver
from utilities.config import Config


# params is used for parametrized the fixtures
# @pytest.fixture(params=['chrome', 'edge'])
@pytest.fixture()
def driver_(request):
    # browser = request.param

    if Config.BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)

    elif Config.BROWSER == 'edge':
        driver = webdriver.Edge()

    driver.get(Config.URL)
    driver.maximize_window()
    # return driver
    yield driver
    driver.quit()

# code when testcases to be executed for one browser

# @pytest.fixture()
# def driver_():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('detach', True)
#     driver = webdriver.Chrome(options=options)
#
#     driver.get("https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.quit()


# using Config class from utilities.config

# @pytest.fixture()
# def driver_():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('detach', True)
#     driver = webdriver.Chrome(options=options)
#
#     driver.get(Config.URL)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
