
from character.player import *
class SpaceStation: 

    def init(self):
        self.wall_hp=100
        self.max_wall_hp=100
        self.oxygen_level=100
        self.oxygen_loss=5

    def repair_wall(self):
        if PlayerClass == ENGINEER:
            self.wall_hp= self.wall_hp + 15
        else:
            self.wall_hp= self.wall_hp +10

    def damage_wall(self,damage):
        self.wall_hp = max(0,self.wall_hp-damage)

    def reinforce_wall(self,amount):
        self.wall_hp += amount
        self.max_wall_hp += amount

    def improve_oxygen(self, reduction):
        self.oxygen_loss=max(0,self.oxygen_loss-reduction)

    def loss_oxygen(self):
        self.oxygen_level = max(0,self.oxygen_level-self.oxygen_loss)

    def is_destroyed(self) -> bool:
        return self.wall_hp <=0 or self.oxygen_level <=0

    def get_info_station(self):
        return f"Mur: {self.wall_hp}/{self.max_wall_hp}\nOxygène: {self.oxygen_level}% (perte: -{self.oxygen_loss}% par tour) "


    





