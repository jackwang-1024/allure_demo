import requests
import pytest
import globalvalue
from common import logger

class TestGetSp:

    def testgetSp(self):
        url = "https://172.16.100.232:8443/v1/clusters"

        headers = {
            'authorization': 'Bearer ' + globalvalue.global_access_token
        }

        # print("==testgetsp22222=====")
        logger.info("==testgetsp22222=====")
        # print("[global_access_token:]" + globalvalue.global_access_token + "[global_access_token]")
        # accesstoken = globalvalue.global_access_token
        logger.info(f"[global_access_token:]{globalvalue.global_access_token}[global_access_token]")
        rep = requests.get(url, headers=headers, verify=False)
        # print(rep.status_code)
        logger.info(rep.status_code)
        # print(url)
        logger.info(url)
        rep_json = rep.json()
        # print(rep_json)
        # print(rep.status_code)
        assert rep.status_code == 200
        # print(rep.text)
        # print(rep_json['data'][0]['clusterName'])
        logger.info(f"clusterName：{rep_json['data'][0]['clusterName']}")
        if rep.status_code == 200:
            globalvalue.global_clusterid = rep_json['data'][0]['clusterId']
            # print(globalvalue.global_clusterid)
            logger.info(f"clusterid{rep_json['data'][0]['clusterId']}")