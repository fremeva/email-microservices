'''
Algoritmo de torres de hanoi
__autor__ "Fredy Mendoza"
'''
def set_n_disk():
    n = 0
    while (True):
        n = int(input('Digite el numero de discos: '))
        if (n > 0):
            break
        else:
            print('\n\tEL numero de disco debe ser mayor que 0\n')
    return n


def output_hanoi(board):
    for torre in range(3):
        print('Torre {} ---> {}'.format(torre + 1, board[torre]))
    print('-' * 40)


def hanoi(board, n, ti=0, taux=1, tf=2):
    if (n == 1):
        board[tf].append(board[ti].pop())
        output_hanoi(board)
    else:
        hanoi(board, n - 1, ti, tf, taux)
        board[tf].append(board[ti].pop())
        output_hanoi(board)
        hanoi(board, n - 1, taux, ti, tf)


if __name__ == '__main__':
    n = set_n_disk()
    board = [[x for x in reversed(range(1, (n + 1)))], [], []]
    print('*' * 20)
    output_hanoi(board)
    print('*' * 20)
    hanoi(board, n)
