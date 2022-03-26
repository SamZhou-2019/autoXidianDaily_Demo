##  设置
import json
import os
import random

PATH = os.path.dirname(__file__)

##  填写设置(True为填写)

DailyUp = True  # 晨午晚检
DailyReport = False  # 疫情通

## 脚本管理员（日志将发送到这位的邮箱）

Admin = 'whx'   # 名称请与email_confirm中的保持一致

############################## 下列各项的参数请在配置文件中设置  ###############################

## 邮箱验证

# 配置文件：email_confirm.json

email_confirm = json.load(open(os.path.join(PATH, 'config/email_confirm.json'), 'r'))


##  一站式学生认证

# 配置文件：identity_confirm.json
identity_confirm = json.load(open(os.path.join(PATH, 'config/identity_confirm.json'), 'r'))


################################ 下列各项的参数由脚本自动生成  ###############################

##  定位

geo_api_info = random.choice(json.load(open(os.path.join(PATH,'config/geo_pool.json'), 'r')))     # 从'geo_pool.json'文件中随机选取一项作为定位


# 具体地点

location_dict = json.loads(geo_api_info)    # geo_api_info专成的字典

province = location_dict['addressComponent'].get('province')    # 所在省

city = location_dict['addressComponent'].get('city')    # 所在市

area = location_dict['addressComponent'].get('district')    # 所在区

address = location_dict.get('formattedAddress')    # 详细地址


if DailyUp:
    # 晨午晚检上报信息
    cwwj_data={
        "ymtys": "0",  # 一码通颜色,：0为绿色
        "sfzx": "1",  # 是否在校：1为在校
        "tw": "1",  # 体温范围：36°C~36.5°C
        "area": bytes(province, 'utf-8') + b'\x20' + bytes(city, 'utf-8') + b'\x20' + bytes(
            area,
            'utf-8'),  # 省市区
        "city": bytes(city, 'utf-8'),  # 市
        "province": bytes(province, 'utf-8'),  # 省
        "address": bytes(address, 'utf-8'),  # 具体地点
        "geo_api_info": geo_api_info,
        "sfcyglq": "0",  # 是否处于隔离期
        "sfyzz": "0",  # 是否出现乏力、干咳、呼吸困难等症状
        "qtqk": "",  # 其他情况
        "askforleave": "0"
    }

if DailyReport:
    # 疫情通上报信息
    yqt_data={
        "sfzx": "0",  # 是否在校：否0是1
        "sfzgn": "1",  # 所在地点：中国大陆为1
        "area": bytes(province, 'utf-8') + b'\x20' + bytes(city, 'utf-8') + b'\x20' + bytes(
            area,
            'utf-8'),  # 省市区
        "city": bytes(city, 'utf-8'),  # 市
        "province": bytes(province, 'utf-8'),  # 省
        "address": bytes(address, 'utf-8'),  # 具体地点
        "zgfxdq": "0",  # 是否在中高风险地区：否0是1
        "tw": "3",  # 体温范围：36.5°C~36.9°C
        "sfcxtz": "0",  # 是否出现症状：否0是1
        "sfjcbh": "0",  # 是否接触接触无症状感染/疑似/确诊人群：否0是1
        "mjry": "0",  # 是否接触密接人员：否0是1
        "csmjry": "0",  # 是否去过疫情场所：否0是1
        "sfcyglq": "0",  # 是否处于隔离期：否0是1
        "sfjcjwry": "0",  # 是否接触境外人员：否0是1
        "sfcxzysx": "0",  # 是否有特别情况：否0是1
        "multiText": "",  # 其他情况
    }

