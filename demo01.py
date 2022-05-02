from selenium.webdriver import Chrome
from time import sleep
driver=Chrome(r"C:\Users\Tejashwini S\Desktop\Training\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")

driver.find_element_by_xpath("//input[@type='text']").send_keys("Computer")
driver.find_element_by_xpath("//input[@type='submit']").click()

ele=driver.find_elements_by_xpath("//a[text()='Build your own cheap computer']/../..//span[@class='price actual-price']")
print(ele)
