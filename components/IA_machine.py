import random
from components.board_logic import *
def throw_random_machine(board,symbolM):
        while True:
            #la maquina escoge una posicion aleatorio
            renglon = random.randint(1,len(board))
            columna = random.randint(1,len(board[0]))
            #compara la posicion que ingreso si esta vacia
            if board[renglon-1][columna-1] == ' ':
                board[renglon-1][columna-1] = symbolM
                print(f"La maquina tiro [{renglon}][{columna}]")
                return board
            #si la posicion esta ocupada el bucle while se repite
def Block_Position(board, symbolM, symbolU):  # Método para bloquear al usuario
    N = len(board)
    M = len(board[0])

    # Verificar filas (horizontal)
    for row in range(N):
        for col in range(M - 2):
            valores = [board[row][col], board[row][col + 1], board[row][col + 2]]
            if valores.count(symbolU) == 2 and valores.count(' ') == 1:
                board[row][col + valores.index(' ')] = symbolM
                print(f"La maquina bloqueo en [{row+1}][{col+1+valores.index(' ')}]")
                return board

    # Verificar columnas (vertical)
    for col in range(M):
        for row in range(N - 2):
            valores = [board[row][col], board[row + 1][col], board[row + 2][col]]
            if valores.count(symbolU) == 2 and valores.count(' ') == 1:
                board[row + valores.index(' ')][col] = symbolM
                print(f"La maquina bloqueo en [{row+1+valores.index(' ')}][{col+1}]")
                return board

    # Verificar diagonales principales (\)
    for row in range(N - 2):
        for col in range(M - 2):
            valores = [board[row][col], board[row + 1][col + 1], board[row + 2][col + 2]]
            if valores.count(symbolU) == 2 and valores.count(' ') == 1:
                idx = valores.index(' ')
                board[row + idx][col + idx] = symbolM
                print(f"La maquina bloqueo en [{row+1+idx}][{col+1+idx}]")
                return board

    # Verificar diagonales secundarias (/)
    for row in range(2, N):
        for col in range(M - 2):
            valores = [board[row][col], board[row - 1][col + 1], board[row - 2][col + 2]]
            if valores.count(symbolU) == 2 and valores.count(' ') == 1:
                idx = valores.index(' ')
                board[row - idx][col + idx] = symbolM
                print(f"La maquina bloqueo en [{row+1-idx}][{col+1+idx}]")
                return board

    # Si no hay una jugada por bloquear, buscar una casilla vacía
    while True:
        #la maquina escoge una posicion aleatorio
        renglon = random.randint(1,len(board))
        columna = random.randint(1,len(board[0]))
        #compara la posicion que ingreso si esta vacia
        if board[renglon-1][columna-1] == ' ':
            board[renglon-1][columna-1] = symbolM
            print(f"La maquina tiro [{renglon}][{columna}]")
            return board
        #si no encuentra una posicion se repite el ciclo
        
def score(board, symbolU, symbolM, depth): ##calcula puntaje de la jugada
    if check_winner(board, symbolU, symbolM, depth) == 2:
        return 10 - depth
    elif check_winner(board, symbolM, symbolU, depth) == 1:
        return depth - 10
    else:
        return 0
    
def minimax(board, depth, symbolU, symbolM, turnPlayer):
    lenBoard = len(board[0])
    boardArray = [elemento for fila in board for elemento in fila]
    if check_winner(board,symbolU, symbolM, depth):
        return score(board, symbolU, symbolM, depth), None
    scores = []
    moves = []
    avaliblesMoves = [indice for indice,elemento in enumerate(boardArray) if elemento == ' ']
    for move in avaliblesMoves:
        possibleBoard = [fila[:] for fila in board]
        if turnPlayer:
            possibleBoard[move//lenBoard][move%lenBoard] = symbolU
        else:
            possibleBoard[move//lenBoard][move%lenBoard] = symbolM
        scores.append(minimax(possibleBoard, depth + 1, symbolU, symbolM, not turnPlayer)[0])
        moves.append(move)
    if turnPlayer:
        maxScoreIx = scores.index(max(scores))
        return scores[maxScoreIx], moves[maxScoreIx]
    else:
        minScoreIx = scores.index(min(scores))
        return scores[minScoreIx], moves[minScoreIx]
    
def throw_minimax_machine(board, depth, symbolU, symbolM, turnPlayer):
    #los sub arreglos se manejan como un arreglo de 2 x 2
    #para poder identificar las jugadas de 3
    sub_1 = div_board(board, 0, 0)
    sub_2 = div_board(board, 0, 1)
    sub_3 = div_board(board, 1, 0)
    sub_4 = div_board(board, 1, 1)

    moves = []
    scores = []

    for sub, (start_row, start_col) in zip([sub_1, sub_2, sub_3, sub_4], [(0, 0), (0, 1), (1, 0), (1, 1)]):
        score, move = minimax(sub, depth, symbolU, symbolM, turnPlayer)
        if move is not None:
            global_move = (start_row * 3 + move // 3, start_col * 3 + move % 3)
            scores.append(score)
            moves.append(global_move)

    # Escoger la mejor jugada según el turno
    if turnPlayer:
        best_move = moves[scores.index(max(scores))]
    else:
        best_move = moves[scores.index(min(scores))]

    # Aplicar la mejor jugada al tablero original
    boardP = [fila[:] for fila in board]
    boardP[best_move[0]][best_move[1]] = symbolM

    print(f"La máquina tiró en: {best_move[0]+1},{best_move[1]+1}")
    return boardP

def div_board(board, start_col, start_row):
    return [fila[start_col:start_col+3] for fila in board[start_row:start_row+3]]

        
    