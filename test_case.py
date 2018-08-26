#coding=UTF-8
#!/usr/local/bin/ python
#from UI_test.test_case.pages.page_to_page import Login
#from UI_test.test_case.pages.java_case import java_case
#from UI_test.test_case.pages.switch_lines import switch_line_case
#from UI_test.test_case.pages.design_workflow import design_workflow_case
#from UI_test.test_case.pages.message import message_case
import argparse
from test_case.module.read_yaml import Player_yaml as PY
from test_case.module.driver import browser
from stage import Stage

if __name__ == "__main__":
    parser = argparse.ArgumentParser() #定义：argparse是python标准库里面用来处理命令行参数的库
    parser.add_argument("-y", help="input player yaml address", type=str)#-y为命令行的参数
    args = parser.parse_args()
    print(args)

    yaml_path = args.y
    print(yaml_path)
    py = PY(yaml_path)
    py.load_yaml()

    driver = browser(py.browser_ip)
    #driver=webdriver.Chrome()
    #driver = browser(address)
    driver.maximize_window()
    driver.get(py.workflow_url)


    #登录pl
    stage = Stage(driver, py.workflow_url, py.login_name, py.login_pas)


    if py.stage_num == 1:
        stage.stage1(py.result_path)

    if py.stage_num == 2:
        stage.stage2(py.result_path)

    if py.stage_num == 3:
        stage.stage3(py.result_path)

    if py.stage_num == 4:
        stage.stage4(py.result_path)

    driver.quit()





