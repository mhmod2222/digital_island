def check_contradict(A1, A0, C1, C0):
    if (A0 == A1) and (C0 != C1):
        if C0 == 0 and C1 != 0:
            C0 = C1
        elif C0 != 0 and C1 == 0:
            C1 = C0
        else:
            C0 = C1 = min(C0, C1)
    return C1, C0
    
def can_enter(n_rows, n_cols, x, y):
        if (x<0) or (x>n_rows-1) or (y<0) or (y>n_cols-1):
            return False
        return True
    
def expand_search(matrix, is_visited, Cat, x, y, test_num):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    is_visited[x][y] = True
    i = [-1, 0 , 0]
    j = [0 , -1, 1]
    for k in range(len(i)):
        is_safe = can_enter(n_rows, n_cols, x+i[k], y+j[k])
        if (is_safe):
            if matrix[x+i[k]][y+j[k]]==test_num:
                if (is_visited[x+i[k]][y+j[k]]):
                    if Cat[x][y] != 0:
                        Cat[x][y] = Cat[x+i[k]][y+j[k]] = min(Cat[x][y], Cat[x+i[k]][y+j[k]])
                    else:
                        Cat[x][y] = Cat[x+i[k]][y+j[k]]
                else:
                    if Cat[x][y] == 0:
                        Cat[x][y] = Cat[x+i[k]][y+j[k]] = max(map(max, Cat)) + 1
                    else:
                        Cat[x+i[k]][y+j[k]] = Cat[x][y]
            else:
                if Cat[x][y] == 0:
                    Cat[x][y] = max(map(max, Cat)) + 1
                if Cat[x+i[k]][y+j[k]] == 0:
                    Cat[x+i[k]][y+j[k]] = max(map(max, Cat)) + 1
            is_visited[x+i[k]][y+j[k]] = True
                

def solution(A):
    n_rows = len(A)
    n_cols = len(A[0])
    Cat = [[0 for z in range(n_cols)] for z in range(n_rows)]
    is_visited = [[False for z in range(n_cols)] for z in range(n_rows)]
    is_visited[0][0] = True
    Cat[0][0] = 1
    
    for i in range(n_rows):
        for j in range(n_cols):
            if not is_visited[i][j]:
                test_num = A[i][j]
                expand_search(A, is_visited, Cat, i, j, test_num)
            if can_enter(n_rows, n_cols, i-1, j):
                Cat[i-1][j], Cat[i][j] = check_contradict(A[i-1][j], A[i][j], Cat[i-1][j], Cat[i][j])
            if can_enter(n_rows, n_cols, i, j-1):
                Cat[i][j-1], Cat[i][j] = check_contradict(A[i][j-1], A[i][j], Cat[i][j-1], Cat[i][j])
            if can_enter(n_rows, n_cols, i, j+1):
                Cat[i][j+1], Cat[i][j] = check_contradict(A[i][j+1], A[i][j], Cat[i][j+1], Cat[i][j])
    return Cat

a = [[1, 4, 4],
     [4, 3, 4],
     [3, 2, 4],
     [2, 2, 2],
     [3, 3, 4],
     [1, 4, 4],
     [4, 1, 1]]

#a = [[1]*3 for _ in range(7)]

x = solution(a)
print(x)