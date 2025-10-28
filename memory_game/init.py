from memory_game.board import create_revealed_matrix, create_shuffled_matrix

def game_init(size, max_tries):

    game_gdata = {
        "hidden_board" :  create_shuffled_matrix(size),
        "revealed_board" : create_revealed_matrix(size),
        "size" : size,
        "revealed" : 0,
        "max_tries" : max_tries,
        "tries" : 0,
        "steps" : 0
    }

    return game_gdata