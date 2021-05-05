n, k = tuple(map(int, input().split(' ')))
ans = 0

while n > 1:
	n = n % k and n - 1 or n / k
	ans += 1

print(ans)