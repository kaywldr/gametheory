from player import Player 
import itertools
from itertools import combinations
class Game:
	def __init__(self, player_list):
		#self.player1 = player1
		#self.player2 = player2
		self.player_list =player_list

		#self.pairs_list = pairs_list
		#self.payoff = payoff
		
	#could call run_games
	def runGame(self, m, pairs_list):
		num_games=0

		#self.m = m
		#pairs_list = []
	

		while num_games < m: 
			#have players pick next action and update history lists
			next_action_1 = self.player1.action()
			next_action_2 = self.player2.action()
			self.player1.my_history.append(next_action_1)
			self.player2.my_history.append(next_action_2)
			self.player1.opp_history.append(next_action_2)
			self.player2.opp_history.append(next_action_1)
			

			#determine payoffs for specific game and update payoff lists for both players

			if next_action_1==0 and next_action_2==0:
				self.player1.payoff_list.append(3)
				self.player2.payoff_list.append(3)
			elif next_action_1==0 and next_action_2==1:
				self.player1.payoff_list.append(0)
				self.player2.payoff_list.append(5)
			elif next_action_1==1 and next_action_2==0:
				self.player1.payoff_list.append(5)
				self.player2.payoff_list.append(0)
			elif next_action_1==1 and next_action_2==1:
				self.player1.payoff_list.append(1)
				self.player2.payoff_list.append(1)

			num_games+=1

	def addPlayer(self, player, player_type):
		self.player_list.append(player)
		return self.player_list

   # def create_Player(player_type, my_history, opp_history):
	#	new_player = Player()
	#	new_player.player_type = player_type
		#new_player.my_history = my_history
		#new_player.opp_history = opp_history
		#return new_player

	def print_results(self):
		#print results of game for each generation
		print("----Player 1----")
		#print("player 1 payoff: " + str(self.player1.payoff_list))
		#print("player 1 history list: " + str(self.player1.my_history))
		#print("player 1 opponent's history list: " + str(self.player1.opp_history))
		print("----Player 2----")
		#print("player 2 payoff: " + str(self.player2.payoff_list))
		#print("player 2 history list: " + str(self.player2.my_history))
		#print("player 2 opponent's history list: " + str(self.player2.opp_history))


	