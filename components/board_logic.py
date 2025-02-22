#Crea un tablero de tamaño NxN y lo retorna
def create_board(size):
    board = []
    empty = ' '
    for _ in range(size):
        temp = []
        for _ in range(size):
            temp.append(empty)
        board.append(temp)
    return board

#Verifica el ganador comparando un simbolo inicial en el tablero y retorna el simbolo ganador o caso contrario "None"
def check_winner(board):
    empty = ' '
    size=len(board)
    #Verificar filas
    for row in board:
        if all(cell==row[0] and cell!=empty for cell in row):
            return row[0]
    #Verificar columnas
    for col in range(size):
        column=[board[row][col] for row in range(size)]
        if all(cell == column[0] and cell!=empty for cell in column):
            return column[0]
    #Verificar diagonal principal (Arriba-Izquierda a Abajo-Derecha)
    main_diagonal=[board[i][i] for i in range(size)]
    if all(cell==main_diagonal[0] and cell!=empty for cell in main_diagonal):
        return main_diagonal[0]
    #Verificar diagonal secundaria (Arriba-Derecha a Abajo-Izquierda)
    inverse_diagonal=[board[i][size-1-i] for i in range(size)]
    if all(cell==inverse_diagonal[0] and cell!=empty for cell in inverse_diagonal):
        return inverse_diagonal[0]
    return None

def check_full(board):
    empty=' '
    for row in board:
        if ' ' in row:
            return False
    return True

#Imprime el estado del tablero
def print_board(board):
    for array in board:
        print(array)