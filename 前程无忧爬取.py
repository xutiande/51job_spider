import csv
import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
opt=Options()
# opt.add_argument("--disable-blink-features")
opt.add_argument("--disable-blink-features=AutomationControlled")
# opt.add_argument('--incognito')#无痕模式
# opt.add_argument("--disable-extensions")
# opt.add_argument("--disable-infobars")
# opt.add_argument("--no-default-browser-check")
# opt.add_experimental_option("excludeSwitches", ["enable-automation"])
# opt.add_experimental_option("useAutomationExtension", False)
# mobileEmulation = {'deviceName': 'iPhone X'}#模拟手机
# opt.add_experimental_option('mobileEmulation', mobileEmulation)
posts_list=[]
firm_list=[]
wages_list=[]
city_list=[]
welfare_list=[]
city_scale_list=[]
city_attribute_list=[]
city_quality_list=[]
experience_list=[]
Degree_list=[]
time_list=[]
link_address_list=[]
test_list=[]
twos_html_list=[]
one_url='https://we.51job.com/'
# browser = webdriver.Chrome()
browser =webdriver.Chrome(chrome_options=opt)
browser.get(one_url)
def job():
    import time
    test='python'
    # test=input("请输入爬取的岗位：")
    # one_html = 'https://we.51job.com/pc/search?keyword={}&searchType=2&sortType=0&metro='.format(test)  # 获取关键词链接
    one_html = 'https://we.51job.com/pc/search?keyword={}&searchType=2&sortType=0&metro='.format(test)
    browser.get(one_html)
    browser.implicitly_wait(10)  # 等待时长最多不超过10秒
    # time.sleep(5)
    p=1
    with open(r"D:/python爬取写入文件/work1.csv", 'a', encoding='gbk', newline="") as f:   #写入csv文件
        w = csv.writer(f)
        w.writerow(['职位', '公司名字', '工资', '城市', '福利', '公司规模', '公司属性', '公司性质', '工作经验', '学历','发布时间', '网址','岗位信息'])
        for i in range(1,201):  #爬取多少组就写多少
            sleep(2*random.random())
            for s in range(1,51):
                sleep(5 * random.random() / 5)
                browser.execute_script("window.scrollBy(0,50)")
                list_div=browser.find_elements(By.XPATH,'//div[@class="j_joblist"]/div') # 获取当前页面总共有多少条职位信息
                sleep(5 * random.random())
                post = browser.find_element(By.XPATH,'//div[@class="j_joblist"]/div[{}]/a/div/span[1]'.format(s)).text  #职位
                print(post)
                firm = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/div[2]/a'.format(s)).text  # 公司名字
                wages = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a/p[1]/span[1]'.format(s)).text         #   工资
                city = browser.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a/p[1]/span[2]/span[1]'.format(s)).text       #城市
                welfare = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a/p[2]'.format(s)).text               #福利
                welfares=welfare.replace('\n','|')
                city_scale = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/div[2]/p[1]'.format(s)).text           #公司规模
                city_scales=city_scale[4:]
                city_attribute = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/div[2]/p[2]'.format(s)).text           #公司属性
                city_quality = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/div[2]/p[1]'.format(s)).text         #公司性质
                city_qualitys=city_quality[0:3]
                experience = browser.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a/p[1]/span[2]/span[3]'.format(s)).text  # 工作经验
                Degree = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a/p[1]/span[2]/span[5]'.format(s)).text  # 学历
                time=browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a/div/span[2]'.format(s)).text             #时间
                link_address=browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{}]/a'.format(s)).get_attribute('href')   #网址

                for j in range(len(list_div)):
                    list_div[j].click() # 点击某个item，进入到详情页
                    windows = browser.window_handles
                    browser.switch_to.window(windows[-1]) # 切换到最后一个标签卡
                    sleep(5 * random.random())
                    # browser.execute_script("window.scrollBy(0,50)")
                    WebDriverWait(browser,50,0.2).until(EC.presence_of_element_located((By.XPATH,'//div[@class="bmsg job_msg inbox"]')))
                    # print("--------------------------")
                    # print(browser.page_source)
                    # print("--------------------------")
                    j+=1
                    posts = browser.find_element(By.XPATH,'//div[@class="bmsg job_msg inbox"]').text #岗位信息
                    print(posts)
                    print('----------------------------')
                    sleep(5 * random.random() / 5)
                    browser.close() # 关闭当前标签页
                    windows = browser.window_handles
                    sleep(5 * random.random() / 5)
                    browser.switch_to.window(windows[0])  # 切换到第一个标签卡
                    sleep(5 * random.random() / 5)
                    w.writerow([post, firm, wages, city, welfares, city_scales, city_attribute, city_qualitys, experience, Degree, time, link_address, posts])  # 写入
            sleep(5 * random.random())
            browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/button[2]/i').click()
            a=1

    browser.close()




if __name__=="__main__":
    job()

