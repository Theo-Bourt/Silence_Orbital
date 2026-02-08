# test attaque et defense pour damage (entre player et alien)

from character.alien import Alien, Parasite
from character.player import *

# Création du joueur et de l'alien
player = Player("Lola", MEDIC)
alien = Parasite()

# Combat tour par tour
turn = 1
while player.is_alive and alien.is_alive:
    print(f"--- Tour {turn} ---")
    
    # Le joueur attaque l'alien
    dmg = alien.take_damage(player.attack)
    
    print(f"{player.name} attaque {alien.name} et inflige {player.attack} dégâts !")
    print(f"{alien.name} a maintenant {alien.hp}/{alien.max_hp} PV.\n")

    if not alien.is_alive:
        print(f"{alien.name} est mort ! {player.name} gagne !")
        break

    # L'alien attaque le joueur
    dmg_taken = player.take_damage(alien.attack)

    print(f"{alien.name} attaque {player.name} et inflige {dmg_taken} dégâts !")
    print(f"{player.name} a maintenant {player.hp}/{player.max_hp} PV.\n")

    if not player.is_alive:
        print(f"{player.name} est mort ! {alien.name} gagne !")
        break

    turn += 1



