1. 
def sports(data):
     teams_name,wins,loses,ties = data
     totals = wins+loses+ties
     score = (wins+ ties/2) / totals
     return(score)

def sort_data(data_list):
      print(data_list)
      a = []
      for b in data_list:
        a.append([sports(b), b])
      a.sort(reverse=True)
      return(a)

Input_Data = [['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]]

print(sort_data(Input_Data))

2.
import turtle

coord_list_1 = [[-200,200],[-200,90],[-50,-20]]
coord_list_2 = [[50,200],[50,170],[300,90],[50,30],[50,0],[50,-13],[50,-73]]

def sort_coordinate(a,b):
  global list
  list = []
  for coordinate in a: 
    for coordinate2 in b: 
      list.append([coordinate,coordinate2])
  
def draw_line(a,b):
  sort_coordinate(a,b)
  print(list)
  turtle.Screen()
  turtle.Turtle()
  for num_coordinate in list: 
    turtle.pu
    turtle.setposition(num_coordinate[0][0],num_coordinate[0][1])
    turtle.pd
    turtle.setposition(num_coordinate[1][0],num_coordinate[1][1])
     
draw_line(coord_list_1,coord_list_2)


3. 

import random 

deck = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

player_hand = [deck[random.randint(0,52)],deck[random.randint(0,51)]]
dealer_hand = [deck[random.randint(0,50)],deck[random.randint(0,49)]]

deck.remove(player_hand[0])
deck.remove(player_hand[1])
deck.remove(dealer_hand[0])
deck.remove(dealer_hand[1])
print(player_hand,dealer_hand,deck)

def who_will_win_end(player_hand,dealer_hand): 
  player = hand_to_score(player_hand)
  dealer = hand_to_score(dealer_hand) 
  if player > 21: 
    print("Dealer Wins! Your hand is too high!")
  elif dealer > 21: 
    print('Player Wins! Dealer hand is too high!')
  elif (player_hand == 'A') and ((player_hand == 'J') or (player_hand == 'Q') or (player_hand == 'K')):
    print('Player Wins through BlackJack')
    exit()
  elif (dealer_hand == 'A') and ((dealer_hand == 'J') or (dealer_hand == 'Q') or (dealer_hand == 'K')):
    print("Dealer Wins through BlackJack!")
    exit()
  elif player > dealer: 
    print('Player Wins! Player # higher than dealer!')
  else: 
    print("Dealer Wins!")

def convert_to_value(card): 
  if (card == 'J') or (card == 'Q') or (card == 'K'):
    return 10
  elif card == 'A':
    return 1
  else: 
    return card

def hand_to_score(hand):
  sum = 0 
  print(hand)
  for card in hand: 
    converted_number = convert_to_value(card)
    sum += converted_number
  print(sum) 
  return sum 


def game():
  print('Welcome to BlackJack')
  print("Here's your hand:",player_hand)
  player_score_1 = hand_to_score(player_hand)
  dealer_score_1 = hand_to_score(dealer_hand)
  if (player_hand == 'A') and ((player_hand == 'J') or (player_hand == 'Q') or (player_hand == 'K')): 
    print('Player Wins through BlackJack!')
  elif (dealer_hand == 'A') and ((dealer_hand == 'J') or (dealer_hand == 'Q') or (dealer_hand == 'K')):
    print("Dealer Wins through BlackJack!")
  else:
    print('You have an option to get an extra card. yes or no?')
    decision = input('')
    if (decision == 'yes') or (decision == 'Yes'):
      player_hand.append(deck[random.randint(0,48)])
      final_score_player = hand_to_score(player_hand)
      if (final_score_player < 21) or (final_score_player == 22): 
        if (dealer_score_1 < 16) or (dealer_score_1 == 16): 
          dealer_hand.append(deck[random.randint(0,47)])
          final_score_dealer = hand_to_score(dealer_hand)
          if (final_score_dealer) > 22 or (final_score_dealer == 22):
            print("Player Wins!")
          else: 
            who_will_win_end(player_hand,dealer_hand)
      else: 
        print("Dealer Wins! Your card is too high")
    else:
      if (dealer_score_1 < 16) or (dealer_score_1 == 16): 
          dealer_hand.append(deck[random.randint(0,47)])
          final_score_dealer = hand_to_score(dealer_hand)
          if (final_score_dealer) > 22 or (final_score_dealer == 22):
            print("Player Wins!")
          else: 
            who_will_win_end(player_hand,dealer_hand)
      else: 
        who_will_win_end(player_hand,dealer_hand)


game()