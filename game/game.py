from station.space_station import *
from character.player import *
from character.alien import *
import random

class SpaceStationGame:
    def __init__ (self, num_players, max_rounds):
        self.station = SpaceStation() 
        self.players=[]
        self.aliens=[]
        self.current_round=0
        self.max_rounds=max_rounds
        self.game_over=False
        self.victory=False
        self.create_players(num_players)

    def create_players(self, num_players):
        classes = [MEDIC, ENGINEER, SOLDIER]

        for i in range(num_players):
            name = input(f"\nNom du joueur {i+1}: ")
            print("\nChoisissez une classe:")

            for j, _classes_ in enumerate(classes, 1):
                print(f"\n{j}. {_classes_.name}")

            choice = int(input("Votre choix: ")) - 1
            player = Player(name, classes[choice])
            self.players.append(player)
            print(f"{player.name} ({player.player_class.name}) rejoint l'équipe!")
    
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
        print(f"\n {self.station.get_info_station()}")
        print("\n👥 EQUIPAGE:")
        for player in self.players:
            print(f"{player.get_info()}")
        print("\n👾 ALIENS:")
        for alien in self.aliens:
            if alien.is_alive:
                print(f"{alien.get_info()}")
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
            self.handle_resources(player)
        elif choice == "2":
            self.handle_attack(player)
        elif choice == "3":
            self.handle_repair(player)
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
                for i in self.players:
                    if i.is_alive:
                        alive_players.append(i)   
                if alive_players:
                    target = random.choice(alive_players)
                    damage = target.take_damage(alien.attack)
                    print(f"💥 {alien.name} attaque {target.name}! (-{damage} HP)")
                    if not target.is_alive:
                        print(f"☠️ {target.name} est mort!")
                        alive_players.remove(target)

    def handle_resources(self, player:Player):
        print("Choissisez une amelioration:")
        print("1. Renforcer le mur")
        print("2. Perdre moins d'oxygene")
        print("3. Améliorer l'attaque")
        print("4. Améliorer la défense")
        choice=input("Votre choix (1-4)")

        if choice=="1":
            self.station.reinforce_wall(30)
            print(f"Mur renforcé! Nouveau maximum: {self.station.max_wall_hp}")
        elif choice =="2":
            self.station.improve_oxygen(1)
            print(f"Système amélioré! Perte d'oxygene réduite à {self.station.oxygen_loss} par tour")
        elif choice=="3":
            player.upgrade_attack()
            print(f"Attaque augmentée! Nouvelle attaque : {player.attack}")
        elif choice =="4":
            player.upgrade_defense()
            print(f"Défense augmentée ! Nouvelle défense: {player.defense}")
        else:
            print("Choix invalide!")

    def handle_attack(self, player:Player):
        alive_aliens = []
        for i in self.aliens:
            if i.is_alive:
                alive_aliens.append(i)
        if not alive_aliens:
            print("Aucun extraterrestre à attaquer")
            return
        
        print("Choisissez une cible:")
        for i in range(len(alive_aliens)):
            print(f"{i+1}.{alive_aliens[i].get_info()}")
        try:
            choice=int(input("Votre choix:"))-1
            target = alive_aliens[choice]
            damage = player.attack_alien(target)
            print(f"{player.name} mets {damage} dégâts à {target.name}!")
            if not target.is_alive:
                print(f"{target.name} éliminé!")
        except (ValueError, IndexError):
            print("Cible invalide!")

    def handle_repair(self,player:Player):
        amount = player.repair_wall(self.station)
        print(f"{player.name} répare le mur de {amount} PV!")
        print(f"Mur: {self.station.wall_hp}/{self.station.max_wall_hp}")

    def check_game_over(self):
        if self.station.is_destroyed():
            self.game_over=True
            self.victory=False
            print("GAME OVER! La station a été détruite!")
            return True
        
        alive_players = []
        for i in self.players:
            if i.is_alive:
                alive_players.append(i)
        if not alive_players:
            self.game_over=True
            self.victory=False
            print("GAME OVER! Tout l'equipage est mort!")
            return True
        
        if self.current_round >= self.max_rounds:
            self.game_over=True
            self.victory=True
            print("VICTOIRE! Vous avez survécu et sauvé la station!")
            return True
        
        if not any(a.is_alive for a in self.aliens):
            self.game_over=True
            self.victory=True
            print("VICTOIRE! Vous avez tué tous les aliens!")
            return True
        
        return False
    

    def play_round(self):

        self.current_round += 1
        self.spawn_aliens()
        self.display_status()

        for player in self.players:
            if player.is_alive:
                self.player_turn(player)
        
        self.aliens_attack()
        self.station.loss_oxygen()
        print(f"\n L'oxygène diminue... Niveau actuel: {self.station.oxygen_level}%")

        if self.station.oxygen_level < 50:
            print("ALERTE OXYGENE BAS!")
            for player in self.players:
                if player.is_alive:
                    damage = player.oxygen_damage()
                    if damage > 0:
                        print(f"{player.name} perd {damage} HP à cause du manque d'oxygène!")
        
        new_aliens = []

        for alien in self.aliens:
            if alien.is_alive:
                new_aliens.append(alien)

        self.aliens = new_aliens

        return self.check_game_over()
    
    def start(self):
        print("\n" + "="*70)
        print("🚀 BIENVENUE DANS SPACE STATION SURVIVAL 🚀")
        print("="*70)
        print("\nVotre mission: Survivre pendant 15 manches et sauver la station!")
        print("Attention: Le mur et l'oxygène sont critiques pour votre survie.")
        input("\nAppuyez sur Entrée pour commencer...")

        while not self.game_over:
            game_over = self.play_round()
            if not game_over:
                input("\nAppuyez sur Entrée pour la prochaine manche...") 
        print("\n" + "="*70)
        print("📊 RÉSUMÉ FINAL")
        print("="*70)
        print(f"Manches survécues: {self.current_round}/{self.max_rounds}")
        print(f"{self.station.get_info_station()}")
        print("\nÉtat de l'équipage:")
        for player in self.players:
            print(f"{player.get_info_station()}")