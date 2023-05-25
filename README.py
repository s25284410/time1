import time

minrtes = int(input("Enter the number of minutes to focus: "))
seconds = minutes * 60

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = '{:20d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    secinds -= 1
    
print("Time's up")
