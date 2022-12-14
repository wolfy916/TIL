n, m, x, y, r, c, k = 2, 2, 1, 1, 2, 2, 2

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
move = ['u', 'd', 'l', 'r']
area = [['-']*(n+2)] + [['-'] + [0]*m + ['-'] for _ in '_'*n] + [['-']*(n+2)]
area[x][y] = 'S'
area[r][c] = 'E'

result = []


def dfs(s_i, s_j, z, k, arr):
    global result
    if z == k:
        if area[s_i][s_j] == 'E':
            result += [''.join(arr)]
    else:
        for i in range(4):
            ni, nj = s_i+di[i], s_j+dj[i]
            if area[ni][nj] != '-':
                dfs(ni, nj, z+1, k, arr+[move[i]])


dfs(x, y, 0, k, [])
if result:
    result.sort()
    answer = result[0]
else:
    answer = 'impossible'

print(answer)

