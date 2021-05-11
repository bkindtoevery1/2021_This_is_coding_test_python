n, m = tuple(map(int, input().split(' ')))
board = []
for i in range(n):
	temp = input()
	board.append([int(x) for x in temp])


def dfs(i, j):
	global n, m, board
	if i < 0 or i == n or j < 0 or j == m:
		return
	if board[i][j]:
		return
	board[i][j] = 1
	dfs(i - 1, j)
	dfs(i + 1, j)
	dfs(i, j - 1)
	dfs(i, j + 1)


ans = 0
for i in range(n):
	for j in range(m):
		if not board[i][j]:
			dfs(i, j)
			ans += 1
print(ans)