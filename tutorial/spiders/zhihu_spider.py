# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = [
	'https://www.zhihu.com/',
    ]

    def get_cookies(self):
	driver = webdriver.Chrome()
	driver.get(self.start_urls[0])
	driver.find_element_by_link_text(u'登录').click()
	driver.find_element_by_name('account').clear()
	driver.find_element_by_name('account').send_keys("username")
	dirver.find_element_by_name('password').clear()
	dirvier.find_element_by_name('password').send_keys("password")
	SignInURL = u'https://www.zhihu.com/#signin'

	try:
	    if dirver.find_element_by_id('captcha'):
		while True:
		    if driver.current_url != SignInURL:
			break
	finally:
	    if driver.current_url == SignInURL:
		driver.find_element_by_css_selector('button.sign-button.submit').click()
	    cookies = dirver.get_cookies()
	    dirver.close()
	    return cookies

    def get_titles(self, response):
	sel = scrapy.Selector(response)
	for i in range(1, 10):
	    xml = r'//*[@id="feed-%d"]/div[1]/div[2]/div[2/h2/a/text()]' % (i)
	    title = sel.xpath(xml).extract()
	    if len(title) > 0:
		print str(title[0])	
	
    def parse(self, response):
	return scrapy.Request(url=self.start_urls[0], cookies=self.get_cookies(), callback=self.get_titles)
