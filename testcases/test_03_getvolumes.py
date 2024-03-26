from common import logger
import requests
import pytest
import globalvalue

class TestGetVolumes:

    def testgetvolumes(self):

        cluterid = globalvalue.global_clusterid
        print("[global_clusterid:]"+cluterid+ "[global_clusterid]")

        url = "https://172.16.100.232:8443/v1/volumes/" + cluterid

        headers = {
            'authorization': 'Bearer ' + globalvalue.global_access_token
        }


        # print("==testgetvolumes=====")
        # print("[global_access_token:]" + globalvalue.global_access_token + "[global_access_token]")
        logger.info("==testgetvolumes=====")
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
        # print(rep_json['data'][0]['volumeName'])
        # print(rep_json['data'][1]['volumeName'])
        # print(rep_json['data'][2]['volumeName'])
        logger.info(rep_json['data'][0]['volumeName'])
        logger.info(rep_json['data'][1]['volumeName'])
        logger.info(rep_json['data'][2]['volumeName'])