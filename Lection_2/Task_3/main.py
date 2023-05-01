
print("-------------------------------------------------------")
print("Program, that search non-unique elements from all three sets without duplication\n")

set1 = set(input("Enter the first set separated by a space: ").split())
set2 = set(input("Enter the second set separated by a space: ").split())
set3 = set(input("Enter the third set separated by a space: ").split())

nonUniq = set1.intersection(set2, set3)

print("\nNon-unique elements from all three sets without duplication: ", list(nonUniq))
print("-------------------------------------------------------")