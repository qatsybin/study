import requests

# 接口测试 
def test_zsgc():
    # get token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwaf66eaa60b74536f&corpsecret=K4QMvCs00L4J1HBKYfXakPsCqHOALt1B7lIIw3CFu1Q"
    r = requests.get(url)
    token = r.json()['access_token']
    # read members
    url_r = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=XuBin"
    r1 = requests.get(url_r)
    print(r1.json())
    # add members
    url_add = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "张三",
        "alias": "jackzhang",
        "mobile": "+86 13800000000",
        "department": [1]
    }
    r2 = requests.post(url_add, json=body)
    result_add = r2.json()['errmsg']
    assert result_add == 'created'
    # update members
    url_up = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "李四",
        "mobile": "+86 13800000001",
        "department": [2],
    }
    r3 = requests.post(url_up, json=body)
    result_up = r3.json()['errmsg']
    assert result_up == 'updated'
    # delete_members
    url_del = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan"
    r4 = requests.get(url_del)
    result_del = r4.json()['errmsg']
    assert result_del == 'deleted'
