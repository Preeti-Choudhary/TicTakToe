import random

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

def show():
    print(
        "", board[0], "|", board[1], "|", board[2],
        "\n-----------\n",
        board[3], "|", board[4], "|", board[5],
        "\n-----------\n",
        board[6], "|", board[7], "|", board[8]
    )


def check_winner(a):
    if checkall(a, 0, 1, 2) is True or checkall(a, 3, 4, 5) is True or checkall(a, 6, 7, 8) is True or \
            checkall(a, 0, 4, 8) is True or checkall(a, 2, 4, 6) is True or checkall(a, 0, 3, 6) is True or\
            checkall(a, 1, 4, 7) is True or checkall(a, 2, 5, 8):
        return True


def checkall(player, loc1, loc2, loc3):
    if board[loc1] == player and board[loc2] == player and board[loc3] == player:
        return True


def all_taken():
    flag = True
    for i in range(0, 8):
        if board[i] != 'x' or board[i] != 'o':
            flag = False
    if flag is True:
        return True
    else:
        return False


show()

while True:

    user_input = input("pick a spot: ")
    user_input = int(user_input)

    if board[user_input] != 'x' and board[user_input] != 'o':
        board[user_input] = 'x'

        if check_winner('x'):
            print("-----------WINNER IS YOU-----------")
            show()
            exit(0)

        while True:
            random.seed()
            opponent = random.randint(0, 8)

            if board[opponent] != 'x' and board[opponent] != 'o':
                board[opponent] = 'o'

                if check_winner('o'):
                    print("-----------WINNER IS OPPONENT-----------")
                    show()
                    exit(0)

                if all_taken() is True:
                    print("-----------GAME ENDS. NO ONE WINS-----------")
                    exit(0)

                break

    else:
        print("spot already taken. pick another spot.")

    show()






