class Space_Station:

    WALL_REINFORCEMENT=30 

    def __init__(self):
        self.wall_hp=100
        self.max_wall_hp=100
        self.oxygen_level=100
        self.oxygen_loss=5

    def reinforce_wall(self):
        self.wall_hp += self.WALL_REINFORCEMENT
        self.max_wall_hp += self.WALL_REINFORCEMENT

    def improve_oxygen(self):
        self.oxygen_loss=max(0,self.oxygen_loss-1)

    





