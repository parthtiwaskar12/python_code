import itertools

digit1 = int(input("digit1 (0-9): "))
digit2 = int(input("digit2 (0-9): "))
digit3 = int(input("digit3 (0-9): "))

if 0 <= digit1 <= 9 and 0 <= digit2 <= 9 and 0 <= digit3 <= 9:
	digits = [str(digit1) , str(digit2) , str(digit3)]

	combinations = itertools.permutations(digits)
	for combo in combinations:
		print(''.join(combo))
else:
	print('Invalid')

