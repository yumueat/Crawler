import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import os
web=Chrome()
web.get("http://lagou.com")
el=web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
lis=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in lis:
    work_name=li.find_element_by_xpath('./div[1]/div[1]/div[1]/a/h3').text
    work_price=li.find_element_by_xpath('./div[1]/div[1]/div[2]/div/span').text
    work_conpany=li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    print(work_conpany,work_name,work_price)