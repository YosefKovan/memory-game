

def player_init_input():

    while True:
        try:
            user_input = int(input("please input a even number: "))
            if user_input % 2 == 0:
                return user_input

            print("make sure to input a valid number!")

        except:
           print("Please make sure to input a even digit only!")

def get_point_from_user():

    while True:
        try:
            user_input = input("Please enter two valid integers: ").split(' ')
            if len(user_input) != 2:
                print("Enter exactly two numbers!!!")
                continue

            row, col = int(user_input[0]), int(user_input[1])
            return row, col

        except:
            print("Make sure to enter two valid integers!!!")

def print_board_revealed(game_data, point1, point2):

    for row in range(game_data["size"]):
        for col in range(game_data["size"]):
            if row == point1[0] and col == point1[1] or row == point2[0] and col == point2[1]:
                print(f"{game_data["hidden_board"][row][col]} ", end="")
            else:
                print(f"{game_data["revealed_board"][row][col]} ", end="")

        print(sep="")

def print_game_board(hidden_matrix, revealed_matrix, size):

    for row in range(size):
        for col in range(size):
            if revealed_matrix[row][col] == 'x':
                print('x ', end=" ")
            else:
                print(hidden_matrix[row][col], end=" ")

        print(sep="")

def print_game_end(game_data, player_won):

    if player_won:
        print(f"Congrats you finished")
    else:
        print("Too many tries play another game or try later!")
