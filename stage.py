#coding=UTF-8
import traceback
from time import sleep
from test_case.pages.page_to_page import Login
from SLEEP import *
from test_case.pages.java_case import java_case
from test_case.pages.switch_lines import switch_line_case
from test_case.pages.design_workflow import design_workflow_case
from test_case.pages.message import message_case
from test_case.module.funcation import image_path,screenshot_save

class Stage:
    def __init__(self,driver,url,lg_usr,lg_pas):
        self.driver=driver
        self.url=url
        self.lg_usr=lg_usr
        self.lg_pas=lg_pas

    def stage1(self,result_path):
        print("stage1  design_workflow")
        log_file=result_path+'/stage1.log'
        file=open(log_file,'w')
        file.writelines("[stage]:1------design_workflow-----\n")
        file.writelines("[result_path]: %s \n" % result_path)

        try:
            lo=Login(self.driver,self.url)
            lo.login_start(self.lg_usr,self.lg_pas)
            sleep(sleep_low)
            workflow = design_workflow_case(lo.driver, lo.url)
            workflow.design_workflow()
            self.driver.quit() #判断条件
            file.writelines("[result]:success\n")

        except BaseException as e:
            image_dir = image_path(result_path, 'error_stage1')
            screenshot_save(self.driver,image_dir,'error_behavior.png')
            file.writelines("[result]:fail\n")
            file.writelines("[traceback]: ")
            file.close()
            traceback.print_exc(file=open(log_file,'a+'))


    def stage2(self,result_path):
        print("stage2  java_case")
        log_file = result_path + '/stage2.log'
        file = open(log_file, 'w')
        file.writelines("[stage]:2------java_case-------\n")
        file.writelines("[result_path]: %s \n" % result_path)

        try:
            lo = Login(self.driver, self.url)
            lo.login_start(self.lg_usr, self.lg_pas)
            sleep(sleep_low)
            java = java_case(lo.driver, lo.url)
            java.java()
            file.writelines("[result]:success\n")
        except BaseException as e:
            image_dir = image_path(result_path, 'error_stage2')
            screenshot_save(self.driver, image_dir, 'error_behavior.png')
            file.writelines("[result]:fail\n")
            file.writelines("[traceback]:" )
            file.close()
            traceback.print_exc(file=open(log_file, 'a+'))


    def stage3(self,result_path):
        print("stage3  switch_lines")
        log_file = result_path + '/stage3.log'
        file = open(log_file, 'w')
        file.writelines("[stage]:3------switch_lines-------\n")
        file.writelines("[result_path]: %s \n" % result_path)

        try:
            lo = Login(self.driver, self.url)
            lo.login_start(self.lg_usr, self.lg_pas)
            sleep(sleep_low)
            lines = switch_line_case(lo.driver, lo.url)
            lines.switch_line()
            file.writelines("[result]:success\n")

        except BaseException as e:
            image_dir = image_path(result_path, 'error_stage3')
            screenshot_save(self.driver, image_dir, 'error_behavior.png')
            file.writelines("[result]:fail\n")
            file.writelines("[traceback]:")
            file.close()
            traceback.print_exc(file=open(log_file, 'a+'))

    def stage4(self, result_path):
        print("stage4  message")
        log_file = result_path + '/stage4.log'
        file = open(log_file, 'w')
        file.writelines("[stage]:4------message-------\n")
        file.writelines("[result_path]: %s \n" % result_path)

        try:
            lo = Login(self.driver, self.url)
            lo.login_start(self.lg_usr, self.lg_pas)
            sleep(sleep_low)
            mes = message_case(lo.driver, lo.url)
            mes.message()
            file.writelines("[result]:success\n")

        except BaseException as e:
            image_dir = image_path(result_path, 'error_stage4')
            screenshot_save(self.driver, image_dir, 'error_behavior.png')
            file.writelines("[result]:fail\n")
            file.writelines("[traceback]:")
            file.close()
            traceback.print_exc(file=open(log_file, 'a+'))



