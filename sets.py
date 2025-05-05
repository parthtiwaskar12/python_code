a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations
c = A.union(B)
print("Union: ",c)
d = A.intersection(B)
print("Intersection: ",d)
e = A - B
print("Difference: ",e)