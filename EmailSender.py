import smtplib
import datetime
from email.mime.text import MIMEText

import Settings

# BJT = str(datetime.datetime.now() + datetime.timedelta(hours=+8))[:-7]  # 时间
T = str(datetime.datetime.now() )[:-7]  # 时间


# % 邮件部分 %
def send_email(subject, message, name):  # 发送一封邮件
    email_address = Settings.email_confirm.get(name).get('email_address')
    authorization = Settings.email_confirm.get(name).get('email_authorization')  # 邮箱校验码
    email_server = Settings.email_confirm.get(name).get('email_server')  # 邮箱服务器地址
    email_port = Settings.email_confirm.get(name).get('email_port')  # 邮箱服务器端口
    
    msg_from = email_address  # 发送方邮箱
    msg_to = email_address  # 接收方，即自己给自己
    sbj = subject  # 标题
    msg = MIMEText(message)  # HTML纯文本格式发送邮件 
    msg['Subject'] = sbj
    msg['From'] = msg_from
    msg['To'] = msg_to

    s = smtplib.SMTP_SSL(email_server, email_port)  # 邮件服务器（逗号前）及端口号（逗号后）
    s.login(msg_from, authorization)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print(f'send a email to {msg_to}')


if __name__ == '__main__':
    pass