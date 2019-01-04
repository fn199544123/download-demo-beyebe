import json

from scrapy_service.request_test.saveHtml import save_to_file
from scrapy_service.webdriver_demo_fangnan.driver_pool.DriverPool import WebDriverPool

driver = WebDriverPool.getOneDriverForTest()
driver.get("https://www.58.com/changecity.html")
cityList = []
for item in driver.find_elements_by_css_selector('a'):
    try:
        dictNow = {"city": item.text, "url": item.get_attribute('href')}
        print(dictNow)
        cityList.append(dictNow)
    except:
        pass
jsonSTR = json.dumps(cityList)
save_to_file("58cityName.txt", jsonSTR)
