# time1
import datetime
import time

# 定義專注時間的起始和結束時間
start_time = datetime.time(9, 0, 0)   # 9點
end_time = datetime.time(17, 0, 0)    # 17點

while True:
    current_time = datetime.datetime.now().time()

    # 檢查是否在專注時間範圍內
    if start_time <= current_time <= end_time:
        print("現在是專注時間！")
    else:
        print("現在不是專注時間。")

    # 暫停一秒
    time.sleep(1)
