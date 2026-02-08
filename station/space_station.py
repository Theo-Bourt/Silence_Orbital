class Space_Station:

    WALL_REINFORCEMENT=30 

    def __init__(self):
        self.wall_hp=100
        self.max_wall_hp=100
        self.oxygen_level=100
        self.oxygen_loss=5

    def repair_wall(self):
        if "player" == "Engineer":
            self.wall_hp= self.wall_hp + 15
        else:
            self.wall_hp= self.wall_hp +10
    

    def damage_wall(self):
        self.wall_hp = self.wall_hp-4

    def reinforce_wall(self):
        self.wall_hp += self.WALL_REINFORCEMENT
        self.max_wall_hp += self.WALL_REINFORCEMENT

    def improve_oxygen(self):
        self.oxygen_loss=max(0,self.oxygen_loss-1)

    def loss_oxygen(self):
        self.oxygen_level = max(0,self.oxygen_level-self.oxygen_loss)

    def is_destroyed(self) -> bool:
        return self.wall_hp <=0 or self.oxygen_level <=0

    def get_info_station(self):
        return f"Mur: {self.wall_hp}/{self.max_wall_hp}\nOxygène: {self.oxygen_level}% (perte: -{self.oxygen_loss}% par tour) "

    





