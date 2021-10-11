from selenium import webdriver
import time

# 登录
dr = webdriver.Chrome()
dr.get("http://localhost:8080/HKR/")
dr.maximize_window()

# 学生端
# dr.find_element_by_id('loginname').send_keys('yyy')
# dr.find_element_by_id('password').send_keys('123456')
# dr.find_element_by_id('submit').click()
# time.sleep(2)

# # 换头像
# dr.find_element_by_id('img').click()
# dr.find_element_by_xpath('//*[@id="ul_pic"]/li[2]/img').click()

# 提交今日评价
# time.sleep(1)
# dr.refresh()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[2]/td[2]/select').send_keys('9（上晚自习）')
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="tea_td"]/select').send_keys('贾生')
# time.sleep(2)
# dr.find_element_by_xpath('//*[@id="subtn"]').click()

# 修改个人信息
# dr.find_element_by_xpath('//*[@id="_easyui_tree_8"]/span[4]/a').click()
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[1]/td[2]/input').clear()
# time.sleep(2)
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[1]/td[2]/input').send_keys('a')
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[3]/td[2]/input').send_keys('987654')
# dr.find_element_by_xpath('//*[@id="_easyui_textbox_input1"]').send_keys('23')
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[5]/td[2]/select').send_keys('女')
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[6]/td[2]/input').send_keys('银河')
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[8]/td[2]/input').send_keys('163@qq.com')
# dr.find_element_by_xpath('//*[@id="info"]/table/tbody/tr[9]/td[2]/textarea').send_keys('……')
# dr.find_element_by_xpath('//*[@id="btn_modify"]').click()
# d)查询所有好友
# dr.find_element_by_xpath('//*[@id="_easyui_tree_10"]/span[4]/a').click()
# e)退出
# dr.find_element_by_xpath('//*[@id="top"]/div/a[2]/img').click()
# 二、教师模块：
# a)教师管理：查询，重置密码
# 登录
# dr.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()
# dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('13552648187')
# dr.find_element_by_xpath('//*[@id="password"]').send_keys('admin')
# dr.find_element_by_xpath('//*[@id="submit"]').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="_easyui_tree_11"]/span[4]/a').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[9]/div/a').click()
# b)学生管理：姓名和电话号码查询、设置毕业和未毕业状态
# dr.find_element_by_xpath('//*[@id="_easyui_tree_12"]/span[4]/a').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="J-stu"]').send_keys('yyy')
# dr.find_element_by_xpath('//*[@id="J-phone"]').send_keys('13548554150')
# dr.find_element_by_xpath('//*[@id="stu_panel"]/div/div/div[1]/table/tbody/tr/td[4]/a/span').click()
# dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[11]/div/a').click()
# c)课程管理：添加、取消添加课程
# dr.find_element_by_xpath('//*[@id="_easyui_tree_13"]/span[4]/a').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="course_panel"]/div/div/div[1]/table/tbody/tr/td/a/span/span[1]').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input').send_keys('语文')
# dr.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea').send_keys('很难')
# time.sleep(1)
# dr.find_element_by_xpath('/html/body/div[7]/div[3]/a[1]/span/span[2]').click()
# dr.find_element_by_xpath('/html/body/div[7]/div[3]/a[2]/span/span[2]').click()
# d)评价：查询评价，导出当前评价、评价报表
# dr.find_element_by_xpath('//*[@id="_easyui_tree_15"]/span[4]/a').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[2]').click()
# dr.find_element_by_xpath('//*[@id="_easyui_tree_16"]/span[4]/a').click()
# e)历史操作日志：日期查询日志，导出当前操作历史
# dr.find_element_by_xpath('//*[@id="_easyui_tree_18"]/span[4]/a').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="history"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[2]').click()
# i)分页显示数据量，第xx页模块
# dr.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[1]/select').send_keys('20')
# dr.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[7]/input').send_keys('3')
# 三、注册：
# a)用户注册
dr.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[1]').click()
dr.find_element_by_id('loginname').send_keys('ewq')
dr.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys('qwe')
dr.find_element_by_id('pwd').send_keys('123456')
dr.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys('123456')
dr.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()
time.sleep(6)
dr.close()
