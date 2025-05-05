def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for string in str:
		if string in vowel:
			count += 1
	print(count)
	
	# Write your code here to count the vowels
	
str = input()
vowel_count(str)