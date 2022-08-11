import json
import requests

def bugtool():
    """获取bug信息 如状态 优先级\等"""
    header = {
        "Accept":"*/*",
        "Connection":"keep-alive",
        "content-type":"application/json"
    }
    cookie = {"ajs_anonymous_id":"%2242584b4b-b04b-47ad-8fa2-8f04bfdc8ba2%22"," SL_G_WPT_TO":"zh-CN", "atlassian.xsrf.token":"725e5e66-f148-4f2e-a701-9a168378c0b7_c307e874e0d17f079f0fea875bd2cb28568a5466_lin","SL_GWPT_Show_Hide_tmp":"1", "SL_wptGlobTipTmp":"1", "JSESSIONID":"DA23FDE467ACA3769F88BD3E7768A8CC"," cloud.session.token":"eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Byb2QtMTU5Mjg1ODM5NCIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI2MjVlODFiZDk1MDZkNjAwNmZkOGJiNTgiLCJlbWFpbERvbWFpbiI6InJjdC5haSIsImltcGVyc29uYXRpb24iOltdLCJjcmVhdGVkIjoxNjU1NzgzODM4LCJyZWZyZXNoVGltZW91dCI6MTY2MDExNTY1OSwidmVyaWZpZWQiOnRydWUsImlzcyI6InNlc3Npb24tc2VydmljZSIsInNlc3Npb25JZCI6IjM3ZjA0Nzg1LWE5ZTgtNDQ3Mi05NTFmLWZmODczNjdjYTNiYSIsInN0ZXBVcHMiOltdLCJhdWQiOiJhdGxhc3NpYW4iLCJuYmYiOjE2NjAxMTUwNTksImV4cCI6MTY2MjcwNzA1OSwiaWF0IjoxNjYwMTE1MDU5LCJlbWFpbCI6InNpbWF5YW5neWFuZ0ByY3QuYWkiLCJqdGkiOiIzN2YwNDc4NS1hOWU4LTQ0NzItOTUxZi1mZjg3MzY3Y2EzYmEifQ.mieIaUdzRBV0AvZczHL8mXqNBP4o9Ahm3hqkfbtI0DyX-CJICPdQifSyQhBb5cZVZB4I0-ktWrdsyL8VK2M_lqUHECVqozFUrEdw9-wKM2KRb2NSZTMWmyHTBXq5C0dtJYuG6iphyYhRrAN_jpnyOZDpxE0yO7SkAtlne6CKtFfJ5MZ4TdsJ5MzNz7IIHS682sCFt568uWBZcTV2PbqrxD0FOipnN3on9ozZoxGzCJcQhgfhAXExCKNM_jnNoKrVjr0fbE86FCBPQYy1I48o8p6cylG72H3H8QaakSdLwgccO0PKfPAxPF6wZrWz7vldgsxhfTjqJN6SBNpY-IkW-w"}
    query = """query IssueListQuery($jql: String, $first: Int!, $last: Int, $filterId: Int, $amountOfIds: Int, $isMaxResultsLimitEnabled: Boolean!) {\n  issueIds: issues(first: $amountOfIds, jql: $jql, filterId: $filterId, isMaxResultsLimitEnabled: $isMaxResultsLimitEnabled) {\n    nodes {\n      issueId\n      __typename\n    }\n    __typename\n  }\n  issues(first: $first, last: $last, jql: $jql, filterId: $filterId, isMaxResultsLimitEnabled: $isMaxResultsLimitEnabled) {\n    nodes {\n      ...GetIssueDetails\n      __typename\n    }\n    ...GetTotalCountFragment\n    jql\n    __typename\n  }\n}\n\nfragment GetIssueDetails on Issue {\n  ...GetIdFragment\n  ...GetIssueIdFragment\n  ...GetIssueKeyFragment\n  ...GetAssigneeFragment\n  ...GetIssueTypeFragment\n  ...GetSummaryFragment\n  ...GetStatusFragment\n  ...GetReporterFragment\n  ...GetPriorityFragment\n  ...GetCreatedFragment\n  ...GetResolutionFragment\n  ...GetUpdatedFragment\n  ...GetDueDateFragment\n  __typename\n}\n\nfragment GetIdFragment on Issue {\n  __typename\n  id\n}\n\nfragment GetIssueIdFragment on Issue {\n  issueId\n  __typename\n}\n\nfragment GetIssueKeyFragment on Issue {\n  issuekey {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetAssigneeFragment on Issue {\n  assignee {\n    userValue {\n      accountId\n      avatarUrl\n      displayName\n      emailAddress\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GetIssueTypeFragment on Issue {\n  issuetype {\n    iconUrl\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment GetSummaryFragment on Issue {\n  summary {\n    textValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetStatusFragment on Issue {\n  status {\n    name\n    statusId\n    statusCategoryId\n    __typename\n  }\n  __typename\n}\n\nfragment GetReporterFragment on Issue {\n  reporter {\n    userValue {\n      accountId\n      avatarUrl\n      displayName\n      emailAddress\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GetPriorityFragment on Issue {\n  priority {\n    name\n    iconUrl\n    __typename\n  }\n  __typename\n}\n\nfragment GetCreatedFragment on Issue {\n  created {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetResolutionFragment on Issue {\n  resolution {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment GetUpdatedFragment on Issue {\n  updated {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetDueDateFragment on Issue {\n  duedate {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetTotalCountFragment on GQLIssueConnection {\n  totalCount\n  __typename\n}\n"""
    variables = {"first": 50, "last": 50, "jql": 'project = SOUL AND type = Bug ORDER BY created DESC', "amountOfIds": 1000, "isMaxResultsLimitEnabled": True}
    url = 'https://rct-ai.atlassian.net/rest/gira/1/?operation=IssueListQuery'
    resp = requests.post(url=url, json={"operationName":"IssueListQuery","query": query,"variables":variables}, headers=header, cookies=cookie)
    print(resp.json())
    i = 0
    all = len(resp.json()['data']['issueIds']['nodes'])
    upUnFix = []
    P0UnFix = []
    P1UnFix = []
    AllUnFix = []
    while i < len(resp.json()['data']['issueIds']['nodes']):
        priority = resp.json()['data']['issues']['nodes'][i]['priority']['name']
        status = resp.json()['data']['issues']['nodes'][i]['status']['name']
        name = [str(resp.json()['data']['issues']['nodes'][i]['summary']['textValue'])]
        if priority == '阻止程序' and status == '打开' or priority == '阻止程序' and status == 'In Dev':
            upUnFix += name
        if priority == 'P0-重要紧急' and status == '打开' or priority == 'P0-重要紧急' and status == 'In Dev':
            P0UnFix += name
        if priority == 'P1-重要不紧急' and status == '打开' or priority == 'P1-重要不紧急' and status == 'In Dev':
            P1UnFix += name
        if status == '打开' or status == 'In Dev':
            AllUnFix += name
        i += 1
    #print(upUnFix)
    #print(P0UnFix)
    #print(P1UnFix)
    #print(AllUnFix)
    #print(all)

    """修改格式推送至飞书"""
    upUnFixNum = len(upUnFix)
    P0UnFixNum = len(P0UnFix)
    P1UnFixNum = len(P1UnFix)
    AllUnFixNum = len(AllUnFix)
    p = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "tag": "div",
                "text": {
                        "content": f"**📒 Soularis-次世**",
                        "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"P0以上未修复BUG数 **{upUnFixNum}** 个",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"P0未修复BUG数 **{P0UnFixNum}** 个",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"P1未修复BUG数 **{P1UnFixNum}** 个",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"全部未修复BUG数 **{AllUnFixNum}** 个",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"BUG总数 **{all}** 个",
                    "tag": "lark_md"
                }
            }, {
                    "actions": [{
                            "tag": "button",
                            "text": {
                                    "content": "点击查看更多BUG详情🔍",
                                    "tag": "lark_md"
                            },
                            "url": "https://rct-ai.atlassian.net/jira/software/c/projects/SOUL/boards/57",
                            "type": "default",
                            "value": {}
                    }],
                    "tag": "action"
            }],
            "header": {
                    "title": {
                            "content": "🔔 今日BUG数量信息如下～",
                            "tag": "plain_text"
                    }
            }
        }
    }
    send = requests.post('https://open.feishu.cn/open-apis/bot/v2/hook/27fd941c-0e6e-47df-a2a0-17b91f7882a3',json.dumps(p))
    #print(send.status_code,send.json())
    return send

if __name__ == '__main__':
    bugtool()
