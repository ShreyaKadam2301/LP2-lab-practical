n= int(input("Enter the value of n "))
board = []

def getBoard():
    for i in range(n):
        nList = []
        for j in range(n):
            nList.append(0)
        board.append(nList)
        
def printBoard():
    for i in range(n):
        for j in range(n):
            print(board[i][j],end="")
        print("")
    
def isSafe(row,col):
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[j][col] == 1:
            return False
    
    i= row-1 # check if queen occur at north-west
    j= col-1
    while(i>=0 and j>=0):
        if board[i][j] ==1:
            return False
        i=i-1
        j=j-1
        
    i= row-1 #north-east
    j= col+1
    while(i>=0 and j<n):
        if board[i][j] ==1:
            return False
        i=i-1
        j=j+1
        
    i= row+1 #south-west
    j= col-1
    while(i<n and j>=0):
        if board[i][j] ==1:
            return False
        i=i+1
        j=j-1
        
    i= row+1 #south-east
    j= col+1
    while(i<n and j<n):
        if board[i][j] ==1:
            return False
        i=i+1
        j=j+1
        
    return True
    
def put(n,count):   #count keeps count on no. of queens on board
    if count==n:    # i.e, if count=4 i.e, the no of total queens
        return True
    for i in range(n):
        for j in range(n):
            if isSafe(i,j):
                board[i][j]=1
                count +=1
                if put(n,count) == True:
                    return True
                board[i][j] =0
                count -=1 
    return False

getBoard()
put(n,0)
printBoard()
