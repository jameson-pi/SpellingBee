import random
class players:
    def __init__(self,names):
        names1={}
        for name in names:
            names1[name] = [0,0]
        self.names = names1
        
    def add_win(self,player):
        self.names[player][0]+=1
    def add_lose(self,player):
        self.names[player][1]+=1
    def wins(self):
        for name in self.names:
            
firstGame=players(["Jameson"])
firstGame.add_win("Jameson")
firstGame.wins()