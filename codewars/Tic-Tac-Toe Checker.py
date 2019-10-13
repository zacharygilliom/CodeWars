def isSolved(board):
    check_list = []
    for list in board:
        product = 1
        for x in list:
            product *= x
        check_list.append(product)
    if (board[0][0] == board[0][1] == board[0][2] == 1) or (board[1][0] == board[1][1] == board[1][2] == 1) or \
            (board[2][0] == board[2][1] == board[2][2] == 1) or (board[0][0] == board[1][0] == board[2][0] == 1) or \
            (board[0][1] == board[1][1] == board[2][1] == 1) or (board[0][2] == board[1][2] == board[2][2] == 1) or \
            (board[0][0] == board[1][1] == board[2][2] == 1) or (board[0][2] == board[1][1] == board[2][0] == 1):
        return 1
    elif (board[0][0] == board[0][1] == board[0][2] == 2) or (board[1][0] == board[1][1] == board[1][2] == 2) or \
            (board[2][0] == board[2][1] == board[2][2] == 2) or (board[0][0] == board[1][0] == board[2][0] == 2) or \
            (board[0][1] == board[1][1] == board[2][1] == 2) or (board[0][2] == board[1][2] == board[2][2] == 2) or \
            (board[0][0] == board[1][1] == board[2][2] == 2) or (board[0][2] == board[1][1] == board[2][0] == 2):
        return 2
    elif check_list[0] == 0 or check_list[1] == 0 or check_list[2] == 0:
        return -1
    else:
        return 0

print(isSolved([[0,0,1],[0,1,2],[2,1,0]]))
print(isSolved([[1,1,1],[0,2,2],[0,0,0]]))
print(isSolved([[2,0,2],[2,1,1],[1,2,1]]))