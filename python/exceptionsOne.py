import sys

x = int(input("X: "))
y = int(input("Y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    #Exit the program
    sys.exit(1)
    

print(f"{x} / {y} = {result}")