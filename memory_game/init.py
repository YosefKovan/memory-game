from memory_game.board import create_revealed_matrix, create_shuffled_matrix

def game_init(size):



    game_gdata = {
        "hidden_board" :  create_shuffled_matrix(size),
        "revealed_board" : create_revealed_matrix(size),
        "size" : size
    }

    return game_gdata