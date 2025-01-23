import copy
n = 4
board = [["*" for j in range(0,n)] for i in range(0,n)]
ans = []

def isSafe(board,row,cloum,n):
    # check horizontal
    for j in range(0,n):
        if board[row][j] == 'Q':
            return False
    # Check for vertical 
    for i in range(0,n):
        if board[i][cloum] == "Q":
            return False
    # check for digonal
    i = row
    j = cloum
    while i >= 0 and j >= 0:
        if (board[i][j] == "Q"):
            return False
        i -= 1
        j -= 1
    i = row 
    j = cloum
    while i>=0 and j < n:
        if (board[i][j] == "Q"):
            return False
        i -= 1
        j += 1
    return True

    


def Nqueens(board,row,n,ans):
    # base case
    if n == row:
       
        ans.append(copy.deepcopy(board))
        return
    # Placing the queen in same  row diffrent colum
    for j in range(0,n):
        if (isSafe(board,row,j,n)):
            board[row][j] = "Q"
            Nqueens(board,row + 1, n, ans)
            board[row][j] = "*"
    

Nqueens(board,0,len(board),ans)
print(ans)
for solution in ans: 
    for i in range(n): 
        for j in range(n): 
            print(solution[i][j], end=" ") 
        print() 
        
    print()



