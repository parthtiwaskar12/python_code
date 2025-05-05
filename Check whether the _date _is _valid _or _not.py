y = int(input("year: "))
m = int(input("month: "))
d = int(input("day: "))
leap = (y%4==0 and y%100!= 0) or (y%400 == 0)
days = [31,28+leap,31,30,31,30,31,31,30,31,30,31]
if m<1 or m>12 or d<1 or d>days[m-1]:
	print("invalid")
else: 
	print("valid")
	d+=1
	if d>days[m-1]:
		d=1
		m+=1
		if m>12:
			m = 1
			y+=1
	print(f"incremented date: {y}-{m:02d}-{d:02d}")