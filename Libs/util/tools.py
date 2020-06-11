import hashlib
import random
import urllib
import jsonpath
import json
import base64
import urllib3
import requests
import time
import uuid
import pymysql.cursors
from random import choice


# class Tool():
def getdatalistfromfile(path):
    data = []
    dataformat = {}  # 数据的格式：csv中第一行为列名
    with open(path, "r") as file:
        filedata = file.readlines()
        col = filedata[0].rstrip("\n").split(",")
        for i in range(0, len(col)):
            dataformat[col[i]] = i

        for line in filedata[1:]:
            data.append(line.strip())
    return data, dataformat


def randomdata(data, dataformat):
    # 随机选取一条数据，返回字典，key为csv中第一行所显示的列名
    result = {}
    temp = choice(data).split(",")
    for k, v in dataformat.items():
        result[k] = temp[v]
    return result


def encrypt(data, secret):
    # 把data按照key排序后进行加密
    # orderdata = dict(sorted(data.items(), key=lambda obj: obj[0]))
    # str_data = json.dumps(orderdata, ensure_ascii=False).replace(" ", "")
    # sign_str = urllib.parse.urlencode(orderdata)
    sign_list = [f'{secret[0]}={secret[1]}']
    # for k,v in orderdata.items():
    for k in sorted(data):
        sign_list.append(f'{k}={data[k]}')

    sign_str = "&".join(sign_list)

    # sign_str = str_data + key
    print(f"====md5前====\n{sign_str}", )
    md5 = hashlib.md5()
    md5.update(sign_str.encode(encoding="utf-8"))
    sign = md5.hexdigest()
    print(f"====md5后====\n{sign}", )
    return sign


def get_value_from_json(json_str, node_path):
    value = None
    try:
        json_str = json.loads(json_str)
        object = jsonpath.jsonpath(json_str, node_path)
        if object:
            value = object
    except Exception as e:
        print(e)
    return value


def get_uuid():
    return str(uuid.uuid1()).replace("-", "")[0:19]


def get_intid():
    return random.randrange(100000000, 900000000, 1)


# def get_message(phone):
#     result = ""
#     data = {"limit": 1, "offset": 0, "search": phone, "_": int(time.time())}
#     url = "http://10.1.1.143:20032/message/paginate"
#     response = requests.request(method="GET", url=url, params=data)
#     response_text = json.loads(response.text)
#     result = response_text.get("rows")[0].get("content", None)
#     return result

def select_sql(config, sql):
    try:
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        return e


def update_sql(config, sql):
    connection = pymysql.connect(**config)
    cursor = connection.cursor()
    try:

        for i in sql:
            cursor.execute(i)
        connection.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    d1 = {'a': 3, "c": '中文', "b": 2, }
    secret = ("GAMEAUTHKEY", "LTGameAuthKey")
    sign = encrypt(d1, secret)
    print(sign)
