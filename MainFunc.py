import time
import Settings
import DailyUp
import DailyReport
from Verifi import conn


if __name__ == '__main__':
    hour = int(time.strftime("%H", time.localtime()))
    for name in conn.keys():
        # 晨午晚检
        if Settings.DailyUp:
            if hour <= 12:
                DailyUp.up('晨检', conn.get(name), name)
            if 12 <= hour < 18:
                DailyUp.up('午检', conn.get(name), name)
            if hour > 18:
                DailyUp.up('晚检', conn.get(name), name)

        # 疫情通
        if Settings.DailyReport:
            DailyReport.report(conn.get(name), name)
