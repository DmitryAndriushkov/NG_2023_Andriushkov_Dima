
print("-------------------------------------------------------")
print("Program, that search count elements whats you entered.")
print("Enter your elements\n(type 'enough' if you want to stop entering your elements)")
print("-------------------------------------------------------")

count = 0
list = []

while True:
    elems = (input("Element[{}]: ".format(count + 1)))
    list.append(elems)
    count += 1
    if elems == 'enough':
        break

print("-------------------------------------------------------")

amount = input("Which element you interested in?: ")

print("Result:", list.count(amount))