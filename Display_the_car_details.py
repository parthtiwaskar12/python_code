class Car:
	def __init__(self,brand,price,model,color):
		self.brand = brand
		self.price = price
		self.model = model
		self.color = color
	def display_details(self):
		print(self.brand)
		print(self.price)
		print(self.model)
		print(self.color)
class Car1(Car):
	def __init__(self,brand ,price,model,color):
		super().__init__(brand,price,model,color)
		
	def display_details(self):
		super().display_details()
class Car2(Car):
	def __init__(self,brand,price,model,color):
		super().__init__(brand,price,model,color)

	def display_details(self):
		super().display_details()

def get_car_details():
	brand = input("brand: ")
	price = float(input("price: "))
	model = input("model: ")
	color = input("color: ")
	return brand, price, model, color

print("Details for Car 1:")
car1_brand, car1_price, car1_model, car1_color = get_car_details()
car1= Car1(car1_brand,car1_price,car1_model,car1_color)


print("Details for Car 2:")
car2_brand, car2_price, car2_model, car2_color = get_car_details()

car2 = Car2(car2_brand,car2_price,car2_model,car2_color)


print("Car 1 Details:")
car1.display_details()


print("Car 2 Details:")
# Display details of the car1
car2.display_details()


