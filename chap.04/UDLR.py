n = int(input())
x, y = (1, 1)
command = input().split(' ')
for letter in command:
	if letter == 'U':
		if x != 1:
			x -= 1
	elif letter == 'D':
		if x != n:
			x += 1
	elif letter == 'L':
		if y != 1:
			y -= 1
	elif letter == 'R':
		if y != n:
			y += 1

print(x ,  y)