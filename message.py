# coding=UTF-8
# !/usr/local/bin/ python
from page_to_page import  Login
from time import sleep
from test_case.elements.element_loc import *
from SLEEP import *

class message_case(Login):
    def message(self):#按照一个测试用例来写
         #进入设计页面
         print('测试短信邮箱功能')
         sleep(sleep_mid)
         self.located(setting_loc).click()
         sleep(sleep_low)
         self.located(mes_set_loc).click()
         sleep(sleep_low)
         self.located(mes_conf_loc).click()
         sleep(sleep_low)
         self.located(mes_upload_loc).click()
         sleep(sleep_mid)
         self.located(excute_loc).clear()
         sleep(sleep_mid)
         self.located(excute_loc).send_keys('java -jar qcloudsms.jar  ${receiver} ${content}')
         sleep(sleep_mid)
         self.located(mes_prefix_loc).clear()
         sleep(sleep_mid)
         self.located(mes_prefix_loc).send_keys("workflow")
         sleep(sleep_low)
         self.located(mes_apl_loc).click()
         print ('test4测试完成')


