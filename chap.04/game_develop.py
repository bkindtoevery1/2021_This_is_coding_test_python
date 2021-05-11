n, m = tuple(map(int, input().split(' ')))
x, y, d = tuple(map(int, input().split(' ')))
game_map = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
	game_map.append(list(map(int, input().split(' '))))
ans = 0
while True:
	if game_map[x][y] == 0:
		ans += 1
		game_map[x][y] = -1
	for i in range(5):
		if i == 4:
			d = (d + 2) % 4
			if game_map[x + dx[d]][y + dy[d]] == 1:
				print(ans)
				
				exit(0)
			else:
				break
		d = (d + 3) % 4
		if not game_map[x + dx[d]][y + dy[d]]:
			break
	x += dx[d]
	y += dy[d]
	d = (d + 2) % 4
