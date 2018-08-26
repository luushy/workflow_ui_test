#coding=UTF-8
import time
import os
import shutil
from selenium import webdriver

def image_path(result_path,stage):
    ipath=result_path+'/image_'+stage
    if os.path.exists(ipath):
        print("删除目录 %s "% ipath)
        shutil.rmtree(ipath)
    print("创建image目录：%s"%ipath)
    os.mkdir(ipath)
    return ipath

def upload_image(ipath,log_file):
    print("upload images")
    shell_command=os.getcwd().split('/smoke_test')[0]+'/smoke_test/upload_image/upload_image.sh '+ipath+'>>'+log_file
    print shell_command
    os.system(shell_command)

def screenshot_save(driver,ipath,iname):
    save_path=ipath+'/'+iname
    driver.get_screenshot_as_file(save_path)
