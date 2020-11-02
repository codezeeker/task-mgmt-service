stuffs = []
while True:
    print("add your list item:")
    items = input()
    stuffs.append(items)
    print(stuffs)
    cont = input("Do you want to continue?")
    if cont == "y":
        continue
    elif cont == "n":
        break
print("here is your list of items today: ", stuffs)
print(" -------------- ")
print("Have a good day")