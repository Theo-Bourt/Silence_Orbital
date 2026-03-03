from game.game import *
if __name__ == "__main__":
    print("Combien de joueurs? (Entre 1 et 4)")
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