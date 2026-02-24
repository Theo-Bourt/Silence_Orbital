from station.space_station import SpaceStation
from character.player import *
from character.alien import *
class Game:
    def __init__(self):
        self.station= SpaceStation
        self.player=[]
        self.aliens=[]
        self.curent_rounds=0

    def handle_resourses(self, player):
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

