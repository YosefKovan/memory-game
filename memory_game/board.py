import random

def get_random_point(size):
    row = random.randrange(size)
    col = random.randrange(size)
    return row, col


def shuffle_matrix(matrix, size):

    max_shuffle = 10000

    while max_shuffle > 0:
        row1, col1 = get_random_point(size)
        row2, col2 = get_random_point(size)

        if row1 == row1 or col1 == col2:
           continue

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]


def create_hidden_matrix(size):

    #this will return a list of all the numbers
    all_characters = [i for i in range(size**2 // 2)]




def create_revealed_matrix(size):
    return [['o' for col in range(size)] for row in range(size)]

