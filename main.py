from game.game import *
if __name__ == "__main__":
    print("Combien de joueurs? (2-4 recommandé)")
    num_players = int(input("Nombre de joueurs: "))
    
    game = SpaceStationGame(num_players=num_players, max_rounds=15)
    game.start()