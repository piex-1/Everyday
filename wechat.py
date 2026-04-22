import argparse
import os
import random
import shutil

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


def _parse_bool(v: str) -> bool:
    s = (v or "").strip().lower()
    if s in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if s in {"0", "false", "f", "no", "n", "off", ""}:
        return False
    raise ValueError(f"invalid bool value: {v}")


def _sync_kamept_snapshot(page_path: str = "page.txt", snapshot_path: str = "source/kamept.txt"):
    if not os.path.exists(page_path):
        return
    os.makedirs(os.path.dirname(snapshot_path) or ".", exist_ok=True)
    shutil.copyfile(page_path, snapshot_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--kamept",
        default="false",
        help="bool: true/false/1/0; true 表示文件有变化继续执行，false 表示无变化直接跳过",
    )
    args = parser.parse_args()

    kamept = _parse_bool(args.kamept)
    if not kamept:
        print("changed=false")

    print("changed=true")

    client = WeChatClient(app_id, app_secret)
    wm = WeChatMessage(client)

    for i in range(len(user_ids)):
        # cit, dat = get_city_date(citys[i])
        dat = str(kamept)
        data = {
            "date": {"value": "今日kamept网址 ：{}".format(dat), "color": get_random_color()},
        }
        res = wm.send_template(user_ids[i], template_ids[i], data)
        print(res)

    _sync_kamept_snapshot("page.txt", "source/kamept.txt")


if __name__ == "__main__":
    main()