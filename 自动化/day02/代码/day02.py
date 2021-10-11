from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 淘宝登录
# dr = webdriver.Chrome()
# dr.get("https://www.taobao.com")
# dr.maximize_window()
# dr.find_element_by_id("q").send_keys("手机")
# dr.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
# dr.find_element_by_id('fm-login-id').send_keys('1234567')
# dr.find_element_by_id('fm-login-password').send_keys('1234567')
# dr.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
# time.sleep(5)
# dr.switch_to.frame('baxia-dialog-content')
# ele = dr.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# ac = ActionChains(dr)
# if bool(ele):
#     print('登录发现滑动验证码')
#     ac.click_and_hold(ele).move_by_offset(258, 0).perform()
# else:
#     print('登录未发现滑动验证码')
# ac.release()
# dr.save_screenshot("登陆失败.jpg")
# time.sleep(10)
# dr.close()

# 添加购物车
# dr = webdriver.Chrome()
# dr.get("http://www.suning.com")
# dr.maximize_window()
# dr.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys('手机')
# dr.find_element_by_xpath('//*[@id="searchSubmit"]').click()
# dr.find_element_by_xpath('//*[@id="pop418"]/a').click()
# dr.find_element_by_xpath('//*[@id="0000000000-12235115639"]/div/div/div[1]/div[1]/a/img').click()
# data = dr.window_handles
# dr.switch_to.window(data[1])
# dr.find_element_by_xpath('//*[@id="addCart"]').click()
# dr.save_screenshot("添加购物车.jpg")
# time.sleep(5)
# dr.close()
