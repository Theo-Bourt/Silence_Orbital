from game.game import *
import time
import msvcrt


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 BIENVENUE DANS SPACE STATION SURVIVAL 🚀")
    print("="*70)
    print("(Appuyez sur Entree pour passer l'introduction)")

    texte = "\nLa station s’est fait envahir par des extraterrestres ! Ils sont entrés par le côté Sud de la base, vous avez enclenché une porte de sécurité qui vous sépare d’eux. Vous êtes donc en sûreté, enfin pour le moment … \n \nLa terre a été prévenue et à immédiatement envoyer une équipe vous sauver. Seulement, étant donné que la station se trouve à des milliers de kilomètres, il va falloir survivre 15 jours au sein de la station spatiale. \n \nLe jeu :\n     -	Vous allez devoir aller tuer des extraterrestres afin d’éviter qu’ils ne se propagent encore plus mais faites attention à votre santé.\n     -	Veillez à ce que la porte qui vous sépare des aliens reste en bon état. Si jamais elle venait à se casser, la station ne supporterait pas la différence de pression et exploserait.\n     -	Le vaisseau ennemi a endommagé les systèmes d’oxygène. L’air dans la station diminue, il vous faut donc limiter ce problème avant d’arriver à cours.\n \nDans l’espace, tout effort est plus dur et prend beaucoup plus de temps que sur terre. A chaque jour passé, vous allez pouvoir vous réaliser une de ces tâches :\n       -	Ressources :\n             o	Améliorer l’attaque\n             o	Améliorer la défense\n             o	Améliorer le soin passif (repos)\n             o	Limiter la perte d’oxygène\n             o	Renforcer la porte de sécurité\n     -	Attaquer les extraterrestres \n     -	Réparer le mur\n     -	Se soigner (repos)\n \nBonne chance et bon courage !\n"
    skip=False
    for i, lettre in enumerate(texte):
        if msvcrt.kbhit():
            while msvcrt.kbhit():
                msvcrt.getwch()
            skip=True
            break
        print(lettre, end="", flush=True) 
        time.sleep(0.05)
   
    if skip:
        print(texte[i:], flush=True)
    time.sleep(3)
        
    print("\nCombien de joueurs? (Entre 1 et 4)")
    num_players=-1
    while not 1<= num_players<=4:
        try:
            num_players = int(input("Nombre de joueurs: "))
            if not 1<=num_players<=4:
                print("Veuillez entrer un nombre entre 1 et 4")
        except ValueError:
            print("Veuillez entrer un nombre valide")
    game = SpaceStationGame(num_players=num_players, max_rounds=15)
    game.start()    