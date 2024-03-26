import pytest
import requests
import globalvalue
from yamltest import YamlUtil
from common import logger


class TestLogin:

    @pytest.mark.parametrize('args', YamlUtil('C:\\learning\\python\\code\\login.yaml').yaml_read())
    def testlogin(self, args):
        # print(args)

        url = args.get('request').get('url')
        logger.info(url)
        headers = args.get('request').get('headers')

        data = args.get('request').get('params')
        rep = requests.post(url, headers=headers, data=data, verify=False)
        assert rep.status_code == args.get('request').get('ast')
        rep_json = rep.json()
        if rep.status_code == 200:
            globalvalue.global_access_token = rep_json['access_token']
            # print(rep_json['access_token'])
            logger.info(f"登录返回的access_token是：{rep_json['access_token']}")
        # global gl.
        # global_access_token = rep_json['access_token']
        # print(rep_json['access_token'])
        # print(global_access_token)

    # def createvolume():
    #     url = "https://172.16.100.209:8443/v1/volumes/task/create?ignoreErrorAlert=true"
    #
    #     data = {
    #         'blockSize': '4096',
    #         'clusterId': 'ee12cfa6-32f7-4617-b9cd-8b4bcef3f64f',
    #         'compressionAlgorithm': 'LZ4',
    #         'enableDedup': 'true',
    #         'volumeName': 'auto02',
    #         'volumeSize': '10737418240'
    #
    #     }
    #
    #     headers = {
    #         'authorization': 'Bearer JocBsNfUYnJUST/UBfew1sjEmoY=',
    #         'Content-Type': 'application/json'
    #     }
    #
    #     rep = requests.post(url, headers=headers, json=data, verify=False)
    #
    #     print(rep.status_code)
    #     print(rep.url)
    #     print(rep.text)

# if __name__ == '__main__':
#     login()
#     getSp()
# createvolume()
# pytest.main(['-sv', "--html=report.html", "--alluredir=allure"])
