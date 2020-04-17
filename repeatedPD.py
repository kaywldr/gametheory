import numpy as np 
import matplotlib.pyplot as plt  
import random
from player import Player
from game import Game
import itertools
from itertools import combinations
from collections import Counter
#cooperate = 0 
#defect = 1 


#payoffs = (((3,3), (0,5), (5,0), (1,1)))



#n = 100 #number of players initialized in generation 1

#p = 5 #% taken off lowest and readded for highest
#m = 3 #number of games per generation
#k = 2 #number of generations

#initialize new n players and create players of each player-type


#start with player 1 and player 2's player-type filled before implemeneting looping initialization


#use Random number generator in Python to generate number within the range from 0 to n
#divide the range into four pieces, each matching a type of player, then instantiate the player
player_list = []
new_game = Game(player_list)

#new_game.runGame(1, pairs_list)
		

#n = 100
#first generation
for i in range(25):
	new_game.player_list.append(Player("AC"))
    
for x in range(25):
	new_game.player_list.append(Player("AD"))
for y in range(25):
	new_game.player_list.append(Player("G"))
for z in range(25):
	new_game.player_list.append(Player("T4T"))
#print("*************************************************************************")
#for a in player_list:
#	print(a.player_type)
m=5
k=20
p=5
#num_gens = 1

for gen in range(1,k+1):

	pairs_list = []
	
	
	x = itertools.combinations(new_game.player_list,2)
	for i in x:
	#print(i)
		if i[0].player_type != i[1].player_type:
			pairs_list.append(i)
	
		#for x in self.pairs_list:
			#player1 = x[0] #how to access each element inside a pair
			#player2 = x[1]

	for pair in pairs_list:
		#print(str(pair[0].player_type) + " vs " + str(pair[1].player_type))

		player1, player2 = pair
		#print(pair.player1.player)
		#print(str(player1.player_type) + " vs " + str(player2.player_type))

		
		
		
		num_games = 0
		
		while num_games < m: 
			#have players pick next action and update history lists

			next_action_1 = player1.action()
			next_action_2 = player2.action()
			player1.my_history.append(next_action_1)
			player2.my_history.append(next_action_2)
			#player1.opp_history = player2.my_history
			#player2.opp_history = player1.my_history
			player1.opp_history.append(next_action_2)
			player2.opp_history.append(next_action_1)
			

			#determine payoffs for specific game and update payoff lists for both players

			if next_action_1==0 and next_action_2==0:
				player1.payoff_list.append(3)
				player2.payoff_list.append(3)
			elif next_action_1==0 and next_action_2==1:
				player1.payoff_list.append(0)
				player2.payoff_list.append(5)
			elif next_action_1==1 and next_action_2==0:
				player1.payoff_list.append(5)
				player2.payoff_list.append(0)
			elif next_action_1==1 and next_action_2==1:
				player1.payoff_list.append(1)
				player2.payoff_list.append(1)
			num_games+=1
		player1.opp_history = []
		player2.opp_history = []
			#print("----------------new game---------------------")
			#print(str(player1.player_type) + " vs. " + str(player2.player_type))
			#print("----Player 1----")
			#print("player 1 payoff: " + str(player1.payoff_list))
			#print("player 1 history list: " + str(player1.my_history))
			#print("player 1 opponent's history list: " + str(player1.opp_history))
			#print("----Player 2----")
			#print(player2.player_type)
			#print("player 2 payoff: " + str(player2.payoff_list))
			#print("player 2 history list: " + str(player2.my_history))
			#print("player 2 opponent's history list: " + str(player2.opp_history))
	sorted_player_list = sorted(player_list, key=lambda x: sum(x.payoff_list), reverse=True)
	#for player in sorted_player_list:
		#print("----new player----")
		#print("player type: " + str(player.player_type))
		#print("player payoff: " + str(player.payoff_list))
		#print("player history list: " + str(player.my_history))
		#print("player opponent's history list: " + str(player.opp_history))
		#print("cumulative payoff for given player " + str(sum(player.payoff_list)))
	AC_count = 0
	AD_count = 0
	G_count = 0
	T4T_count = 0
	cum_AC_payoff = 0
	cum_AD_payoff=0
	cum_G_payoff=0
	cum_T4T_payoff=0

	for player in sorted_player_list:
		if player.player_type=="AC":
			AC_count +=1
			cum_AC_payoff+=sum(player.payoff_list)
		if player.player_type=="AD":
			AD_count+=1
			cum_AD_payoff+=sum(player.payoff_list)
		if player.player_type=="G":
			G_count+=1
			cum_G_payoff+=sum(player.payoff_list)
		if player.player_type=="T4T":
			T4T_count+=1
			cum_T4T_payoff+=sum(player.payoff_list)
	total_payoff=cum_G_payoff + cum_AD_payoff + cum_AC_payoff + cum_T4T_payoff
	
	#for player in player_list:
		#	player.payoff_list = []
	
