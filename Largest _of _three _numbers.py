n1 = float(input("Enter the first number: "));
n2 = float(input("Enter the second number: "));
n3 = float(input("Enter the third number: "));
largest = max(n1,n2,n3);
#if n1 > n2:
#	if n2 > n3:
#		print(f"Largest number: {n1}");
#	else:
#		print(f"Largest number: {n2}");
#else:
#	if n3 > n2:
#		print(f"Largest number: {n3}");
#	else:
#		print(f"Largest number: {n2}");
print(f"Largest number: {largest}");