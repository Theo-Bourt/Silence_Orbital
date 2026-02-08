from character.alien import Parasite

class PlayerClass:
    def __init__(self, name, max_hp, attack, defense):
        self.name = name 
        self.max_hp = max_hp 
        self.attack = attack
        self.defense = defense
    
MEDIC = PlayerClass("MEDIC", max_hp=120, attack=8, defense=5)
ENGINEER = PlayerClass("ENGINEER", max_hp=100, attack=10, defense=6)
SOLDIER = PlayerClass("SOLDIER", max_hp=150, attack=12, defense=7)


class Player():
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
    
    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
