class Alien :
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.is_alive = True

    def take_damage(self, damage):
        self.hp = self.hp - damage 

        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

    def get_info(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp}, ATK: {self.attack})"
    
class Parasite(Alien):
    count=0
    def __init__(self):
        Parasite.count+=1
        super().__init__(f"Parasite #{Parasite.count}", 20, 4)

class Dominant(Alien):
    count=0
    def __init__(self):
        Dominant.count+=1
        super().__init__(f"Dominant #{Dominant.count}", 60, 12)
