
radius = float(input("Enter the radius : "))
if 0.0 <= radius <= 100.0 :
	pi =3.14 
	area = pi * radius * radius
	print(f"Area of circle = {area:.6f}")
else:
	print("Enter a positive value upto 100")