
print("-------------------------------------------------------")
print("Program, that output only unique elements.")

elems = input("Enter a set of elements separated by a space: ").split()

uniqElems = list(set(elems))

print("Unique elements: ", uniqElems)
print("-------------------------------------------------------")