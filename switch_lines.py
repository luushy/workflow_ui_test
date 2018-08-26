#coding=UTF-8
#!/usr/local/bin/ python
from page_to_page import Login
from time import sleep
from test_case.elements.element_loc import *
from SLEEP import *
class switch_line_case(Login):
    def switch_line(self):
        sleep(sleep_hig)
        self.swtich_to(designpage_loc)
        #新建工作区
        try:
           sleep(sleep_low)
           self.located(located_workarea_loc).click()

        except:
            sleep(sleep_low)
            self.new_workaera("test_selenium","selenium test")

        sleep(sleep_low)
        self.new_workflow('test4','lines')
        sleep(sleep_mid)
        print('开始设计')
        self.shell_edit('shel34','shell34')
        sleep(sleep_low)
        self.sql_edit('sql78','sql78')
        sleep(sleep_low)
        source_sql_start=self.located(sql_start_loc1)
        source_shell_end=self.located(shell_end_loc1)
        sleep(sleep_low)
        self.drag(source_shell_end,source_sql_start)
        sleep(sleep_mid)
        self.located(select_lines_loc).click()
        #sleep(2)
        #self.located(yes_line_loc).click()
        sleep(sleep_low)
        self.located(no_lines_loc).click()
        sleep(sleep_mid)
        self.located(or_lines_loc).click()
        sleep(sleep_mid)
        self.located(weak_lines_loc).click()
        sleep(sleep_mid)
        self.located(fasle_lines_loc).click()
        sleep(sleep_mid)
        self.located(skip_lines_loc).click()
        sleep(sleep_mid)
        self.located(delete_lines_loc).click()
        sleep(sleep_hig)
        self.located(save_workflow_loc).click()
        sleep(sleep_low)
        print('test3 测试完成')


