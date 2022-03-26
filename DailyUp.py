# 晨午晚检填写程序
import json
import datetime
from EmailSender import send_email
import Settings
import geo_pool_append

T = str(datetime.datetime.now() )[:-7]  # 时间

UPLOAD_URL = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"   # 填报时用的url

INFO_URL = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report"  # 查看填报信息时用的url

def up(subject, conn, name):

    result_main = conn.post(
        url=UPLOAD_URL,
        data=Settings.cwwj_data  # 填写数据
    )

    # 数据发送错误
    if result_main.status_code != 200:
        send_email(subject, T + '\n' + '数据发送错误，错误代码：' + result_main.status_code, name)
        exit()

    try:
        result_json = json.loads(result_main.text)  # 拿到返回信息

        # 异常情况
        if result_json['e'] != 0:
            info = 'error: ' + str(result_json['m'])

            # 如果检测到晨午晚检已手动填写，脚本将获取到此次填写的位置信息并将其加入到'Geo_pool.json'中
            if info == 'error: 您已上报过':
                respond = conn.get(INFO_URL)
                info = json.loads(respond.text)["d"].get('info').get('geo_api_info')
                geo_pool_append.add(info)
                send_email(subject, f'检测到{name}手动填写，位置信息已加入Geo_pool', Settings.Admin)
            
            # 其他错误情况
            else:
                send_email(subject, info, name)
        
        # 上报成功
        else:
            if Settings.Admin == name:      # 给管理员发送日志
                respond = conn.get(INFO_URL)
                info = json.loads(respond.text)["d"].get('info')
                msg = info.pop("geo_api_info", "no geo info")   # 除去位置信息，内容太多
                if msg == 'no geo info':
                    info['geo_api_info'] = 'No Position!'
                json_info = json.dumps(info, indent=4, sort_keys=False, ensure_ascii=False)     # 生成json格式的日志
                send_email(subject, T + '\n' + f'{subject}填写完成。\n {json_info}', name)
            else:
                send_email(subject, T + '\n' + f'{subject}填写完成。', name)
    except json.decoder.JSONDecodeError:
        print('晨午晚检填报程序数据发送部分出现异常。请检查是否按照步骤进行配置。')
        send_email(subject, T + '晨午晚检填报程序数据发送部分出现异常。请检查是否按照步骤进行配置。', name)


if __name__ == '__main__':
    # from Verifi import conn
    # up('wj', conn.get(Settings.Admin), Settings.Admin)
    pass
