 #1.  
 #A file with the name 'practice_text.txt' has to be in the directory for this to work 
 
text = open("practice_text.txt", "r") 
  
d = dict() 
word_list = []
clean_list = []

for line in text:
    lower_case = line.lower()
    the_thing = lower_case.split()
    word_list.append(the_thing)

for word in word_list:
    for individual in word:
          finished = individual.strip(',."/!?\;() ')
          clean_list.append(finished) 
print(clean_list)

for word in clean_list: 
   if word in d: 
     d[word] = d[word] + 1
   else: 
     d[word] = 1
  
for key in list(d.keys()): 
    print(key, ":", d[key]) 






# 2. 

Holiday_dictionary = {'Easter' : '4/4/2020', 'Christmas' : '12/25/2020', 'Halloween' : '10/30/2020', 'Thanksgiving' : '11/26/2020', 'Hanakkah' : '12/10/2020', 'Ramadan' : '4/23/2020', 'Diawli' : '11/14/2020', 'Hwanzaa' : '12/26/2020'}


def replace_with_holiday(string):
  List = [] 
  split_sentence = string.split() 
  for word in split_sentence: 
    List.append(word) 
    for holiday in Holiday_dictionary: 
      if holiday == word:
        List.remove(word)
        List.append(Holiday_dictionary[holiday])
      else: 
        continue
  print(List)
  
replace_with_holiday('Here are the dates: Easter Christmas Halloween Thanksgiving Hanakkah Ramadan Diawli Hwanzaa')

# 3. 
import os
dict = {}
lists = []
alphabetical_list = []
organized_dict = {} 

def reading_phone_book(file):
    with open(file,'r') as text:
        for values in text:
            value = values.strip(os.linesep)
            items = value.split('\t')
            lists.append(items)
    for contacts in lists:
        dict[contacts[0]] = contacts[1]
    text.close()

def add_new_names_to_phone_book():
    while True:
        b = input('Do you want to add a contact?')
        if b == 'yes':
            name = input('Please enter the name of the person')
            number = input("Please enter that person's number in the format: xxx-xxx-xxxx")
            dict[name] = number
        else:
            return False
        
def alphabetical_order(dictionary):
    print(dict) 
    for names in dictionary:
        alphabetical_list.append(names)
        alphabetical_list.sort()
    for names in alphabetical_list:
        organized_dict[names] = dict[names]

def update_phonebook1(infile,outfile):
    reading_phone_book(infile)
    add_new_names_to_phone_book()
    alphabetical_order(dict) 
    output = open(outfile,'w')
    output.write('Name\tPhone Number\n')
    for items in organized_dict:
        output.write(items)
        output.write('\t')
        output.write(organized_dict[items])
        output.write('\n') 
        
        
update_phonebook1('simple_phone_book.tsv','simple_phone_book_output.tsv')


#4. 
import os
dict = {}
organized_dict = {}
lists = []
numerical_list = []


def reading_phone_book(file):
    with open(file,'r') as text:
        for values in text:
            value = values.strip(os.linesep)
            items = value.split('\t')
            lists.append(items)
    for contacts in lists:
        dict[contacts[1]] = contacts[0]
        
    print(lists)
    print(dict)
    
    text.close()

def add_new_names_to_phone_book():
    while True:
        b = input('Do you want to add a contact?')
        if b == 'yes':
            number = input("Please enter that person's number in the format: xxx-xxx-xxxx")
            name = input('Please enter the name of the person')
            dict[number] = name
        else:
            return False
        
def numerical_order(dictionary):
    for names in dictionary:
        numerical_list.append(names)
        numerical_list.sort()

    for numbers in numerical_list:
        organized_dict[numbers] = dict[numbers]

    
def update_phonebook2(infile,outfile):
    reading_phone_book(infile)
    add_new_names_to_phone_book()
    numerical_order(dict) 
    output = open(outfile,'w')
    output.write('Name\tPhone Number\n')
    for items in organized_dict:
        output.write(items)
        output.write('\t')
        output.write(organized_dict[items])
        output.write('\n') 
        
        
update_phonebook2('simple_phone_book.tsv','simple_phone_book_output_2.tsv')


