import random
class player:
  def __init__(self, username):
    self.username = username
    self.score = 0
class match:
  def __init__(self, player1, player2, winner):
    self.player1 = player1
    self.player2 = player2
    self.winner = winner
class tournament:
  def __init__(self):
    self.players = {}
    self.matches = []
  def register_player(self,username):
    if username in self.players:
      print(f"{username} already registered.")
    else:
      self.players[username] = player(username)
      print(f"{username} registered.")
  def add_match_result(self, username1, username2, winner_name):
    if winner_name not in [username1, username2]:
      print("Winner must be one of the two players.")
      return 
    if username1 not in self.players or username2 not in self.players:
      print("Player(s) not registered.")
      return 
    
    winner = self.players[winner_name]
    winner.score+=3
    match = match(username1,username2,winner_name)
    self.matches.append(match)
    print(f"{username1} vs {username2} => {winner_name}")
  def display_leaderboard(self):
    sorted_players= sorted(self.players.values(),key=lambda p: (-p.score,p.username))
    for i, player in enumerate(sorted_players,1):
      print(f"{i}. {player.username} - {player.score}") 
  def simulate_Knockout(self, player_list=None, round_num=1):
    if player_list is None: 
      player_list= list(self.players.keys()) 
      if len(player_list)% 2 !=0:
        print("Even number of players required.")
        return 
    winners=[]
    for i in range(0, len(player_list),2):
      p1=player_list[i]
      p2=player_list[i+1]
      winner = random.choice([p1,p2])
      print(f"{p1} vs {p2} => {winner}")
      winners.append(winner)
      self.add_match_result(p1,p2,winner)
      if len(winners)==1:
        print(f"Champion: {winner[0]}")
        
