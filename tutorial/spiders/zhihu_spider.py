# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com',
    ]

    def get_cookies(self):
        driver = webdriver.Chrome()
        driver.get(self.start_urls[0])
        driver.find_element_by_link_text(u'登录').click()
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys("18600682316")
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys("huzichunJOHN1234")
        SignInURL = u'https://www.zhihu.com/#signin'

        try:
            #TODO: add captcha recongnize
            if dirver.find_element_by_id('captcha'):
                print "captcha"
                while True:
                    print "#" * 20
                    print driver.current_url
                    print "#" * 20
                    if driver.current_url != SignInURL:
                        break
        finally:
            if driver.current_url == SignInURL:
                driver.find_element_by_css_selector('button.sign-button.submit').click()
            cookies = driver.get_cookies()
            #driver.close()
            import time
            time.sleep(5)
            return cookies

    def get_titles(self, response):
        sel = scrapy.Selector(response)
        for i in range(10):
            xml = r'//*[@id="feed-%d"]/div[1]/div[2]/div[2]/h2/a/text()' % (i)
            title = sel.xpath(xml).extract()
            if len(title) > 0:
                print "#" * 20
                print str(title[0])
                print "#" * 20

    def parse(self, response):
        return scrapy.Request(url=self.start_urls[0], cookies=self.get_cookies(), callback=self.get_titles)
