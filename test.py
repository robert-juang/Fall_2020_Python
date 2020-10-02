import time

def clock(hour,minute,second,tenths):
    a = 5
    while a == 5:
        for tenths in range(1,10):
            time.sleep(0.1)
            print(hour,":",minute,":",second,".",tenths)
            if tenths == 9:
                second = second + 1
                tenths = 0
                print(hour,":",minute,':',second,".",tenths)
                if second == 59:
                    for tenths in range(1,10):
                        time.sleep(0.1)
                        print(hour,":",minute,":",second,".",tenths)
                        if hour == 23 and minute == 59 and second == 59 and tenths == 9:
                            hour = 0
                            minute = 0
                            second = 0
                            tenths = 0
                            print(hour,":",minute,":",second,".",tenths)
                        if minute == 59 and tenths == 9:
                            minute = 0
                            second = 0
                            tenths = 0
                            hour = hour + 1
                            print(hour,':',minute,":",second,".",tenths)
                        if tenths == 9:
                            tenths = 0
                            second = 0
                            minute = minute + 1
                            print(hour,":",minute,":",second,".",tenths)
    else:
        print('hi')


clock(0,0,0,0)
