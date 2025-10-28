from memory_game.io import print_game_board

def game_round(game_data):
    print_game_board(game_data)

def play_game(game_data):

    game_over = False
    while not game_over:
        game_round(game_data)




