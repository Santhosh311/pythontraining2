from selenium.webdriver import Chrome
from time import sleep
driver= Chrome(r"C:\Users\Tejashwini S\Desktop\Training\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.find_element_by_link_text("Register").click()
sleep(2)
driver.find_element_by_id("gender-male").click()
sleep(2)
driver.find_element_by_id("FirstName").send_keys("Santhosh")
sleep(2)
driver.find_element_by_id("LastName").send_keys("S")
sleep(2)
driver.find_element_by_name("Email").send_keys("santhu1998@gmail.com")
sleep(2)
driver.find_element_by_name("Password").send_keys("Santhu@1998")
sleep(2)
driver.find_element_by_name("ConfirmPassword").send_keys("Santhu@1998")
sleep(2)
driver.find_element_by_id("register-button").click()
sleep(2)
                                               
