#coding=UTF-8
#!/usr/local/bin/ python
#完成登录操作
username_loc=('xpath',".//input[@id='username']")
passward_loc=('xpath',".//input[@name='password']")
confirm_loc=('xpath',".//input[@name='submit']")

#进入设计页面
designpage_loc=('xpath','/html/body/div/top-navbar/header/div[1]/section/nav/ul/li[2]/a/wf-icon')

#新建工作区
workarea_loc=('xpath','./html/body/div/div/div/ui-view/workspace-layout/section/side-menu/div/div[1]/div[2]/ul/li[@class="side-menu-item create"]')
name_workarea_loc=('xpath','//popover-create-workspace/form/div[1]/input')
desc_workarea_loc=('xpath','//popover-create-workspace/form/div[2]/textarea')
confirm_workarea_loc=('xpath','//popover-create-workspace/form/div[3]/button')
located_workarea_loc=('xpath','.//div[@title="test_selenium"]')

#新建工作流
workflow_loc=('xpath','.//*[@title="新建工作流"]/button')
name_workflow_loc=('xpath','.//input[@ng-model="$ctrl.workflow.name"]')
desc_workflow_loc=('xpath','.//textarea[@ng-model="$ctrl.workflow.desc"]')
confirm_workflow_loc=('xpath','//button[text()="保存"]')

