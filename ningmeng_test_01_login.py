import os
import loguru
import pytest
import requests
import allure

# 日志持久化 -- 保存在日志文件
loguru.logger.add(sink="mylog.log")

# 第一步：获取接口文档 分析需求, 准备测试数据【接口测试需要五大要素】
# 测试数据保存在 列表 嵌套字典的数据类型。-- 每一条用例存在字典里；三条用例一起存在列表里，数据读取方便
case_all = [
{'case_id': 1,
'header': {"X-Lemonban-Media-Type":"lemonban.v2"},
'url': 'http://api.lemonban.com/futureloan/member/login',
'data': {"mobile_phone": "13811112005",	"pwd": "lemon666"},
'expected': {"code": 0,"msg": "OK"}
 },
{'case_id': 2,
'header': {"X-Lemonban-Media-Type":"lemonban.v2"},
'url': 'http://api.lemonban.com/futureloan/member/login',
'data': {"mobile_phone": "13811112005",	"pwd": "lemon12345"},
'expected': {"code": 1,"msg": "账号信息错误"}
 },
{'case_id': 3,
'header': {"X-Lemonban-Media-Type":"lemonban.v2"},
'url': 'http://api.lemonban.com/futureloan/member/login',
'data': {"mobile_phone": "13811112005",	"pwd": ""},
'expected': {"code": 1,"msg": "密码为空"}
 }
]

# 第二步：发送接口请求-工具+代码，得到响应结果  -- 数据读取，列表读取数据【索引】 字典读取数据【键值对】
# Python代码基础 +  接口测试基础  补课学习
# 接口地址
url = case_all[0]["url"]
# 接口请求头部
header = case_all[0]["header"]
# 接口请求参数
data = case_all[0]["data"]
# 发送接口请求 得到响应结果
response = requests.request("post",url,headers=header,json=data)
# 查看响应结果信息
print(response.json())
# 代码断言
assert response.json()["msg"] == case_all[0]["expected"]["msg"]

# 第三步：执行每一条用例 - pytest测试框架 | unittest 【老的】
# 测试数据不一样，然后执行的方法一样的 测试结果不一样的 == 框架设计思想，DDT 数据驱动思想，简化代码
# 装饰器： 依次取到测试数据【一条一条取数据】，依次传给下面的方法使用
@pytest.mark.parametrize("case",case_all)
def test_login(case): # case存储数据是什么类型？--字典存的每一条测试用例
    # 接口地址
    url = case["url"]
    loguru.logger.info(f"url地址是{url}")
    # 接口请求头部
    header = case["header"]
    loguru.logger.info(f"header{header}")
    # 接口请求参数
    data = case["data"]
    loguru.logger.info(f"请求参数是{data}")
    expected = case["expected"]
    loguru.logger.info(f"期望结果是{expected}")
    # 发送接口请求 得到响应结果
    response = requests.request("post", url, headers=header, json=data)
    loguru.logger.info(f"响应消息是{response.json()}")
    # 代码断言
    try:  # 异常捕获
        assert response.json()["msg"] == expected["msg"]
        loguru.logger.info("断言成功")
    except AssertionError as e:
        loguru.logger.error("断言失败")
        raise e

# 以后跟公司用例 1000+ 用例，所有测试结果 不能在pycharm 里结果去看； 页面报告里-- html
# 自动发现所有测试用例  不用是活动收集  --命名规则
# 生成测试报告的 json文件不是给人看  给allure 看的
# 想要生成html页面 给人看的报告
pytest.main(["-v","-s","--clean-alluredir","--alluredir=allure-results"])
os.system(r"allure generate -c -o 项目测试报告")









