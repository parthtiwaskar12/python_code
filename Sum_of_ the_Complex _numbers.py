class Complex:
    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def initComplex(self):
        self.real = int(input("Real Part: "))
        self.imaginary = int(input("Imaginary Part: "))

    def display(self):
        print(f"{self.real}+{self.imaginary}i")

    def sum(self, c1, c2):
        self.real = c1.real + c2.real
        self.imaginary = c1.imaginary + c2.imaginary

# Main program
print("complex number 1")
c1 = Complex()
c1.initComplex()
c1.display()

print("complex number 2")
c2 = Complex()
c2.initComplex()
c2.display()

print("Sum:", end=" ")
c3 = Complex()
c3.sum(c1, c2)
c3.display()