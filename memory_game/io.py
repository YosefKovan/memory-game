
def player_init_input():

    while True:
        try:
            user_input = int(input("please input a even number: "))
            if user_input % 2 == 0:
                return user_input

            print("make sure to input a valid number!")

        except:
           print("Please make sure to input a even digit only!")


def print_reveal(hidden_matrix, revealed_matrix, location):
    pass


def print_game_board(hidden_matrix, revealed_matrix, size):

    for row in range(size):
        for col in range(size):
            if revealed_matrix[row][col] == 'o':
                print('o', end=" ")
            else:
                print(hidden_matrix[row][col], end=" ")
        print(sep="")