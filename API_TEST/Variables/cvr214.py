from Libs.util.tools import *

domain_test = 'http://192.168.1.171:8888'
MAC = 'AV:CA:83:48:29'
businessFlowNumber = get_uuid()

Valid_biClientLoginout_header = {'Content-Type': 'application/json'}
Valid_biClientLoginout_body = {
    "userId": "",
    "loginStatus": 0,
    "clientBrand": "华为",
    "clientModel": "华为mate30",
    "clientImei": "123131",
    "androidVersion": "10.2.3",
    "mac": MAC,
    "clientCpu": "8",
    "clientMemory": "16",
    "storage": "64",
    "networkType": 1,
    "operators": "中国移动",
    "localIp": "192.168.1.202",
    "extranetIp": "116.46.56.202",
    "appId": "123456",
    "appPackage": "letinvr.gd.yuexiangwug",
    "appVersion": "5.3.2",
    "operation": 1,
    "businessFlowNumber": businessFlowNumber
}

Valid_biHeartclientUserHeart_header = {'Content-Type': 'application/json'}
Valid_biHeartclientUserHeart_body = {
    "mac": MAC,
    "biTimeInterval": 3,
    "businessFlowNumber": businessFlowNumber
}

Valid_biClientLoginout_logout_body = {
    "userId": "",
    "loginStatus": 0,
    "clientBrand": "华为",
    "clientModel": "华为mate30",
    "clientImei": "123131",
    "androidVersion": "10.2.3",
    "mac": MAC,
    "clientCpu": "8",
    "clientMemory": "16",
    "storage": "64",
    "networkType": 1,
    "operators": "中国移动",
    "localIp": "192.168.1.202",
    "extranetIp": "116.46.56.202",
    "appId": "123456",
    "appPackage": "letinvr.gd.yuexiangwug",
    "appVersion": "5.3.2",
    "operation": 2,
    "businessFlowNumber": businessFlowNumber
}