#AC_count = sorted_player_list.count(player.player_type="AC")
#AD_count = sorted_player_list.count(player.player_type="AD")
#G_count = sorted_player_list.count(player.player_type="G")
#T4T_count = sorted_player_list.count(player.player_type="T4T")
#print(AC_count)
#print(len(sorted_player_list))
#print(float(AC_count)/len(sorted_player_list))
	#print("wwwwwwwwwwwwwwwwwwwwwwwwwww")
	#print(len(sorted_player_list))
	#print(sorted_player_list)
	temp_list = sorted_player_list[:]
	percent_pop = float(p)*float(1.0/100.0)*float(len(sorted_player_list))
	#percent_pop = p*(1/100)*len(sorted_player_list)
	#print(percent_pop)
	for i in range(int(percent_pop)):
		sorted_player_list.pop(i)
		sorted_player_list.append(temp_list[i])
	#print(sorted_player_list)
	#print(len(sorted_player_list))
	player_list = sorted_player_list
	#for player in  player_list:
	#	del player.payoff_list[:]

	#for player in player_list:
			#player.payoff_list = []

	print("---------Gen " + str(gen) + "----------")
	print("***********Percentages************")
	print("AC percentage: " + str((float(AC_count) / len(sorted_player_list) * 100))+"%" )
	print("AD percentage: " + str((float(AD_count) / len(sorted_player_list) * 100))+"%" )
	print("G percentage: " + str((float(G_count) / len(sorted_player_list) * 100))+"%" )
	print("T4T percentage: " + str((float(T4T_count) / len(sorted_player_list) * 100))+"%" )
	print("***********Cumulative payoff************")
	print("AC cumulative payoff: " + str(cum_AC_payoff))
	print("AD cumulative payoff: " + str(cum_AD_payoff))
	print("G cumulative payoff: " + str(cum_G_payoff))
	print("T4T cumulative payoff: " + str(cum_T4T_payoff))
	print("total cumulative payoff: " + str(total_payoff))
	print("***********Averages************")
	print("AC average payoff: " + str(cum_AC_payoff/len(sorted_player_list)))
	print("AD average payoff: " + str(cum_AD_payoff/len(sorted_player_list)))
	print("G average payoff: " + str(cum_G_payoff/len(sorted_player_list)))
	print("T4T average payoff: " + str(cum_T4T_payoff/len(sorted_player_list)))
	for player in player_list:
		for x in range(len(player_list)):
			del player.payoff_list[:]



#proportion_AC = np.true_divide(cum_AC_payoff, total_payoff) * 100
#proportion_AD = np.true_divide(cum_AD_payoff, total_payoff) * 100
#proportion_G = np.true_divide(cum_G_payoff, total_payoff) * 100
#proportion_T4T = np.true_divide(cum_T4T_payoff, total_payoff) * 100

#plt.bar(ind, proportion_AC, width=0.8, label='AC score', color='gold', bottom=proportion_AD+proportion_G+proportion_T4T)
#plt.bar(ind, proportion_AD, width=0.8, label='AD score', color='silver', bottom=proportion_G+proportion_T4T)
#plt.bar(ind, proportion_G, width=0.8, label='G Score', color='#CD853F', bbottom=proportion_T4T)
#plt.bar(ind, proportion_T4T, width=0.8, label='T4T score', color='#000000')

#plt.xticks(ind, countries)
#plt.ylabel("Total Payoff")
#plt.xlabel("# Generations")
#plt.title("Question 1")
p#lt.ylim=1.0

# rotate axis labels
#plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

#plt.show()








