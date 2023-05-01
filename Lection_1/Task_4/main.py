import math

print("-------------------------------------------------------------")
print("Quadratic equation calculator:\nax2 + bx + c = 0, a ≠ 0")
numA = int(input("Enter (a) number: "))
numB = int(input("Enter (b) number: "))
numC = int(input("Enter (c) number: "))
Discriminant = (numB **2) - (4 * numA * numC)

if numA == 0:
    print("Error! Number (a) = 0")
    exit()

if Discriminant > 0:
    root1 = (-abs(numB) + math.sqrt(Discriminant)) / 2
    root2 = (-abs(numB) - math.sqrt(Discriminant)) / 2
    print("Discriminant is bigger than 0, so there`s 2 roots:\nRoot 1 = {}\nRoot2 = {}".format(root1, root2))
elif Discriminant == 0:
    root1 = -abs(numB /  2 * numA)
    print("Discriminant is 0, so there`s 1 root:\nRoot 1 = ", root1)
else:
    print("Discriminant less than 0, so there`s no roots")
print("-------------------------------------------------------------")