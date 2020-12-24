#1.
def triangle(number): 
  if number <= 1: 
    return number
  else: 
    return number + triangle(number-1)




#2.
def question():
  things = input('Are we there yet?')
  if things == 'yes': 
    exit
  else: 
    question() 


#3.
	

def QuickSort(list):
    n = len(list)

    lower = []
    higher = []

    if n == 0 or n == 1:
        return list

    elif n == 2:
        if list[1] < list[0]:
            t = list[0]
            list[0] = list[1]
            list[1] = t

        return list

    else:
        pivot = list[0]

        for i in range(1, len(list)):
            if list[i] < pivot:
                lower.append(list[i])
            else:
                higher.append(list[i])

    lower = QuickSort(lower)
    higher = QuickSort(higher)

    newList = []
    newList = lower
    newList.append(pivot)
    newList.extend(higher)

    return newList

input_list = [35, 42, 39,7, 49, 46, 33, 43, 28, 25]

print(QuickSort(input_list))