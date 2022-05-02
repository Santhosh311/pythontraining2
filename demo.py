from selenium.webdriver import Chrome
driver=Chrome(r"C:\Users\Tejashwini S\Desktop\Training\chromedriver.exe")

driver.get("https://app.joinsuperset.com/join/#/signup/student/jobprofiles/434299c0-14cf-4cee-8266-4c9bc1905ce2")

driver.maximize_window()
current_url= driver.title
url= driver.current_url
#sleep(4)

