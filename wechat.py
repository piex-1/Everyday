import os
import math
import random
import requests

from datetime import date, datetime
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate

today = datetime.now()

# 微信公众测试号ID和SECRET
# app_id = os.environ["APP_ID"]
# app_secret = os.environ["APP_SECRET"]
app_id = "wx51bf806759421418"
app_secret = "4e1c7aeea2d958be40e9e40d12839aea"

user_ids = "oDtDl2yhXPRqifvRYnaHDsHHBZ84".split(",")
template_ids = "sKV0YjtSl3uqpBTUiJJPNCfRHWr4f0sHfFf5GWKSszU".split(",")
citys = "北京".split(",")
solarys = "10".split(",")
start_dates = "2020-01-01".split(",")
birthdays = "01-01".split(",")

# 当前城市、日期
def get_city_date(city):
    return city, today.date().strftime("%Y-%m-%d")

# 字体随机颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)

for i in range(len(user_ids)):
    cit, dat = get_city_date(citys[i])
    data = {
        "date": {"value": "今日日期：{}".format(dat), "color": get_random_color()},
    }

    res = wm.send_template(user_ids[i], template_ids[i], data)
    print(res)