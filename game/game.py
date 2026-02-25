from station.space_station import *
from character.player import *
from character.alien import *
import random

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

    def create_player(self, num_player):
        classes = [PlayerClass.MEDIC, PlayerClass.ENGINEER, PlayerClass.SOLDIER]

        for i in range(num_player):
            name = input(f"\nNom du joueur {i+1}: ")
            print("\nChoisissez une classe:")

            for idx, cls in enumerate(classes, 1):
                print(f"\n{idx}. {cls.value}")
            choice = int(input("Votre choix")) - 1
            player = Player(name, classes[choice])
            self.player.append(player)
            print(f"{player.name} ({player.player_class.value}) rejoint l'équipe!")
    
    def spawn_aliens(self):
        num_parasites = 2 + (self.current_round // 3)
        num_dominants = max(0, (self.current_round - 5) // 2)

        for i in range(num_parasites):
            self.aliens.append(Parasite())
        
        for i in range(num_dominants):
            self.aliens.append(Dominant())
    
    def display_status(self):
        print("\n" + "="*70)
        print(f"🚀 MANCHE {self.current_round}/{self.max_rounds} 🚀")
        print("="*70)
        print(f"\n {self.station}")
        print("\n👥 EQUIPAGE:")
        for alien in self.aliens:
            print(f" {alien}")
        print("="*70)

    def player_turn(self, player: Player):
        if not player.is_alive:
            return
        
        print(f"\n🎮 Tour de {player.name}")
        print("Choisissez une action:")
        print("1. Ressources (améliorer une faculté)")
        print("2. Attaquer les extraterrestres")
        print("3. Réparer le mur")

        choice = input("Votre choix (1-3): ")

        if choice == "1":
            pass
        elif choice == "2":
            pass 
        elif choice == "3":
            pass 
        else:
            print("Choix invalide, tour perdu!")

    def aliens_attack(self):
        if not self.aliens:
            return
        
        print("\n👾 PHASE D'ATTAQUE EXTRATERRESTRE")

        alive_aliens = []

        for i in self.aliens:
            if i.is_alive:
                alive_aliens.append(i)
        
        for alien in alive_aliens:
            if random.random() < 0.6:
                damage = alien.attack
                self.station.damage_wall(damage)
                print(f"💥 {alien.name} attaque le mur! (-{damage} PV)")
            else:
                alive_players = []
                for i in self.player:
                    if i.is_alive:
                        alive_players.append(i)
            
            if alive_players:
                target = random.choice(alive_players)
                damage = target.take_damage(alien.attack)
                print(f"💥 {alien.name} attaque {target.name}! (-{damage} HP)")
                if not target.is_alive:
                    print(f"☠️ {target.name} est mort!")