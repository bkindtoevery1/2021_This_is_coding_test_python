ans = 8
location = input()
minus_position = [['a', 'h'], ['b', 'g'], ['1', '8'], ['2', '7']]
for pos in minus_position[0]:
	if pos in location:
		ans /= 2

for pos in minus_position[1]:
	if pos in location:
		ans -= 2

for pos in minus_position[2]:
	if pos in location:
		ans /= 2

for pos in minus_position[3]:
	if pos in location:
		ans = ans == 4 and ans - 1 or ans - 2

print(int(ans))