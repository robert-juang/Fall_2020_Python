#1.
def voting_ratio(number_of_democrats,number_of_republicans):
    try:
      ratio = float(number_of_democrats)/float(number_of_republicans)
      if ratio == 0:
        print("All Republicans")
      else:
        print(ratio)
    except:
      print("All Democrats")



voting_ratio(89778,67856)


#2.

def read_story(file):
  story = open(file,'r')
  vowela = 0
  vowele = 0
  voweli = 0
  vowelo = 0
  vowelu = 0
  for lowercase in story:
      a = lowercase.lower()
      vowel = 'a','e','i','o','u'
      for vowel in a:
          if vowel == 'a':
              vowela = vowela + 1
          elif vowel == 'e':
              vowele = vowele + 1
          elif vowel == 'i':
              voweli = voweli + 1
          elif vowel == 'o':
              vowelo = vowelo + 1
          elif vowel == 'u':
              vowelu = vowelu + 1
  print(vowela,vowele,voweli,vowelo,vowelu)
  write_new_document(vowela,vowele,voweli,vowelo,vowelu)
  story.close()

def write_new_document(a,e,i,o,u):
    vowel = open('Vowel_Profile','w')
    vowel.write('This is a Vowel Profile file.\n')
    vowel.write('A Frequency:')
    vowel.write(str(a))
    vowel.write('\n')
    vowel.write('E Frequency:')
    vowel.write(str(e))
    vowel.write('\n')
    vowel.write('I Frequency:')
    vowel.write(str(i))
    vowel.write('\n')
    vowel.write('O Freqneycy:')
    vowel.write(str(o))
    vowel.write('\n')
    vowel.write('U Frequency:')
    vowel.write(str(u))
    vowel.close()

read_story('practice_text.txt')

# line = story.readline() #read oneline at a time
#
# line_list = big_string.split(os.olinesep) #splitting the story
#
# os.getcwd() #identifies the cwd

#3. 
import os

split_list = []
old_team = [] 
sorted_team = [] 

def sports(wins, loses, ties):
    totals = int(wins)+int(loses)+int(ties) 
    score = (int(wins)+ int(ties)/2) / int(totals)
    return(score)

def sort_data(data_list):
    for b in data_list: 
        old_team.append([sports(b[1],b[2],b[3]), b])
    old_team.sort(reverse=True)
  
def add_team():
  print("Do you want to add a team?")
  a = input('')
  while a == 'yes':
    print('What would you like to add? Type "done" if you are finished')
    team = input('')
    if team == 'done':
      a = False
      return a 
    print('What is the Wins? Losses? And Ties? Enter the numbers one after another (press enter after wins and so on)')
    win = input('')
    loses = input('')
    ties = input('')
    score_of_team = sports(win,loses,ties)
    output = [team, win, loses, ties]
    split_list.append(output) 
  else:
    exit 

def read_input_data(data):
  file = open(data,'r')
  for items in file:
    b = items.split() 
    split_list.append(b)
  add_team()
  sort_data(split_list)
  file.close()

def write_sample_lines():
  read_input_data('hw7.tsv')
  file = open('new_profile','w')
  for list in old_team:
      sorted_team.append(list[1])
  print(sorted_team)
  for item in sorted_team:
    file.write(item[0])
    file.write('\t')
    file.write(item[1])
    file.write('\t')
    file.write(item[2])
    file.write('\t')
    file.write(item[3])
    file.write('\n')  
  file.close() 
  

write_sample_lines()


#4. 
#problem4
import os
import sys
import csv

def average_movie_scores(filename):
    data = None
    if os.path.isfile(filename):
        data = getData(filename)
    else:
        sys.exit(1)
    print("Would you like to add a new user?")
    choice = input("Yes or No?")
    while choice not in ["no", "No"]:
        new_user = [data[len(data) - 1][0] + 1]
        for movie in data[0]:
            print('Did you see the movie', movie, "?")
            print('O means you did not see the movie')
            print('Otherwise the ratings are: 1: Terrible, 2: Bad, 3: Average, 4: Good, 5: Fantastic')
            rating = int(input("What is your rating?"))
            new_user.append(rating)
        print("Add one more user?")
        choice = input("Yes or No?")
    show_data(data)

def show_data(data):
    for i in range(len(data[0])):
        movie = data[0][i]
        total = 0
        for j in range(1, len(data)):
            total += data[j][i]
        average = total/(len(data) - 1)
        count = 0
        for j in range(1, len(data)):
            if data[j][i] > 0:
                count += 1
            if count > 0:
                print("The movie", movie, "had an average score of", average, ".", count, "people saw it in this sample.")
            elif count == 0:
              print('Nobody saw,',movie) 

def getData(filename):
    data = []
    file = open(filename, "r")
    i = 0
    for line in file:
        line = line.rstrip()
        line = line.split("\t")
        if i > 0:
            for j in range(len(line)):
                line[j] = int(line[j])
        data.append(line)
        i = i + 1
    file.close()
    return data

average_movie_scores('sample_rating.tsv') 

