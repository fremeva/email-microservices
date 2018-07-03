'''
SOLUCION #2
Hacer un algoritmo que realice el paseo del caballo en un tablero de ajedrez, indicando cualquier posicion del tablero.
__autor__ = Fredy Mendoza Vargas
'''


def set_initial_position():
    '''
    Función que obtiene del usuario la posicion inicial del tablero.
    :return: el numero de la fila y la columna (Tupla)
    '''
    i, j = -1, -1  # Inicializamos i, j con -1
    while (True):
        if (i == -1):
            i = int(input('Digite la posicion de la fila donde quiere iniciar (0-7): '))
        if (i < 0 or i > 7):
            print('El valor de la fila debe ser entre 0 y 7\n')
            i = -1
            continue
        else:
            j = int(input('Digite la posicion de la columna donde quiere iniciar (0-7): '))
            if (j < 0 or j > 7):
                print('El valor de la columna debe ser entre 0 y 7\n')
                continue
            else:
                break
    return i, j


def is_valid_range(x, y):
    '''
    Funcion que valida si las coordenadas x, y es del rango de la dimension del tablero
    :param x: Posicion de las fila
    :param y: Posicion de la columna
    :return: True or False
    '''
    return (x < 8 and x >= 0) and (y < 8 and y >= 0)


def is_empty(x, y, board):
    '''
    Funcion que verifica si la posicion del tablero[x][y] esta vacio
    :param x: Posicion de las fila
    :param y: Posicion de la columna
    :param board: Tablero 8x8
    :return: True or False
    '''
    return board[x][y] == 0


def output(tablero):
    for x in range(8):
        print(tablero[x])


def posibles_caminos(x, y, board):
    MOV = [[2, 1], [-2, -1], [1, 2], [-1, -2], [2, -1], [-2, 1], [1, -2], [-1, 2]]
    ways, cont = [], 0
    for mov in MOV:
        x2 = x + mov[0]
        y2 = y + mov[1]
        if is_valid_range(x2, y2) and is_empty(x2, y2, board):
            cont += 1
            ways.append([x2, y2])
    return ways, cont


def fill_board(board, row, colum, iterator=2):
    while (iterator <= 64):
        ways, total = posibles_caminos(row, colum, board)
        winner, tmp = ways[0], 0
        for index, way in enumerate(ways):
            sub_way, sub_total = posibles_caminos(way[0], way[1], board)
            if (index == 0):
                winner = way
                tmp = sub_total
            else:
                if (tmp > sub_total):
                    winner = way
                    tmp = sub_total
        row, colum = winner[0], winner[1]
        board[row][colum] = iterator
        iterator += 1


if __name__ == '__main__':
    board = [[0 for x in range(8)] for y in range(8)]  # Inicializamos el tablero con 0
    row, colum = set_initial_position()  # Capturamos la coordenada inicial
    board[row][colum] = 1  # Inicializamos con 1 en la posicion incial
    fill_board(board, row, colum)
    output(board)  # Imprimimos el tablero en consola
