#coding=UTF-8
#!/usr/local/bin/ python
import yaml # 一种非标记语言，一般用来写配置文件

class Player_yaml:
    def __init__(self,path):
        self.path=path
        self.stage_num=0
        self.browser_ip=''
        self.workflow_url=''
        self.login_name=''
        self.login_pas=''
        self.result_path=''


    def load_yaml(self):
        file=open(self.path)
        dic=yaml.load(file)
        print(dic)
        self.stage_num = dic['selenium_params']['stageNum']
        print("stage_num: %s" % self.stage_num)
        self.result_path = dic['selenium_params']['resultFileName']
        print("result_path: %s" % self.result_path)
        self.browser_ip=dic['selenium_params']['workflow.selenium.server.address']
        print("browser  %s"%self.browser_ip)
        self.workflow_url=dic['selenium_params']['workflow.server.url']
        print("workflow_url  %s" % self.workflow_url)
        self.login_name=dic['selenium_params']['workflow.login.name']
        print("workflow username %s" % self.login_name)
        self.login_pas=dic['selenium_params']['workflow.login.password']
        print("worklfow password %s" % self.login_pas)















#yml=Player_yaml('/home/yushuangchun/TDC/pilot_smoke_test/case_jdbc_bunch.yml')
#yml.load_yaml()
