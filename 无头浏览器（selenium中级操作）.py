from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

opt=Options()#设置配置
opt.add_argument("--headless")#增加无头配置
opt.add_argument("--disable-gpu")#增加禁用gpu配制

web=Chrome(options=opt)#调用浏览器并且配置
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

sel_el=web.find_element_by_xpath()#定位到下来列表
sel=Select(sel_el)#对元素进行包装，包装成下拉菜单
for i in range(len(sel.options)):#让浏览器进行调整下拉菜单选项
    sel.select_by_index(i)#按照索引进行切换
    time.sleep()
    table=web.find_element_by_xpath()
    print(table)

print("over!")
web.close()
# web.switch_to.window(web.window_handles[-1])#切换到最后一个窗口
# web.switch_to.window(web.window_handles[0])#切换到第一个窗口
# iframe=web.find_element_by_xpath()#定位到iframe
# web.switch_to.frame(iframe)#切换进iframe
# web.switch_to.default_content()#切换回原页面