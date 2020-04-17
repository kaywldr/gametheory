#from game import Game 
class Player:
	def __init__(self, player_type):
	
		self.player_type = player_type
		self.my_history = []
		self.opp_history = []
		self.payoff_list = []

	def action(self):
	
		#always cooperate
		if self.player_type == "AC":
			return 0;
		#always defect
		elif self.player_type == "AD":
			return 1
		#grudger
		elif self.player_type == "G":
			if len(self.opp_history)==0:
				return 0
			elif 1 in self.opp_history:
				return 1
			else:
				return 0
		#tit-for-tat
		elif self.player_type == "T4T":
			if len(self.opp_history) == 0:
				return 0
			else:
				#check if this is right syntax for last action in history
				return self.opp_history[-1]

	
	#need to figure out how to update history for opponent's action
	#def update(self, game):
		#self.payoff_list.append(payoff)
	#	self.my_history.append(action(self)) #basically append rhe most recent move
		#self.opp_history.append(self.action) #absically append your opponent's last move!
		#self.payoff_list.append(payoff) #append the payoff for the most recent game
