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

        new_aliens = []
        for a in self.aliens:
            if a.is_alive:
                new_aliens.append(a)
        self.aliens = new_aliens

        n = len(self.players)

        if n == 1:
            parasite_count = 2
            dominant_count = 1
        elif n == 2:
            parasite_count = 4
            dominant_count = 2
        elif n == 3:
            parasite_count = 6
            dominant_count = 2
        else:  
            parasite_count = 8
            dominant_count = 4

        
        if self.current_round % 5 == 0:
            for a in range(dominant_count):
                self.aliens.append(Dominant())
        
        elif self.current_round % 2 == 1:
            for a in range(parasite_count):
                self.aliens.append(Parasite())
    
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

    def handle_attack(self, player: Player):
        alive_aliens = []
        for a in self.aliens:
            if a.is_alive:
                alive_aliens.append(a)
        if not alive_aliens:
            print("Aucun extraterrestre à attaquer.")
            return

        damage_remaining = player.attack

        while damage_remaining > 0:
            new_aliens = []
            for a in self.aliens:
                if a.is_alive:
                    new_aliens.append(a)
            self.aliens = new_aliens
            if not self.aliens:
                print("Tous les aliens ont été éliminés!")
                break

            print("\nChoisissez une cible:")
            for i in range(len(self.aliens)):
                print(f"  {i+1}. {self.aliens[i].get_info()}")

            choice = -1
            while not 0 <= choice < len(self.aliens):
                try:
                    choice = int(input("Votre choix: ")) - 1
                    if not 0 <= choice < len(self.aliens):
                        print(f"Choix invalide. Choisissez entre 1 et {len(self.aliens)}")
                except ValueError:
                    print("Veuillez entrer un nombre valide")

            target = self.aliens[choice]
            hp_before = target.hp

            target.take_damage(damage_remaining)

            if not target.is_alive:
                surplus = damage_remaining - hp_before
                
                new_aliens = []
                for a in self.aliens:
                    if a.is_alive:
                        new_aliens.append(a)
                self.aliens = new_aliens
                if surplus > 0 and self.aliens:
                    print(f"💀 {target.name} éliminé! ({surplus} dégâts en surplus)")
                    print(f"⚡ Il vous reste {surplus} dégâts à distribuer!")
                else:
                    print(f"💀 {target.name} éliminé!")
                damage_remaining = surplus
            else:
                print(f"⚔️  {player.name} inflige {damage_remaining} dégâts à {target.name}! "
                        f"(HP restants: {target.hp}/{target.max_hp})")
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