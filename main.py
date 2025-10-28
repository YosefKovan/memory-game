from memory_game.board import create_hidden_matrix, shuffle_matrix

if __name__ == "__main__":
   matrix = create_hidden_matrix(20)
   matrix = shuffle_matrix(matrix, 20)
   print(matrix)