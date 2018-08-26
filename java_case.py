#coding=UTF-8
#!/usr/local/bin/ python
from page_to_page import Login
from time import sleep
from test_case.elements.element_loc import *
from SLEEP import *


class java_case(Login):
    def java(self):
        sleep(sleep_mid)
        self.swtich_to(designpage_loc)
        #新建工作区
        try:
           sleep(sleep_low)
           self.located(located_workarea_loc).click()

        except:
            sleep(sleep_low)
            self.new_workaera("test_selenium","selenium test")

        sleep(sleep_low)
        self.new_workflow('test2','java')
        sleep(sleep_low)
        print('开始设计')
        source_java=self.located(java_loc)
        sleep(sleep_low)
        self.drag_position(source_java,200,200)
        sleep(sleep_low)
        self.located(name_java_loc).send_keys("java")
        sleep(sleep_low)
        self.located(desc_java_loc).send_keys("java")
        sleep(sleep_low)
        self.located(java_file_loc).click()
        sleep(sleep_mid)
        self.located(upload_file).click()
        #关闭弹出的系统对话框
        # dialog_box = self.driver.switch_to_alert()
        # dialog_box.dismiss()
        print("上传文件成功")
        sleep(sleep_low)
        self.located(confirm_java_loc).click()
        sleep(sleep_mid)
        self.located(save_workflow_loc).click()
        sleep(sleep_mid)
        print('test2完成')

