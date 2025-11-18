#Milage Converter

print("Welcome to Distance Convertor!\nChoose what you wanna convert:\n")
print("1. KM -> Miles\n2. Miles -> KM\n")

option = None

option = input("Option = ")

if option == '1':
    KM = input("Enter KMs:")
    print(f"{KM} KM -> {int(KM) * 0.621371} Miles")

elif option == '2':
    Miles = input("Enter KMs:")
    print(f"{Miles} Miles -> {int(Miles) * 1.60934} KM")

else:
    print("Invalid Input! ")



