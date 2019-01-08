from scrapy_service.test.requestsTest.saveHtml import html_test
from scrapy_service.test.requestsTest.saveImg import file_test

if __name__ == '__main__':
    html_test("http://www.kugou.com/song/t5y7342.html",'kugou.html')
    file_test("http://fs.w.kugou.com/201901041305/32c342cb1774dbfef75f26dea5a9bb06/G127/M04/00/09/X5QEAFwsdjeAUEytADjjb71qEN8965.mp3",'song.mp3')