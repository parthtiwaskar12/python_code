m1 = float(input("subject 1: "));
m2 = float(input("subject 2: "));
m3 = float(input("subject 3: "));
m4 = float(input("subject 4: "));
m5 = float(input("subject 5: "));

avg = (m1 + m2 + m3 + m4 + m5 )/ 5;
print(f"Average Marks: {avg:.2f}");
if  100 >= avg >= 90:
	print("Grade: A\n");
elif 89 >=avg >= 80:
	print("Grade: B\n");
elif 79 >= avg >= 70:
	print("Grade: C\n");
elif 69 >= avg > 60:
	print("Grade: D\n");
else :
	print("Grade: F\n");