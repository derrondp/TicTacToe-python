from random import choice

board = list(' ' for x in range(10))


def printboard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def select(board):
    from random import choice
    return choice(board)


def isSpaceFree(board, position):
    return board[position] == ' '


def isboardFull(board):
    return not board.count(' ') > 1


def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (
            board[4] == letter and board[5] == letter and board[6] == letter) or (
            board[7] == letter and board[8] == letter and board[9] == letter) or (
            board[1] == letter and board[5] == letter and board[9] == letter) or (
            board[3] == letter and board[5] == letter and board[7] == letter) or (
            board[1] == letter and board[4] == letter and board[7] == letter) or (
            board[2] == letter and board[5] == letter and board[8] == letter) or (
            board[3] == letter and board[6] == letter and board[9] == letter)


def insertLetter(position, letter):
    board[position] = letter


def playermove():
    run = True

    while run:
        position = input("Enter a position to place an \'X\': ")
        try:
            position = int(position)
            if 0 < position < 10:
                if isSpaceFree(board, position):
                    run = False
                    insertLetter(position, 'X')
                else:
                    print("Sorry! This space has been occupied")
            else:
                print("Enter a valid integer between the range (0-10)")
        except:
            print("Please input an integer!")


def computermove():
    available_moves = [x for x, letter in enumerate(board) if x != 0 and letter == ' ']
    
    move = 0

    for letter in ['X', 'O']:
        for i in available_moves:
            copy = board[:]
            copy[i] = letter
            if isWinner(copy, letter):
                move = i
                return move
    
    corners = []
    for i in available_moves:
        if i in [1, 3, 7, 9]:
            corners.append(i)
    
    if len(corners) > 1:
        return select(corners)
    
    edges = []
    for i in available_moves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    
    if len(edges) > 1:
        return select(edges)

    if 5 in available_moves:
        move = 5
        return move
    
    return move


def main():
    print("WELCOME TO TIC TAC TOE")
    printboard(board)

    while not isboardFull(board):
        if not isWinner(board, 'O'):
            playermove()
            printboard(board)
        else:
            print("Sorry \'O\'s won this time!")
            break
        
        if not isWinner(board, 'X'):
            position = computermove()
            if position == 0:
                print("Tie Game!!!")
                break
            else:
                insertLetter(position, 'O')
                print("Computer placed an \'O\' in position", position)
                printboard(board)
        else:
            print("Sorry \'X\'s won this time!")
            break
    
    if isboardFull(board):
        print("Tie Game!!!")
        

if __name__ == '__main__':
    main()
