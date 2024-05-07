import time
recent_time=time.strftime('%H:%M:%S')
recent_time=int(time.strftime('%H'))
c= input("enter your name")

if( recent_time<12):
    print("Good Morning", c.capitalize(),".It is",recent_time,"o'clock\nHave a great day")
elif(12<=recent_time and recent_time<19):
    print("Good Evening", c.capitalize() ,".It is",recent_time,"o'clock\nHave a great day")
else:
    print("Good Night", c.capitalize() ,".It is",recent_time,"o'clock\nSweet Dreams")
