white = input("Вкажіть дію (+, _, /, *): ")
a = float (input("Вкажіть перше число: "))
b = float (input("Вкажіть друге число: "))
if (white == "+"):
    c = a+b
    print (c)
elif (white == "-"):
    c = a-b
    print (c)
elif (white == "/"):
    c = a/b
    print (c)
elif (white == "*"):
    c = a*b
    print (c)
else:
    print ("Дані введено не коректно")
input()

