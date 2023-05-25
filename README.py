import time

minutes = int(input("請輸入要專注的分鐘數: "))
seconds = minutes * 60

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)  # 修正此行，將原本的 20d 改為 02d
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1  # 修正此行，將原本的 secinds 改為 seconds

print("時間到！")
