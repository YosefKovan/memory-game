from memory_game.game import play_game
from memory_game.io import player_init_input
from memory_game.init import game_init

if __name__ == "__main__":
   size = player_init_input()
   game_data = game_init(size)
   play_game(game_data)