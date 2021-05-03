n, m, k = tuple(map(int, input().split(' ')))

arr = list(map(int, sorted(input().split(' '), reverse=True)))

print(arr[0] * (m - int(m / (k + 1))) + arr[1] * int(m / (k + 1)))
