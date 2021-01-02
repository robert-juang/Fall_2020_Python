from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import os
from blanks_globals import stop_words,pos_categories,basic_wikipedia_search_url

list_for_paragraph = []
list_without_punctuation = []
random_words_10 = [] 
parts_of_speech_words = [] 
dictionary_word_to_pos = {} 
dictionary_new_words = {}
new_word_list = []


def read_wikipedia(link):
  #import stuff and get things set up for beautiful soup
  wikipedia = 'https://en.wikipedia.org/wiki/'
  subject = link
  wikipedia_search_link = wikipedia + subject
  output = urlopen(wikipedia_search_link)
  soup = BeautifulSoup(output,'html.parser')
  paragraphs = soup.find_all('p')

  #start defining what a paragraph will look like 
  for paragraph in paragraphs:
    first_paragraph = paragraph.text[0:len(paragraph.text)]
    length = len(paragraph.text)
    #conditions for a paragraph length wise
    if length < 250:
        continue
    else:
        break 
  #write the paragraph into a document in Python folder 
  write_paragraph = open('wikipedia_paragraph', 'w')
  write_paragraph.write(first_paragraph) 

#generate 10 words from a given text file (Change so that it generates it from N number of words)
def generate_words_from_text(file):
    original_text = open(file, 'r')
    for lines in original_text:
        lines = lines.lower()
        words = lines.split(" ")
        for word in words:
            result = word.strip(',."/!?\;() ')
            list_without_punctuation.append(result)  
    #print(list_without_punctuation)
    filter_out_word()
    

#Filter out the words so that only certain ones are chosen 
def filter_out_word():
    global no_dup_random_words_10
    for a in range(0, 10):
        random_words_10.append(list_without_punctuation[random.randint(0,len(list_without_punctuation)-2)])
    for things in random_words_10: 
        choose_word(things)
        
    unique_set = set(random_words_10)
    
    no_dup_random_words_10 = list(unique_set) 

        
#remove the word if it's in the stop_words list 
def choose_word(word):
    for things in stop_words:
        if word == things:
            print('[removed]',word)
            try: 
                random_words_10.remove(word)
            except:
                continue 


#return the parts of speech of a particular word            
def parts_of_speech(random): 
  print('Your options for categories include: person name, organization name, place name, other name, singular noun, adjective, adverb')
  print('Choose a Category for the Word:',random)
  POS = input('')
  parts_of_speech_words.append(POS)
    

#part 2 / run the above program and put things into a dictionary            
def make_wikipedia_template():
    topic = input('What would you like your Blanks game to be about?')
    read_wikipedia(topic)
    generate_words_from_text('wikipedia_paragraph') 
    for word in no_dup_random_words_10:
      parts_of_speech(word)
    for items in range(0,len(no_dup_random_words_10)):
        dictionary_word_to_pos[no_dup_random_words_10[items]] = parts_of_speech_words[items] 
    get_new_words()
    replace_words() 

# get new word for the parts of speech to replace the existing word

def get_new_words():
    for things in random_words_10:
        print('Give me a word belonging to the category:',dictionary_word_to_pos[things])
        new_word = input('')
        dictionary_new_words[new_word] = dictionary_word_to_pos[things]
        new_word_list.append(new_word) 
    #print(dictionary_new_words)
    #print(new_word_list) 

#Part 3 / replace the words so that a mad_lib is written
    
def replace_words():
    readed = open('wikipedia_paragraph') 
    writed = open('mad_lib','w')
    filedata = readed.read() 
    for i in range(0,len(no_dup_random_words_10)):
        filedata = filedata.replace(no_dup_random_words_10[i],new_word_list[i])
    writed.write(filedata) 
    readed.close
    writed.close 
    
make_wikipedia_template()
