1.

a = 'cat'
for i in a:
    print(ord(i), end=" ", sep='')

2.

def isvowel(character):
    if character in ['a','e','i','o','u']:
        return True
    else:
        return False

def add_ing(string):
    mixedstring = ''
    for i in string[-3:]:
        if isvowel(i):
            mixedstring += 'v'
        else:
            mixedstring += 'c'
    if mixedstring == 'cvc':
        a = string + string[-1] + 'ing'
        return(a)
    elif mixedstring == 'vvc':
        a = string + 'ing'
        return(a)
    elif mixedstring == 'vcv':
        a = string.strip("e")
        b = a + 'ing'
        return(b)
    elif mixedstring == 'ccv':
        a = string + 'ing'
        return(a)
    elif mixedstring == 'cvv':
        a = string + 'ing'
        return(a)
    elif mixedstring == 'vcc':
        a = string + 'ing'
        return(a)
    else:
        a = string+'ing'
        return(a)

print(add_ing('write'))

#3.
def word_to_number(word):
    if word == 'one':
        return(1)
    elif word == 'two':
        return(2)
    elif word == 'three':
        return(3)
    elif word == 'four':
        return(4)
    elif word == 'five':
        return(5)
    elif word == 'six':
        return(6)
    elif word == 'seven':
        return(7)
    elif word == 'eight':
        return(8)
    elif word == 'nine':
        return(9)
    elif word == 'ten':
        return(10)
    elif word == 'eleven':
        return(11)
    elif word == 'twelve':
        return(12)
    elif word == 'thirteen':
        return(13)
    elif word == 'fourteen':
        return(14)
    elif word == 'fifteen':
        return(15)
    elif word == 'sixteen':
        return(16)
    elif word == 'seventeen':
        return(17)
    elif word == 'eighteen':
        return(18)
    elif word == 'nineteen':
        return(19)
    elif word == 'twenty':
        return(20)
    elif word == 'thirty':
        return(30)
    elif word == 'forty':
        return(40)
    elif word == 'fifty':
        return(50)
    elif word == 'sixty':
        return(60)
    elif word == 'seventy':
        return(70)
    elif word == 'eighty':
        return(80)
    elif word == 'ninety':
        return(90)
    elif word == 'hundred':
        return(100)
    elif word == 'thousand':
        return(1000)
    elif word == 'million':
        return(1000000)
    elif word == 'billion':
        return(1000000000)

def chinese_character_to_arabic_number(character):
    if character == 'ä¸€':
        ## '\u4e00'
        return(1)
    elif character == 'äºŒ':
        ## '\u4e8c'
        return(2)
    elif character == 'ä¸‰':
        ## '\u4e09'
        return(3)
    elif character == 'å››':
        ## '\u56db'
        return(4)
    elif character == 'äº”':
        ## '\u4e94'
        return(5)
    elif character == 'å…­':
        ## '\u516d'
        return(6)
    elif character == 'ä¸ƒ':
        ## '\u4e03'
        return(7)
    elif character == 'å…«':
        ## '\u516b'
        return(8)
    elif character == 'ä¹':
        ## '\u4e5d'
        return(9)
    elif character == 'å':
        ## '\u5341'
        return(10)
    elif character == 'ç™¾':
        ## '\u767e'
        return(100)
    elif character == 'åƒ':
        ## '\u5343'
        return(1000)
    elif character == 'ä¸‡':
        ## '\u4e07'
        return(10000)
    elif character == 'è¬':
        ## '\u842c'
        return(10000)
    elif character == 'å„„':
        ## '\u5104'
        return(100000000)
    elif character == 'äº¿':
        ## '\u4ebf'
        return(100000000)
    elif character == 'å…†':
        ## '\u5146'
        return(1000000000000)

# sample_arabic_number_strings = ['Five hundred million two hundred three thousand seventeen', 'One billion seventy three', 'One hundred ninety two thousand seven hundred thirty one']
#
# sample_chinese_number_strings = ['ä¹ä¸‡äºŒåƒä¸‰ç™¾äºŒåä¸€','ä¹åƒäºŒç™¾ä¸‡äºŒåƒä¸‰ç™¾äºŒåä¸€','ä¹äº¿å…«åƒä¸‡å››ç™¾å…«åä¸€']
a = []
b = 'twenty two million three hundred thirty two thousand eight hundred ninety five'.split(' ')

def convert_array_step2(a):
    b = []
    hold = 0
    for i in range(0,len(a)):
      #print(a[i])
      current_number = a[i]

      if (current_number > 999):
        if hold > 0:
          b.append(hold)
          b.append(current_number)
          hold = 0
        else:
          b.append(current_number)
      elif hold == 0:
          hold = current_number
      elif current_number > hold:
          hold = hold * current_number
      else:
          b.append(hold)
          b.append(current_number)
          hold = 0

    if hold != 0:
        b.append(hold)
    return(b)

def convert_array_step3(a):
    hold = 0
    b = []
    for i in range(0,len(a)):
      #print(a[i])
      current_number = a[i]

      if (current_number > 999):
        b.append(hold)
        b.append(current_number)
        hold = 0
      elif hold == 0:
          hold = current_number
      elif current_number < hold:
          hold = hold + current_number
      else:
          b.append(hold)
          b.append(current_number)
          hold = 0
    if hold != 0:
      b.append(hold)
    return(b)

def convert_array_step4(a):
    hold = 0
    b = []
    for i in range(0,len(a)):
        #print(a[i])
        current_number = a[i]
        if (current_number > 999):
            hold = hold * current_number
            b.append(hold)
            hold = 0
        elif hold == 0:
            hold = current_number
        elif current_number < hold:
            hold = hold * current_number
        else:
            b.append(hold)
            b.append(current_number)
            hold = 0
    if hold != 0:
      b.append(hold)
    return(b)

def convert_array_step5(a):
    sum = 0
    for i in range(0,len(a)):
        sum = sum + a[i]
    print("The Sum of the number you entered is,", sum)


#convert b into number and put it into a
for i in b:
    a.append(word_to_number(i))

print(a)

output = convert_array_step2(a)

output2 = convert_array_step3(output)

output3 = convert_array_step4(output2)

answer = convert_array_step5(output3)

answer
