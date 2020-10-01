## Name: Robert Jiang
## Homework 2: Exercises 1-8

## 1.

Day_of_week = ('Wednesday,')
Month = ('September ')
Day_of_month = ('16,')
Year = ('2020')

print (Day_of_week,Month,Day_of_month,Year,sep="")

## 2. 

print ('''The newscaster said, "And Now for Something Completely Different!"\n \nOne quote: ', Two quotes ", Red Quotes, Blue Quotes''')

## 3.

print('5'+'4')

## This one adds two strings back to back; the operation does not involve numbers

print(5+4)

## This one adds two integers together; it is an operation involving numbers

## 4. 

output = str(int('5') + int('4'))

print (output)

## 5.

## a.
output = ((5*5)/5)-5
print(output)

## b.
output = 5-((5**5)*5)
print(output)

## c.
output = 60-(40*1.5)+(5**2)-25
print(output)

## 6.

quarters = 543//25

remaining_amount1 = 543%25

nickels = remaining_amount1//5

pennies = remaining_amount1 - nickels*5

print(quarters,'quarters',nickels,'nickels',pennies,'pennies')

## 7.

def num(num1, num2, num3):
    num = (num1+num2+num3)//3
    return(num)

avg = num(3,6,9)

print (avg)


## 8.


def func2(haha):
    print('haha')
    print('haha ','haha ','haha', sep="")

print ('You entered:')

func2('haha')



## 9.

def Function_1(number1, number2, number3, number4, number5, number6):
    calc1 = (number1 + number2 + number3)//3
    calc2 = (number4 + number5 + number6)//3
    result = calc1 + calc2
    return(result)

numbers = Function_1(5,10,15,20,25,30)

print(numbers)
