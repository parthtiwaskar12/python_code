def factorial(num):
	if num ==0 or num == 1:
		return 1
	return num * factorial(num-1)

try:
	num = int(input("Enter a number : "))
	if num < 0:
		print("Enter a positive number\n")
	else :
		print(f"Factorial of given number is : {factorial(num)}\n")
except ValueError:
	print("invalid numbner")