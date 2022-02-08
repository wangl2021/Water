# -*- coding: utf-8 -*-
from jira import JIRA


def infos_jira(jira_id):
    jira_option = {
        'server': 'https://jira.zz.com/',
        'verify': False
    }
    jira_info = JIRA(options=jira_option, basic_auth=('', ''))
    issue = jira_info.issue(jira_id)
    res = {
        'jira_id': issue.key,  # jira
        'back_developer': issue.fields.customfield_10201,  # 责任人
        'tester': issue.fields.customfield_10203,  # 测试
        'producter': issue.fields.customfield_10202,  # 产品
        'summary': issue.fields.summary,  # 概要
        'developer_startTime': issue.fields.customfield_10300,  # 开发开始时间
        'developer_endTime': issue.fields.customfield_10302,  # 开发结束时间
        'tester_startTime': issue.fields.customfield_10301,  # 测试开始时间
        'tester_endTime': issue.fields.customfield_10305,  # 测试结束时间
        'tester_online': issue.fields.customfield_10304,  # 上线时间
        'project' : issue.fields.project.name,  # 项目名称
        'status': issue.fields.status,  # 状态
    }
    # print(issue.raw) #查所有
    return res


# print(infos_jira('ZQQS-1110')['status'])
