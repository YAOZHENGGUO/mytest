from selenium import webdriver
import time

# 任务1 百度搜索
# dr = webdriver.Chrome()
# dr.get("http://www.baidu.com")
# dr.maximize_window()
# dr.find_element_by_id("kw").send_keys("Python自动化")
# dr.find_element_by_id("su").click()
# time.sleep(3)
# dr.quit()

# 任务2
# 输入
# dr = webdriver.Chrome()
# dr.get(r"E:/python自动化测试/qwe/day01/任务/练习的html/frame.html")
# dr.find_element_by_id("input1").send_keys("你好，再见！")
# dr.maximize_window()
# time.sleep(4)
# dr.quit()

# 表单提交
# dr = webdriver.Chrome()
# dr.get(r'E:/python自动化测试/qwe/day01/任务/练习的html/上传文件和下拉列表/autotest.html')
# dr.find_element_by_xpath("//*[@id='accountID']").send_keys('account')
# dr.find_element_by_xpath("//*[@id='passwordID']").send_keys('221113')
# dr.find_element_by_xpath('//*[@id="areaID"]').send_keys('天津市')
# dr.find_element_by_xpath('//*[@id="sexID2"]').click()
# dr.find_element_by_xpath('//*[@value="summer"]').click()
# dr.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r'E:\python自动化测试\test\自动化\day01\任务\1.txt')
# time.sleep(4)
# dr.quit()

# 弹框
# dr = webdriver.Chrome()
# dr.get(r"E:/python自动化测试/qwe/day01/任务/练习的html/弹框的验证/dialogs.html")
# dr.find_element_by_id("confirm").click()
# time.sleep(3)
# dr.switch_to.alert.dismiss()
# time.sleep(3)
# dr.quit()

# 任务3 京东搜索一件商品，查看详情
# dr = webdriver.Chrome()
# dr.get("http://www.jd.com")
# dr.maximize_window()
# dr.find_element_by_id("key").send_keys("华为手机")
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
# dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
# time.sleep(3)
# dr.quit()
