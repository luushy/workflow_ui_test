#coding=UTF-8
#!/usr/local/bin/ python
from page_to_page import  Login
from time import sleep
from test_case.elements.element_loc import *
from SLEEP import *

class design_workflow_case(Login):
    def design_workflow(self):#按照一个测试用例来写
         #进入设计页面
        sleep(sleep_mid)
        self.swtich_to(designpage_loc)
        #新建工作区
        sleep(sleep_low)
        self.new_workaera("test_selenium","selenium test")
        #test1工作流
        sleep(sleep_low)
        self.new_workflow('test1','shell')
        sleep(sleep_low)
        self.shell_edit('shell12','shell12')
        sleep(sleep_low)
        self.located(save_workflow_loc).click()
        print('工作流设计完成')
        #进入设计页面
        sleep(sleep_mid)
        self.swtich_to(designpage_loc)
        #test2工作流f
        #trigger
        sleep(sleep_low)
        self.new_workflow('test2','trigger_shell')
        sleep(sleep_low)
        self.trigger_edit()
        #shell
        sleep(sleep_low)
        self.shell_edit('shell90','shell90')
        #delay
        sleep(sleep_low)
        self.delay_edit('delay','2')
        #sql
        sleep(sleep_low)
        self.sql_edit('sql2','sql2')
        #连接trigger和shell
        sleep(sleep_low)
        source_trigger_end=self.located(triggger_end_loc)
        source_shell_start=self.located(shell_start_loc)
        sleep(sleep_low)
        self.drag(source_trigger_end,source_shell_start)
        #连接shell和sql
        sleep(sleep_low)
        source_shell_end=self.located(shell_end_loc)
        source_sql_start=self.located(sql_start_loc)
        sleep(sleep_low)
        self.drag(source_shell_end,source_sql_start)
        #连接delay和sql
        source_delay_end=self.located(delay_end_loc)
        sleep(sleep_low)
        self.drag(source_delay_end,source_sql_start)
        #工作流全局变量
        self.workflow_var()
        #保存工作流
        sleep(sleep_low)
        self.located(save_workflow_loc).click()
        print('工作流设计完成')
        #工作流发布与上线
        print('工作流发布状态：')
        self.workflow_public_and_person()



