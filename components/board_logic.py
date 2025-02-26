# Funciones que nos serviran para operar el tablero
def create_board(r, c):
    board = [[' ' for _ in range(c)] for _ in range(r)]
    return board


def show_board(board):
    """Muestra el tablero de juego con coordenadas."""
    for row in range(len(board)):
        print(" | ".join(board[row]))  # Une los elementos con "|"
        print("-" * (len(board[row]) * 4 - 1))  # Línea divisoria

    print("\nCoordenadas del tablero:")
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                print(f"X | ", end="")
            if board[row][col] == 'O':
                print(f"O | ", end="")
            if board[row][col] == ' ':
                print(f"[{row + 1}][{col + 1}] | ", end="")
        print("\n" + "-" * (len(board[0]) * 9 - 1))  # Línea divisoria ajustada


def check_board(row, col):
    if row < 3 or col < 3:
        print("El tablero no se creo")
        return False
    else:
        print("El tablero se creo")
        return True


def check_winner(board, symbolU, symbolM, cont):
    N = len(board)  # tamano del renglon
    M = len(board[0])  # tamano de la columna

    # verificamos los renglones, para identificar si hay N iguales
    for row in range(N):
        # este es el arreglo dinamico N x 1, si hay mas de N renglones se adelantara una posicion
        for col in range(M - 2):
            if all(board[row][col + i] == symbolU for i in range(3)):
                return 1
            if all(board[row][col + i] == symbolM for i in range(3)):
                return 2

    # verificamos las columnas, para identificar si hay M iguales
    for col in range(M):
        # este es el arreglo dinamico 1 x M, si hay mas de M columnas se adelantara una posicion
        for row in range(N - 2):
            if all(board[row + i][col] == symbolU for i in range(3)):
                return 1
            if all(board[row + i][col] == symbolM for i in range(3)):
                return 2

    # Verificamos las diagonales, de arriba hacia abajo
    for row in range(N - 2):
        for col in range(M - 2):
            if all(board[row + i][col + i] == symbolU for i in range(3)):
                return 1
            if all(board[row + i][col + i] == symbolM for i in range(3)):
                return 2

    # verificamos las diagonales, de abajo hacia arriba
    for row in range(2, N):
        for col in range(M - 2):
            if all(board[row - i][col + i] == symbolU for i in range(3)):
                return 1
            if all(board[row - i][col + i] == symbolM for i in range(3)):
                return 2

    # si el contador de tiros es igual a M x N entonces es un empate
    if cont == N * M:
        return 3
    # se retorna cero si aun no encuentra un ganador
    return 0
