#Board
board = [
    [["  "],["  "],["  "]],
    [["  "],["  "],["  "]],
    [["  "],["  "],["  "]]
]

checkers = [
    board[0][0][0]!="  ",
    board[0][1][0]!="  ",
    board[0][2][0]!="  ",
    board[1][0][0]!="  ",
    board[1][1][0]!="  ",
    board[1][2][0]!="  ",
    board[2][0][0]!="  ",
    board[2][1][0]!="  ",
    board[2][2][0]!="  "
]

chance = True
while True:
    while True:
        if chance:
            lis = input("Enter position: ").split(',')
            chance = False
            int_lis = []
            for i in lis:
                int_lis.append(int(i))
            x,y=int_lis
            board[x][y][0]="X"
            print(f'{board[0]}\n{board[1]}\n{board[2]}')
        else:
            lis = input("Enter position: ").split(',')
            chance = True
            int_lis = []
            for i in lis:
                int_lis.append(int(i))
            x,y=int_lis
            board[x][y][0]="O"
            print(f'{board[0]}\n{board[1]}\n{board[2]}')
        if board[0][0][0] == board[0][1][0] == board[0][2][0]:
            if board[0][0][0] == "X":
                print("Player 1 wins!")
                break
            elif board[0][0][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[1][0][0] == board[1][1][0] == board[1][2][0]:
            if board[1][0][0] == "X":
                print("Player 1 wins!")
                break
            elif board[1][0][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[2][0][0] == board[2][1][0] == board[2][2][0]:
            if board[2][0][0] == "X":
                print("Player 1 wins!")
                break
            elif board[2][0][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[0][0][0] == board[1][0][0] == board[2][0][0]:
            if board[0][0][0] == "X":
                print("Player 1 wins!")
                break
            elif board[0][0][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[0][1][0] == board[1][1][0] == board[2][1][0]:
            if board[0][1][0] == "X":
                print("Player 1 wins!")
                break
            elif board[0][1][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[0][2][0] == board[1][2][0] == board[2][2][0]:
            if board[0][2][0] == "X":
                print("Player 1 wins!")
                break
            elif board[0][2][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[0][0][0] == board[1][1][0] == board[2][2][0]:
            if board[0][0][0] == "X":
                print("Player 1 wins!")
                break
            elif board[0][0][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif board[0][2][0] == board[1][1][0] == board[2][0][0]:
            if board[0][2][0] == "X":
                print("Player 1 wins!")
                break
            elif board[0][2][0] == "O":
                print("Player 2 wins!")
                break
            else:
                continue
        elif all(checkers):
            print("Draw!!!")
            break
        print("\n")
    choice = input("Do you want to play again??(Y/N): ").upper()
    if choice == "Y":
        print("Quitting....")
        break
    else:
        continue
