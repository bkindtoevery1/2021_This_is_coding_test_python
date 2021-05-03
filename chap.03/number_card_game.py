n, m = tuple(map(int, input().split(' ')))

ans = -1
for i in range(n):
	to_compare = sorted(list(map(int, input().split(' '))))[0]
	ans = ans < to_compare and to_compare or ans

print(ans)
