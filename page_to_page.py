#coding=UTF-8
from selenium.webdriver.support import expected_conditions as EC
from Page import Page
from selenium.webdriver.common.keys import Keys
from test_case.elements.element_loc import *
from time import sleep
from SLEEP import *

class Login(Page):
    url = ''
    username_loc=("xpath", ".//input[@id='username']")
    password_loc = ("xpath", ".//input[@name='password']")
    confirm_user_loc = ("xpath", ".//input[@name='submit']")


    def open(self):
        self._open(self.url)



    def login(self, username, password):
        sleep(sleep_low)
        user_input = self.slow_wait(EC.presence_of_element_located(self.username_loc))
        user_input.clear()
        user_input.send_keys(username)
        sleep(sleep_low)
        self.slow_wait(EC.presence_of_element_located(self.password_loc)).clear()
        self.slow_wait(EC.presence_of_element_located(self.password_loc)).send_keys(password)


    def login_start(self, username, password):
        sleep(sleep_low)
        self.open()
        sleep(sleep_low)
        self.login(username, password)

        try:
            sleep(sleep_low)
            self.located(self.confirm_user_loc).send_keys(Keys.ENTER)
            print("登录成功")
        except:
            print("登录失败")
            raise

    def located(self,loc):
        return self.slow_wait(EC.presence_of_element_located(loc))


    def swtich_to(self,page_loc):
        sleep(sleep_low)
        self.located(page_loc).click()
        print('进入设计页面')


    def new_workaera(self,name,desc):
        sleep(sleep_low)
        self.located(workarea_loc).click()
        self.located(name_workarea_loc).send_keys(name)
        sleep(sleep_low)
        self.located(desc_workarea_loc).send_keys(desc)
        sleep(sleep_low)
        self.located(confirm_workarea_loc).click()
        print('新建工作域：%s' %name)


    def new_workflow(self,name,desc):
        sleep(sleep_low)
        self.located(located_workarea_loc).click()
        sleep(sleep_low)
        self.located(workflow_loc).click()
        sleep(sleep_low)
        self.located(name_workflow_loc).send_keys(name)
        sleep(sleep_low)
        self.located(desc_workflow_loc).send_keys(desc)
        sleep(sleep_low)
        self.located(confirm_workflow_loc).click()
        print('新建工作流：%s' %name)
        sleep(sleep_low)


    #单个组件
    def shell_edit(self,name,desc,x=200,y=200):
        sleep(sleep_low)
        source_shell=self.located(shell_loc)
        self.drag_position(source_shell,x,y)#(x=200,y=200)
        sleep(sleep_low)
        self.located(name_shell_loc).send_keys(name)
        self.located(desc_shell_loc).send_keys(desc)
        sleep(sleep_low)
        self.located(shell_cont_loc).click()
        sleep(sleep_low)
        self.located(input_shellcont_loc).send_keys('sleep 5')
        self.located(shell_para_loc).click()
        sleep(sleep_low)
        self.located(input1_shellpara_loc).send_keys('shell1')
        sleep(sleep_low)
        self.located(input2_shellpara_loc).send_keys('shell1')
        sleep(sleep_low)
        self.located(add_shellvar_loc).click()
        sleep(sleep_low)
        self.located(confirm_shell_loc).click()

    def delay_edit(self,name,time):
        sleep(sleep_low)
        source_delay=self.located(delay_loc)
        self.drag_position(source_delay,400,50)
        sleep(sleep_low)
        self.located(name_delay_loc).send_keys(name)
        self.located(delay_time_loc).clear()
        self.located(delay_time_loc).send_keys(time)
        sleep(sleep_low)
        self.located(confirm_delay_loc).click()

    def trigger_edit(self):
        sleep(sleep_low)
        source_trigger=self.located(trigger_loc)
        self.drag_position(source_trigger,200,-200)
        self.located(name_trigger_loc).send_keys("trigger")
        sleep(sleep_low)
        self.located(select_task_loc).click()
        self.located(task_workdomain_loc).click()
        sleep(sleep_low)
        self.located(task_workarea_loc).click()
        sleep(sleep_low)
        self.located(task_workflow_loc).click()
        sleep(sleep_low)
        self.located(task_loc).click()
        sleep(sleep_low)
        self.located(confirm_trigger_loc).click()

    def sql_edit(self,name,desc):
        sleep(sleep_low)
        source_sql=self.located(sql_loc)
        self.drag_position(source_sql,200,400)
        sleep(sleep_low)
        self.located(name_sql_loc).send_keys(name)
        sleep(sleep_low)
        self.located(desc_sql_loc).send_keys(desc)
        sleep(sleep_low)
        self.located(sql_cont_loc).click()
        sleep(sleep_low)
        self.located(input_sqlcont_loc).send_keys('show databases')
        self.located(certif_loc).click()
        sleep(sleep_low)
        self.located(input_certif_loc).send_keys('xxxxx')
        sleep(sleep_low)
        self.located(confirm_sql_loc).click()


    def workflow_var(self):
        sleep(sleep_low)
        self.located(globalvar1_loc).send_keys('p2')
        self.located(globalvar2_loc).send_keys('p2')
        self.located(add_var_loc).click()


    def workflow_public_and_person(self):
        sleep(sleep_low)
        self.swtich_to(designpage_loc)
        sleep(sleep_low)
        self.located(located_workarea_loc).click()
        sleep(sleep_low)
        self.located(select_workflow_loc).click()
        sleep(sleep_low)
        self.located(publish_loc).click()
        sleep(sleep_low)
        self.located(confirm_publish_loc).click()
        sleep(sleep_low)
        print("已发布")
        self.located(select_workflow_loc).click()
        sleep(sleep_low)
        self.located(person_loc).click()
        self.located(confirm_person_loc).click()
        sleep(sleep_low)
        print('已下线')








