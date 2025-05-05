def Sumof(n):
	if n == 0:
		return 0
	else:
		return n % 10 + Sumof(  n // 10 )

# take user input and add the function call
number = int(input(''))
result = Sumof(number)
print(result)