import time
user_time=int(input('enter time in seconds'))
while(user_time):
    mins, secs = divmod(user_time,60)
    timer='{:02d}:{:02d}'.format(mins, secs)
    print(timer,end='\r')
    time.sleep(1)
    user_time-=1
print('times up')
