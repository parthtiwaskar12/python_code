dict = {}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")

	choice = int(input("Enter choice (1-4): "))

	match choice:
		case 1:
			name = input("Name: ")
			number = input("Phone number: ")
			dict[name] = number
		case 2:
			name = input("Name: ")
			if name in dict:
				del dict[name]
			else:
				print("Not found")
		case 3:
			print(dict)
		case 4:
			break
		case _:
			print("Invalid")

