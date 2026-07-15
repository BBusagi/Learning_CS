#25 Try Except\

# try:
#     number = int(input("Enter a number"))
#     print(number)
# except:
#     print("Invalid input")

try:
    value = 10/0
    number = int(input("Enter a number"))
    print(number)
except ValueError as err:
    print(err)
except ZeroDivisionError:
    print("Divided by zero")