
from  colorama  import  init
from  colorama  import  Fore ,  Back ,  Style
init ()


print(Fore.BLACK)
print(Back.CYAN)
white = input("Вкажіть дію (+, -, /, *): ")

print(Back.RED)
a = float (input("Вкажіть перше число: "))
b = float (input("Вкажіть друге число: "))

print(Back.GREEN)
if (white == "+"):
    c = a+b
    print ("Результат: " + str (c))
elif (white == "-"):
    c = a-b
    print ("Результат: " + str (c))
elif (white == "/"):
    c = a/b
    print ("Результат: " + str (c))
elif (white == "*"):
    c = a*b
    print ("Результат: " + str (c))
else:
    print ("Дані введено не коректно")


input()


