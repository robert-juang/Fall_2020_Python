1. 
from turtle import *
import math
import random 

class rainbow_turtle(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.pu()
    self.setpos(-100,-100)
    self.pd() 
  def fd (self,distance):
    colors = ["red","orange","yellow","green","blue","indigo","purple"]
    segments = distance//10
    for move in range(segments): 
      self.pd()
      self._go(5)
      self.pencolor(colors[random.randint(0,6)])
      self.pu()


def test_turtles():
    global adam3
    adam3 = rainbow_turtle()
    adam3.speed(0)
    for num in range(3): 
        adam3.fd(100)
        adam3.left(120)
    for num in range(4):
        adam3.fd(100)
        adam3.left(90) 
    for num in range(5):
        adam3.fd(100)
        adam3.left(72)
    for num in range(6):
        adam3.fd(100)
        adam3.left(60)
    for num in range(7): 
        adam3.fd(100)
        adam3.left(51.42857143)

test_turtles()

2.

class weighted_die: 
  def __init__(self,number_of_sides):
    self.number_of_sides = number_of_sides
  def roll(self):
    self.face = random.randint(1,100)
    if self.face >= 1 and self.face <= 10: 
      return(1) 
    elif self.face >= 11 and self.face <= 22:
      return(2) 
    elif self.face >= 23 and self.face <= 37:
      return(3) 
    elif self.face > 38 and self.face <= 55:
      return(4) 
    elif self.face >= 56 and self.face <= 76:
      return(5)
    elif self.face >= 77 and self.face <= 100:
      return(6)
    else: 
      return(none)

def question_2():
  test_die = weighted_die(6)
  print('Testing Weighted Die 20 rolls')
  for num in range(20): 
    print(test_die.roll())

question_2()

#3.
from dice import *
from game_utilities import *
import random


class dice_game():
    def __init__(self,game_name):
        self.score = 0
        self.game_name = game_name
        self.die = die(6)
    def __repr__(self):
        return('Game: ' + self.game_name + str(utility.get_id_num()))
    def __str__(self):
        return('Game: ' + self.game_name)
    def game_over_who_wins(self):
        None
    def print_score(self):
        print(self.score)
    def one_turn(self):
        print('Next Turn')
    def play_game(self):
        while not(self.game_over_who_wins()):
            self.one_turn()
            self.print_score()

class war_dice_game(dice_game):
    def __init__(self, game_name, end_score, cheating=False):
        self.score = 0
        self.computer_score = 0
        self.end_score = end_score
        if cheating:
            self.die = cheat_die1(6,4)
        else:
            self.die = die(6)
        self.computer_die = die(6)
        print('***This is',game_name+'!')
    def print_score(self):
        print('Computer has', self.computer_score,'points.')
        print('You have',self.score,'points.')
    def game_over_who_wins(self):
        if self.computer_score > self.end_score:
            self.print_score()
            print('Computer Wins!')
            return(True)
        elif self.score > self.end_score:
            self.print_score()
            print('You Win!')
            return(True)
        else:
            return(False)

class Boom(war_dice_game):
	def __init__(self,game_name = "The game"):
		super().__init__(game_name, 10, False)
		self.player_dice = [die(i) for i in range(1,10 + 1)]
		self.player_dice_used = [False for i in range(10)]
		self.computer_dice = [die(i) for i in range(1,10 + 1)]
		self.computer_dice_used = [False for i in range(10)]
		self.computer_score = 0
		self.player_score = 0
	
	def play(self):
		print("Boom!")
		for i in range(10):
			computer_die = self.get_random_dice()
			computer_roll = computer_die.roll()
			print("The computer rolled", computer_roll)
			player_die = self.get_player_input()
			player_roll = player_die.roll()
			print("You rolled", player_roll)
			if computer_roll > player_roll:
				self.computer_score += computer_roll
			elif computer_roll == player_roll:
				pass
			elif computer_roll < player_roll:
				self.player_score += player_roll
			
			print("Computer has " + str(self.computer_score) + " points.")
			print("You have " + str(self.player_score) + " points.")
		if self.computer_score > self.player_score:
			print("You lost!")
		elif self.computer_score == self.player_score:
			print("Tie")
		elif self.computer_score < self.player_score:
			print("You win!")
			
	def get_player_input(self):
		print("Choose a die number.")
		self.print_available_dice()
		die_index = int(input()) - 1
		while self.player_dice_used[die_index]:
			print("please choose one of the options!")
			die_index = int(input("Which number? ")) - 1
		die = self.player_dice[die_index]
		self.player_dice_used[die_index] = True
		return die
	
	def print_available_dice(self):
		print("\n\n")
		for i in range(10):
			if not self.player_dice_used[i]:
				print(self.player_dice[i].number_of_sides)
			
	
	def get_random_dice(self):
		i = random.randint(0,9)
		while self.computer_dice_used[i]:
			i = random.randint(0,9)
		die = self.computer_dice[i]
		self.computer_dice_used[i] = True
		return die	


class single_dice_war_simple(war_dice_game):
    def one_turn(self):
        computer_roll = self.computer_die.roll()
        player_roll = self.die.roll()
        print('You rolled',player_roll,'and the computer rolled',computer_roll)
        self.score = self.score+player_roll
        self.computer_score = self.computer_score+computer_roll

class single_dice_war_with_pot(war_dice_game):
    def __init__(self, game_name, end_score,cheating=False):
        self.game_name = game_name
        self.score = 0
        self.computer_score = 0
        self.end_score = end_score
        if cheating:
            self.die = cheat_die1(6,4)
        else:
            self.die = die(6)
        self.computer_die = die(6)
        self.pot = 0
    def one_turn(self):
        computer_roll = self.computer_die.roll()
        player_roll = self.die.roll()
        difference = player_roll-computer_roll
        print('You rolled',player_roll,'and the computer rolled',computer_roll)
        if difference > 0:
            difference = difference + self.pot
            print('You gain',difference,'points.')
            self.score=self.score+difference
            self.pot = 0
        elif difference < 0:
            difference = (-1 *difference)+self.pot
            print('You lose',difference,'points')
            self.computer_score=self.computer_score+difference
            self.pot = 0
        else:
            print('It is a tie!,Do you want to put',computer_roll+player_roll,'in the pot?')
            if utility.yes_or_no():
                self.pot=self.pot+computer_roll+player_roll

def question3():
	game = Boom()
	game.play()

question3()