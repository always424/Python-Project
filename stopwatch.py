import time

value   = int(input("Enter Time In Seconds : "))

for i in reversed(range(0,value)):
    seconds = int(i%60)
    minutes = int((i / 60)) % 60
    hours = int(i / 3600)
    time.sleep(1)
    print(f"{hours:02} : {minutes:02} : {seconds:02}")

print("TIMES UP !!!!")
