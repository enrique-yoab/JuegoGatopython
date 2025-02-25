import random

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