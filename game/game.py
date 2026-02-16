from station.space_station import SpaceStation

class SpaceStationGame:
    def __init__ (self, num_player, max_rounds):
        self.station = SpaceStation() 
        self.player=[]
        self.aliens=[]
        self.current_round=0
        self.max_rounds=max_rounds
        self.game_over=False
        self.victory=False
        self._create_players(num_player)