#shell实例1
shell_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[1]/div[2]/design-task-prototype[2]/div/div[1]')
name_shell_loc=('xpath','.//div[@class="popover-task-split-content"]/popover-task-plugin-settings/div/div[1]/input')
desc_shell_loc=('xpath','.//div[@class="popover-task-split-content"]/popover-task-plugin-settings/div/div[2]/textarea')
shell_cont_loc=('xpath','.//div[@class="side-tab"]/h3[2]')
input_shellcont_loc=('xpath','.//textarea[@ng-model="task.shellCommand"]')
shell_para_loc=('xpath','.//div[@class="side-tab"]/h3[5]')
input1_shellpara_loc=('xpath','.//div[@class="popover-task-split-content"]/design-params/div/div[1]/input')
input2_shellpara_loc=('xpath','.//div[@class="popover-task-split-content"]/design-params/div/div[3]/input')
add_shellvar_loc=('xpath','//div[@class="popover-task-split-content"]/design-params/div/div[4]/button')
confirm_shell_loc=('xpath','.//div[@class="popover-task-foot"]/button')
shell_start_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[4]/*[name()="svg"]/*[name()="circle"]')
shell_end_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[3]/*[name()="svg"]/*[name()="circle"]')
shell_end_loc1=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[1]/*[name()="svg"]/*[name()="circle"]')

#trigger实例
trigger_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[1]/div[2]/design-task-prototype[5]/div/div[1]')
name_trigger_loc=('xpath','.//input[@ng-model="task.name"]')
#选择触发任务
select_task_loc=('xpath','.//div[@class="source-task-tree-dropdown-toggle wf-dropdown-toggle"]/wf-icon')
task_workdomain_loc=('xpath','//popover-task-trigger-tree/div/div[2]/div/div/span')
#task_workarea_loc=('xpath','//popover-task-trigger-tree/div/div[2]/div[1]/div[8]/div[1]')
#task_workarea_loc=('xpath','//div/span[@text()="test_selenium"]')
task_workarea_loc=('xpath','//div/span[text()="test_selenium"]')
#//*[@id="ngdialog7"]/div[2]/div/div[2]/popover-task-trigger/form/div[1]/div[3]/popover-task-trigger-tree/div/div[2]/div/div[8]/div/span
task_workflow_loc=('xpath','//div/span[text()="test1"]')
task_loc=('xpath','//div/span[text()="shell12"]')
confirm_trigger_loc=('xpath','.//div[@class="popover-task-foot"]/button')
#trigger_start_loc=('xpath',)
triggger_end_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[1]/*[name()="svg"]/*[name()="circle"]')

#SQl
sql_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[1]/div[2]/design-task-prototype[3]/div/div[1]')
name_sql_loc=('xpath','//div[@class="popover-task-split-content"]/popover-task-plugin-settings/div/div[1]/input')
desc_sql_loc=('xpath','//div[@class="popover-task-split-content"]/popover-task-plugin-settings/div/div[2]/textarea')
sql_cont_loc=('xpath','//div[@class="side-tab"]/h3[2]')
input_sqlcont_loc=('xpath','.//textarea[@ng-model="task.jdbcContent"]')
certif_loc=('xpath','//div[@class="side-tab"]/h3[3]')
input_certif_loc=('xpath','//div[@class="popover-task-split-content"]/div[1]/input')
#sql_para_loc=('xpath',)
#input_sqlpara1_loc=('xpath',)
#input_sqlpara2_loc=('xpath',)
confirm_sql_loc=('xpath','//div[@class="popover-task-foot"]/button')
sql_start_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[8]/*[name()="svg"]/*[name()="circle"]')
sql_start_loc1=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[4]/*[name()="svg"]/*[name()="circle"]')
#sql_end_loc=('xpath',)

#delay
delay_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[1]/div[2]/design-task-prototype[4]/div/div[1]')
name_delay_loc=('xpath','//div[@class="pop-content"]/popover-task-calendar/form/div[1]/div[1]/input')
delay_time_loc=('xpath','//div[@class="pop-content"]/popover-task-calendar/form/div[1]/div[3]/input')
confirm_delay_loc=('xpath','//div[@class="pop-content"]/popover-task-calendar/form/div[2]/button')
#delay_start_loc=('xpath',)
delay_end_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/wf-borderless-space/div/div[2]/div[5]/*[name()="svg"]/*[name()="circle"]')

#java
java_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[1]/div[2]/design-task-prototype[1]/div/div[1]')
name_java_loc=('xpath','//div[@class="popover-task-split-content"]/popover-task-plugin-settings/div/div[1]/input')
desc_java_loc=('xpath','//div[@class="popover-task-split-content"]/popover-task-plugin-settings/div/div[2]/textarea')
java_file_loc=('xpath','//div[@class="side-tab"]/h3[2]')
upload_file=('xpath','//button/div[text()="上传文件"]')
confirm_java_loc=('xpath','//div[@class="popover-task-foot"]/button')

#工作流的全局变量设置
globalvar1_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[2]/div[2]/div[2]/design-params/div/div[1]/input')
globalvar2_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[2]/div[2]/div[2]/design-params/div/div[3]/input')
add_var_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[2]/div[2]/div[2]/div[2]/design-params/div/div[4]/button')

#保存设计好的工作流
save_workflow_loc=('xpath','/html/body/div/div/div/ui-view/design-workflow/div/div[1]/div[2]/wf-btn[1]/button')
#工作流全选
select_workflow_loc=('xpath','/html/body/div/div/div/ui-view/workspace-layout/section/div/div/design-list/div/design-workflow-list/workflow-filter-table/div/wf-table/div/div[1]/div[1]/label/input')

publish_loc=('xpath','.//*[@title="发布工作流"]')
confirm_publish_loc=('xpath','//div[@class="btn-area"]/button[2]')
#发布状态监测
condition_loc=('xpath','/html/body/div/div/div/ui-view/workspace-layout/section/div/div/design-list/div/div/design-workflow-list/workflow-filter-table/div/wf-table/div/div[2]/div[1]/div[6]/wf-table-cell/deploy-type-col/strong')
condition2_loc=('xpath','/html/body/div/div/div/ui-view/workspace-layout/section/div/div/design-list/div/div/design-workflow-list/workflow-filter-table/div/wf-table/div/div[2]/div[2]/div[6]/wf-table-cell/deploy-type-col/strong')
#下线
person_loc=('xpath','//*[@title="下线工作流"]')
confirm_person_loc=('xpath','//div[@class="btn-area"]/button[2]')

#选线
select_lines_loc=('xpath','//div[@class="wf-borderless-space-main position-absolute"]/*[name()="svg"]')
yes_line_loc=('xpath','//label/div[text()="是依赖"]')
no_lines_loc=('xpath','/html/body/div[2]/ul/li[2]/label/div[1]')
or_lines_loc=('xpath','/html/body/div[2]/ul/li[4]/label/div[1]')
weak_lines_loc=('xpath','/html/body/div[2]/ul/li[3]/label/div[1]')
fasle_lines_loc=('xpath','/html/body/div[2]/ul/li[5]/label/div[1]')
skip_lines_loc=('xpath','/html/body/div[2]/ul/li[6]/label/div[1]')
delete_lines_loc=('xpath','//*[@title="删除"]')


#短信
setting_loc=('xpath','/html/body/div/top-navbar/header/div[2]/aside/div[1]/ul/li[4]/a/wf-icon/*[name()="svg"]')

mes_set_loc=('xpath','//a[text()="邮箱/短信配置"]')
mes_conf_loc=('xpath','//span[text()="短信配置"]')
mes_upload_loc=('xpath','//div[text()="上传"]')
#excute_loc=('xpath','/html/body/div/div/div/config.xml-layout/section/div/notification-config.xml/div/div/sms-config.xml/div/form/div[2]/textarea')2.18
excute_loc=('xpath', '//form[@name="smsConfigForm"]/div[2]/textarea')#2.19
mes_prefix_loc=('xpath','//form[@name="smsConfigForm"]/div[3]/input')
mes_apl_loc=('xpath','//form[@name="smsConfigForm"]/div[4]/wf-btn[2]/button/div')
