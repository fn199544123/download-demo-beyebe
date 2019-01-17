from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor="http://192.168.10.61:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("http://www.baidu.com")
print(driver.title)
driver.close()
