# #1.


def triangle_number(num):
    sum = 0
    for i in range(0,num+1,1):
        sum += i
    print(sum)


triangle_number(10)


# #2.


def make_a_rectangle(height, width, character):

    for i in range(0,height):
        print(character*width)

make_a_rectangle(5,10,'*')

#3.
def make_a_parallelogram(height, width, character):

    for i in range(0,height):
        a = height-i
        print(" "*a)
        print(character*width)

make_a_parallelogram(9,10,'*')

#4.
import time
def addZero(string):
    if (len(string)==1):
        return '0'+string
    return string

def times(hours, minutes, seconds, tenths):
    i = (int(hours)*36000 + int(minutes)*600 + int(seconds)*10 + int(tenths))
    while True:
        time.sleep(0.1)
        tenths = i%10
        seconds = str(int(i/10)%60)
        minutes = str(int(i/600)%60)
        hours = str(int(i/36000)%24)
        print(addZero(hours),":",addZero(minutes),":",addZero(seconds),".",tenths)
        i = i+1

times(0,0,0,0)
