#TIC TAC TOE
board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')

def winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

def dfs(player):
    if winner():
        return winner()

    if ' ' not in board:
        return 'Draw'

    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            result = dfs('O' if player == 'X' else 'X')
            board[i] = ' '

            if result == player:
                return player

    return 'Draw'

print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    # User move
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position! Try again.")
        continue

    board[pos] = 'X'

    if winner():
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break

    # Machine move using DFS
    best = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            result = dfs('X')
            board[i] = ' '

            if result == 'O':
                best = i
                break

    if best == -1:
        best = board.index(' ')

    board[best] = 'O'
    print("Machine's move:")
    display()

    if winner():
        print("Machine wins!")
        break

    if ' ' not in board:
        print("Draw!")
        break