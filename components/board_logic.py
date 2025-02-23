#Funciones que nos serviran para operar el tablero
def create_board(r,c):
    board = [[' 'for _ in range(c)] for _ in range(r)]
    return board

def show_board(board):
    """Muestra el tablero de juego."""
    for row in board:
        print(" | ".join(row)) # imprime la lista de fila, uniendo sus elementos con "|"
        print("-" * (len(row)*4-1)) # crea una linea de "-" para separar las filas.

def check_board(row, col):
    if row < 3 or col < 3:
        print("El tablero no se creo")
        return False
    else :
        print("El tablero se creo")
        return True   

def check_winner(board, symbolU, symbolM, cont):
    N = len(board)     #tamano del renglon
    M = len(board[0])  #tamano de la columna
    
    #verificamos los renglones, para identificar si hay 3 iguales
    for row in range(N):
        #este es el arreglo dinamico 3 x 3, si hay mas de 3 columnas se adelantara una a la derecha
        for col in range(M-2):
            if all(board[row][col+i] == symbolU for i in range(3)):
                return 1
            if all(board[row][col+i] == symbolM for i in range(3)):
                return 2
            
    #verificamos las columnas, para identificar si hay 3 iguales
    for col in range(M):
        #este es el arreglo dinamico 3 x 3, si hay mas de 3 renglones se adelantara una a la derecha
        for row in range(N-2):
            if all(board[row+i][col] == symbolU for i in range(3)):
                return 1
            if all(board[row+i][col] == symbolM for i in range(3)):
                return 2
            
    #Verificamos las diagonales, de arriba hacia abajo
    for row in range(N-2):
        for col in range(M-2):
            if all(board[row+i][col+i] == symbolU for i in range(3)):
                return 1
            if all(board[row+i][col+i] == symbolM for i in range(3)):
                return 2
            
    #verificamos las diagonales, de abajo hacia arriba
    for row in range(2, N):
        for col in range(M-2):
            if all(board[row-i][col+i] == symbolU for i in range(3)):
                return 1
            if all(board[row-i][col+i] == symbolM for i in range(3)):
                return 2
    
    #si el contador de tiros es igual a M x N entonces es un empate
    if cont == N*M:
        return 3
    #se retorna sero si aun no encuentra un ganador
    return 0