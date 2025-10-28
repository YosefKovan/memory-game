import random

def get_random_point(size):
    row = random.randrange(size)
    col = random.randrange(size)
    return row, col

def shuffle_matrix(matrix, size):

    max_shuffle = 1000

    while max_shuffle > 0:

        row1, col1 = get_random_point(size)
        row2, col2 = get_random_point(size)

        if row1 == row2 and col1 == col2:
            continue

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        max_shuffle -= 1

    return matrix

def create_hidden_matrix(size):
    """this will create a matrix will all the hidden numbers"""

    #this will return a list of all the numbers
    all_characters = [i for i in range(size**2 // 2)] * 2

    matrix = []

    for i in range(size):
        arr = []
        for j in range(size):
            arr.append(all_characters[i*size + j])
        matrix.append(arr)

    return matrix

def create_revealed_matrix(size):
    """this will create the revealed matrix"""
    return [['o' for col in range(size)] for row in range(size)]

def create_shuffled_matrix(size):
    return shuffle_matrix(create_hidden_matrix(size), size)