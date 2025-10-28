from memory_game.init import game_init
from memory_game.io import print_game_board, get_point_from_user, print_board_revealed, print_game_end, \
    player_init_input
import time

def player_won(game_data):

    for row_arr in game_data["revealed_board"]:
        if 'x' in row_arr:
            return False

    return True

def player_lost(game_data):
    return game_data["tries"] >= game_data["max_tries"]

def update_board(game_data, point1, point2):
    game_data["revealed_board"][point1[0]][point1[1]] = 'o'
    game_data["revealed_board"][point2[0]][point2[1]] = 'o'

def cards_are_equal(game_data, point1, point2):
    """this function will check if both cards are equal"""
    return game_data["hidden_board"][point1[0]][point1[1]] == game_data["hidden_board"][point2[0]][point2[1]]

def point_is_valid(point, game_data):
    return 0 <= point[0] < game_data["size"] and 0 <= point[1] < game_data["size"]

def player_choose(game_data):

    point = get_point_from_user()

    while not point_is_valid(point, game_data):
        print("the point you have chose is no valid try again!")
        point = get_point_from_user()

    return point

def game_round(game_data):

    print_game_board(game_data["hidden_board"], game_data["revealed_board"], game_data["size"])
    point1 = player_choose(game_data)
    point2 = player_choose(game_data)

    print_board_revealed(game_data, point1, point2)

    if cards_are_equal(game_data, point1, point2):
        print("You found a match, Congratulations!")
        update_board(game_data, point1, point2)
        game_data["steps"] += 1
    else:
        print("You did not find a match take a good look at the board before it disappears!")
        game_data["tries"] += 1
        time.sleep(5)

def play_game(game_data):

    while not player_won(game_data) or not player_lost(game_data):
        game_round(game_data)

    print_game_end(game_data, player_won(game_data))

def game_manager():

    game_over = False
    while not game_over:
        size = player_init_input()
        game_data = game_init(size, 10)
        play_game(game_data)







