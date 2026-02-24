from station.space_station import SpaceStation
from character.player import *
from character.alien import *
class Game:
    def __init__(self):
        self.station= SpaceStation
        self.player=[]
        self.aliens=[]
        self.curent_rounds=0

    def handle_resourses(self, player:Player):
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
            print(f"Système amélioré! Perte d'oxygene réduite à {self.station.loss_oxygen} par tour")
        elif choice=="3":
            player.upgrade_attack()
            print(f"Attaque augmentée! Nouvelle attaque : {player.attack}")
        elif choice =="4":
            player.upgrade_defense()
            print(f"Défense augmentée ! Nouvelle défense: {player.defense}")
        else:
            print("Choix invalide!")

    def handle_attack(self, player:Player):
        alive_aliens= [a for a in self.aliens if a.is_alive]
        if not alive_aliens:
            print("Aucun extraterrestre à attaquer")
            return
        
        print("Choisissez unz cible:")
        for i in alive_aliens:
            print(f"{i}.{alive_aliens}")
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
        
        if not any(p.is_alive for p in self.player):
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
        for player in self.player:
            if player.is_alive:
                self.player_turn(player)
        self.aliens_attack()

        self.station.loss_oxygen()
        print(f"L'ocygen diminue. Niveau actuel:{self.station.oxygen_level}%")

        if self.station.oxygen_level<50:
            print("ALERTE OXYGENE BAS!")
            for player in self.player:
                if player.is_alive:
                    damage = player.oxygen_damage()
                    if damage>0:
                        print(f"{player.name} perd {damage} HP à cause du manque d'oxygène!")

        self.aliens = [a for a in self.aliens if a.is_alive]

        return self.check_game_over()
