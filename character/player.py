class PlayerClass:
    def __init__(self, name, max_hp, attack, defense):
        self.name = name 
        self.max_hp = max_hp 
        self.attack = attack
        self.defense = defense
    
MEDIC = PlayerClass("MEDIC", max_hp=120, attack=8, defense=5)
ENGINEER = PlayerClass("ENGINEER", max_hp=100, attack=10, defense=6)
SOLDIER = PlayerClass("SOLDIER", max_hp=150, attack=12, defense=7)


class Player:
    def __init__(self, name, player_class):
        self.name = name 
        self.player_class = player_class
        self.max_hp = player_class.max_hp
        self.hp = self.max_hp
        self.attack = player_class.attack
        self.defense = player_class.defense
        self.oxygen = 100 
        self.is_alive = True 
    
    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp = self.hp - actual_damage

        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        
        return actual_damage
    

    def oxygen_damage(self):

        damage = 0
        if self.hp < 25:
            damage = 10
        elif self.hp < 50:
            damage = 5
        elif self.hp < 75:
            damage = 3
        
        if damage > 0:
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                self.is_alive = False 
        
        return damage 
    
    def attack_alien(self, alien):
        damage = self.attack
        alien.take_damage(damage)
        return damage

    def repair_wall(self, station):
        if self.player_class == ENGINEER:
            amount = 15
        else:
            amount = 10
        station.wall_hp = min(station.max_wall_hp, station.wall_hp + amount)
        return amount 

    def upgrade_attack(self):
        self.attack += 3
    
    def upgrade_defense(self): 
        self.defense += 5
    
    def get_info(self):
        status = "✅" if self.is_alive else "💀"

        return f"{status} {self.name} ({self.player_class.name}) - HP: {self.hp}/{self.max_hp} | ATK: {self.attack} | DEF: {self.defense}"