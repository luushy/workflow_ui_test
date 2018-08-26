#coding=UTF-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui  import Select
from time import sleep



class Page:
    def __init__(self,driver,base_url):
        self.driver=driver
        self.base_url=base_url

    #执行func，等待10s
    def wait(self,func):
        return WebDriverWait(self.driver,10).until(func)

    def slow_wait(self,func):
        return WebDriverWait(self.driver,30).until(func)

    #打开url
    def _open(self,url):
        if self.url[:4]=='http':
            self.driver.get(self.url)

        else:
            self.driver.get(self.base_url+url)

    #鼠标拖拽某一元素到指定位置
    def drag_position(self,source,x,y):
        return ActionChains(self.driver).drag_and_drop_by_offset(source,x,y).perform()

    #鼠标从起点拖拽到终点
    def drag(self,start,end):
        return ActionChains(self.driver).drag_and_drop(start,end).perform()

    #select下拉菜单中通过value选元素
    def select_by_value(self,source,value):
        return Select(source).select_by_value('%s'%value)

    #svg标签中的元素点击
    def svg_click(self,source):
        ActionChains(self.driver).click(source).perform()

    def mouse_move_to(self,source,xoffset,yoffset):
        ActionChains(self.driver).move_to_element_with_offset(source,xoffset,yoffset).perform()

    def select_by_text(self,top,text):
        s1=Select(top)
        s1.select_by_visible_text(text)

    def click_element(self,element):
        ActionChains(self.driver).click(element)

    def select_scroll_item(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(3)
        element.click()
