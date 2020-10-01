#1.

def number(n):

    remainder = n % 2

    if n == 0:
        print('zero')
        exit()
    if remainder == 0:
        print('even')
    else:
        print('odd')
    if n/3 == int(n/3):
        print('divisble by three')

number(12)

#2.

def func(n):
    remainder = n % 2
    remainder2 = n % 3
    if remainder == 0 and remainder2 != 0:
        condition1 = (True)
        condition2 = (False)
    elif remainder != 0 and remainder2 != 0:
        condition2 = (False)
        condition1 = (False)
    elif remainder != 0 and remainder2 == 0:
        condition2 = (True)
        condition1 = False
    elif remainder == 0 and remainder2 == 0:
        condition1 = False
        condition2 = False
    else:
        print('this number does not make sense')

    if (condition1 == True) or (condition2 == True):
        print('True')
    else:
        print('False')

func(6)

#condition1 false (number is even and it divisible by 3) = 12
#condition1 true (number is even and is not divisble by 3)= 22
#condition2 false (number is odd and it not divisble by 3) = 13
#condition2 true (nuber is odd and it divisble by 3) = 27

#3.

print("Choose a statement in your mind that you would like to have evaluated")
print('Note: Please use all lowercase when answering the two questions')
print('Is your statement True,False, or Unknown according to experts in the relevant domain or according to some objective set of facts?')
a = input('')

print('Is your statement True, False, or Unknown according to Donald Trump?')
b = input('')

def test_your_facts(a, b):
    if (a == 'true') and (b == 'true'):
        print('Classification: True')
    elif (a == 'false') and (b == 'false'):
        print('Classification: False')
    elif (a == 'unknown') and (b == 'unknown'):
        print('Classification: Unknown')
    elif (a == 'false' or 'unknown') and (b == 'true'):
        print('Classification: Alternative Fact')
    elif (a == 'true' or 'unknown') and (b == 'false'):
        print('Classification: Alternative Falsehood')
    elif (a == 'true' or 'false') and (b == 'unknown'):
        print('Classification: Alternative Unknown')
    else:
        print('Try again')

test_your_facts(a, b)

Part2.

print ('Oh no, the princess has been kidnapped! You are supposed to prevent the princess from being captured, but you are terrible at your job. You decide to go on an adventure to try and retrieve and princess.')

print ('You are not very bright, so you think of different ways in which you can rescue the princess. Pick a number from the choices below:')
print('1. You decide to investigate the room where the princess was captured')
print('2. You decide to meet the local oracle for advice')
print('3. You do nothing')

def second():
    print("The letter inside reads: 'Do not trust the oracle! He kidnapped me! Come to the basement of the castle!!'")
    print("You then turn around and sees the oracle approaching you.")
    print('1. Ignore him and proceed to the basement')
    print('2. Ready your sword and try killing the oracle')
    print('3. Offer him the necklace')
    choice = int(input())
    if choice == 1:
        print("As you walk by him, he pulled out his wand and turns you into a rabbit. He puts you inside a cage and takes the cage down to the basement. The princess doesn't realize that you've been turned into a rabbit and you spent the rest of eternity down there with the princess...as a rabbit")
        print('The End')
    elif choice == 2:
        print("As soon as you lift your sword, the oracle pulls out his wand and turns you into a rat. While you didn't save the princess, at least you're not going to starve as you sneak your way into the castle's kitchen.")
        print('The End')
    elif choice == 3:
        print("The Oracle takes the necklace and walks away. You hurry to the basement and find the princess unconscious in a large cage. You open the cage and free the princess. She gives you a kiss on the cheek.")
        print('Congratuations! You achieved the best ending!')
    else:
        print('pick a valid number')

def first():
    print("In the princess's room, you find the princess's necklace and an envelope. She is nowhere to be seen.")
    print('1. Open the envelope')
    print("2. Take the necklace and sell it for money. After all, what's the point in saving the princess?")
    print('3. You do nothing')
    choice = int(input())
    if choice == 1:
        second()
    elif choice == 2:
        print('As soon as you grab the necklace, the local oracle barges into the room with a wand in hand. You are turned into a frog. He then proceeds to step on you. You Die!!')
    elif choice == 3:
        print('The princess dies. Gosh! You are so lazy. Do you not shed a single tear of remorse? Do you feel happy now that the princess is dead?')
    else:
        print('pick a valid number')

choices = int(input(''))

if choices == 1:
    first()
elif choices == 2:
    print('The oracle tells you that you should investigate the room where the princess was captured. Do you trust the oracle?')
    print('1. Yes')
    print('2. No')
    choices2 = int(input(''))
    if choices2 == 1:
        first()
    elif choices2 == 2:
        print("You turn around to leave, but the oracle backstabs and kills you. You die!!")
    else:
        print('pick a valid number')

elif choices == 3:
    print('The princess dies. Gosh! You are so lazy. Do you not shed a single tear of remorse? Do you feel happy now that the princess is dead?')
    exit()
else:
    print('pick a valid number')
