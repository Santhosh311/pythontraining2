from selenium.webdriver import Chrome
from time import sleep
driver= Chrome(r"C:\Users\Tejashwini S\Desktop\Training\chromedriver.exe")
driver.get("https://www.ajio.com/")
driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("Shoes")
driver.find_element_by_xpath("//span[@class='ic-search']").click()

