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
            for j in range (len(classes)):
                print(f"\n{j+1}. {classes[j].name}")

            choice=-1
            while not 0<= choice <len(classes):
                try:
                    choice = int(input("Votre choix: ")) - 1
                    if not 0<= choice <len(classes):
                        print(f"Choix invalide. Choisissez un nombre entre 1 et {len(classes)}")
                except ValueError:
                    print(f"Veuillez entrer un nombre valide")

            player = Player(name, classes[choice])
            self.players.append(player)
            print(f"{player.name} ({player.player_class.name}) rejoint l'équipe!")
    
    def spawn_aliens(self):
        new_aliens=[]
        for alien in self.aliens:
            if alien.is_alive:
                new_aliens.append(alien)
        self.aliens = new_aliens
        num_parasites = min(1 + (self.current_round // 4),8)*len(self.players)
        num_dominants = min(max(0,(self.current_round-4)//4),4)*len(self.players)

        for i in range(num_parasites):
            self.aliens.append(Parasite())
        
        for i in range(num_dominants):
            self.aliens.append(Dominant())
    
    def display_status(self):
        print("\n" + "="*70)
        print("\n👥 EQUIPAGE:")
        for player in self.players:
            print(f"{player.get_info()}")
        print("\n👾 ALIENS:")
        for alien in self.aliens:
            if alien.is_alive:
                print(f"{alien.get_info()}")
        print("="*70)
        print(f"🚀 MANCHE {self.current_round}/{self.max_rounds} 🚀")
        print("="*70)
        print(f"\n {self.station.get_info_station()}")

    def player_turn(self, player: Player):
        if not player.is_alive:
            return
        
        print(f"\n🎮 Tour de {player.name}")
        print("Choisissez une action:")
        print("1. Ressources (améliorer une faculté)")
        print("2. Attaquer les extraterrestres")
        print("3. Réparer le mur")

        choice=""
        while choice not in("1","2","3"):
            choice = input("Votre choix (1-3): ")
            if choice not in("1","2","3"):
                print("Choix invalide. Entrez un nombre entre 1 et 3")

        if choice == "1":
            self.handle_resources(player)
        elif choice == "2":
            self.handle_attack(player)
        elif choice == "3":
            self.handle_repair(player)     

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
        print("\nChoissisez une amelioration:")
        print("1. Renforcer le mur")
        print("2. Perdre moins d'oxygene")
        print("3. Améliorer l'attaque")
        print("4. Améliorer la défense")

        choice=""
        while choice not in("1","2","3","4"):
            choice = input("Votre choix (1-4): ")
            if choice not in("1","2","3","4"):
                print("Choix invalide. Entrez un nombre entre 1 et 4")

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
        choice=-1
        while not 0<=choice<len(alive_aliens):
            try:
                choice=int(input("Votre choix:"))-1
                if not 0<=choice<len(alive_aliens):
                    print(f"Choix invalide. Choisissez un nombre entre 1 et {len(alive_aliens)}")
            except (ValueError, IndexError):
                print("Veuillez entrer un nombre valide")

        damage_remaining=player.attack
        target = alive_aliens[choice]
        while damage_remaining>0:
            overflow=target.hp
            target.take_damage(damage_remaining)

            if not target.is_alive:
                print(f"{target.name} éliminé!")
                damage_remaining=damage_remaining-overflow
                print(f"{target.name} éliminé!({damage_remaining} dégats en surplus)")
                new_aliens=[]
                for alien in self.aliens:
                    if alien.is_alive:
                        new_aliens.append(alien)
                self.aliens =new_aliens

                if damage_remaining>0 and self.aliens:
                    target=self.aliens[0]
                    print(f"Les dégats en surplus s'appliquent à {target.name}!")
                else:
                    break
            else:
                print(f"{player.name} mets {damage_remaining} dégâts à {target.name}!")
                break

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
        
        alive_aliens=[]
        for a in self.aliens:
            if a.is_alive:
                    alive_aliens.append(a)
        if not alive_aliens:
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
                alive_aliens=[]
                for a in self.aliens:
                    if a.is_alive:
                        alive_aliens.append(a)
                if not alive_aliens:
                    self.check_game_over()
                    return
        
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

        self.check_game_over()
    
    def start(self):
        print("\n" + "="*70)
        print("🚀 BIENVENUE DANS SPACE STATION SURVIVAL 🚀")
        print("="*70)
        print("\nVotre mission: Survivre pendant 15 manches et sauver la station!")
        print("Attention: Le mur et l'oxygène sont critiques pour votre survie.")
        input("\nAppuyez sur Entrée pour commencer...")

        while not self.game_over:
            self.play_round()
            if not self.game_over:
                input("\nAppuyez sur Entrée pour la prochaine manche...") 
        print("\n" + "="*70)
        print("📊 RÉSUMÉ FINAL")
        print("="*70)
        print(f"Manches survécues: {self.current_round}/{self.max_rounds}")
        print(f"{self.station.get_info_station()}")
        print("\nÉtat de l'équipage:")
        for player in self.players:
            print(f"{player.get_info()}")