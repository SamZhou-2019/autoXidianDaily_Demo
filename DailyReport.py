# 疫情通填写程序
import json
import datetime
from EmailSender import send_email
import Settings

T = str(datetime.datetime.now() )[:-7]  # 时间
def report(conn):
    # 

    result_main = conn.post(
        url="https://xxcapp.xidian.edu.cn/ncov/wap/default/save",
        data=Settings.yqt_data  # 填写数据
    )

    # @ 错误2：数据发送错误 @
    if result_main.status_code != 200:
        print("数据发送错误，错误代码：", result_main.status_code)
        send_email('疫情通', T + '\n' + '数据发送错误，错误代码：' + result_main.status_code)
        exit()
    else:
        try:
            # @ 程序完成 @
            result_json = json.loads(result_main.text)
            print(T + '  疫情通填写完成。\nmsg：' + result_json['m'])
            # send_email('疫情通', T + '\n程序完成。\n' + str(result_json['e']) + '-' + result_json['m'])
        except json.decoder.JSONDecodeError:
            print('疫情通填报程序数据发送部分出现异常。请检查是否按照步骤进行配置。')
            send_email('疫情通', T + '疫情通填报程序数据发送部分出现异常。请检查是否按照步骤进行配置。')

if __name__ == '__main__':
    report()