cont = "y"
lst = list()
while cont == "y":
    item = input("\nEnter the list item: ")
    lst.append(item)
    cont = input("\nDo you want to continue?[y/n] :")

print("\n\n------------------")
print("   Today's tasks")
print("------------------")
for i in lst:
    print(i+"\n")
print("------------------")