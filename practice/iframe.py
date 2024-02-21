from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()

driver.find_element("xpath", '//p[text()="Login or Create Account"]').click()

time.sleep(5)
web_element = driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(web_element)
driver.find_element("xpath", '//div[@id="container"]').click()
time.sleep(3)
handle = driver.window_handles
driver.switch_to.window(handle[1])
driver.close()
driver.switch_to.window(handle[0])
time.sleep(3)

driver.switch_to.default_content()
driver.find_element("xpath", '//input[@id="username"]').send_keys("abc@gmail.com")
time.sleep(2)
driver.find_element("xpath", "//span[@class='commonModal__close']").click()
time.sleep(2)
driver.close()
