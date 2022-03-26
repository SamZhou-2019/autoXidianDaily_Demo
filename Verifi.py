# 学生认证部分
import datetime
import json
from json.tool import main
from click import pass_context
import requests

import Settings
from EmailSender import send_email

T = str(datetime.datetime.now() )[:-7]  # 时间
num = len(Settings.identity_confirm)    # 待填写人数

conn = {}
for name in Settings.identity_confirm.keys():
    try:
        sess = requests.Session()
        result_login = sess.post(
            url='https://xxcapp.xidian.edu.cn/uc/wap/login/check',
            # username 学号,password 统一登录密码
            data={'username': Settings.identity_confirm.get(name).get('stu_id'), 'password': Settings.identity_confirm.get(name).get('stu_pass')}
        )
        login_json = json.loads(result_login.text)
        conn[name] = sess
    except requests.exceptions.ConnectionError:
        print("网络连接中断,请检查网络连接。")
        exit()

    #  错误1:登录错误 
    if result_login.status_code != 200:
        print('登录连接错误,HTTP状态码:', result_login.status_code)
        send_email('登录错误', T + '\n' + '登录连接错误,HTTP状态码:' + result_login.status_code)
        exit()
    else:
        try:
            if login_json['e'] != 0:
                print('登录错误,错误信息: ' + login_json['m'])
                send_email('登录错误', T + '\n' + '登录错误,错误信息:' + login_json['m'])
                exit()
            else:
                # 成功登录
                print(f'{name}登录成功。')

        except json.decoder.JSONDecodeError:
            print('疫情通及晨午晚检填报程序登录部分出现异常。请检查是否按照步骤进行配置。')
            send_email('填报程序出现异常', T + '疫情通及晨午晚检填报程序登录部分出现异常。请检查是否按照步骤进行配置。')
            exit()



if __name__ == "__main__":
    pass