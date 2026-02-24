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

            


































def _handle_attack(self, player: Player):
    """Gère l'action Attaque"""
    alive_aliens = [a for a in self.aliens if a.is_alive]

    if not alive_aliens:
        print("❌ Aucun extraterrestre à attaquer!")
        return

    print("\nChoisissez une cible:")
    for i, alien in enumerate(alive_aliens, 1):
        print(f"{i}. {alien}")

    try:
        target = alive_aliens[int(input("Votre choix: ")) - 1]
    except (ValueError, IndexError):
        print("❌ Cible invalide!")
        return

    damage = player.attack_alien(target)
    print(f"💥 {player.name} inflige {damage} dégâts à {target.name}!")

    if not target.is_alive:
        print(f"☠️ {target.name} éliminé!")