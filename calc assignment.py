#calculator_assignment

def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def percentage(x,y):
    return x%y

print("enter your choice")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Percentage")
choice = input('enter your choice: ')

num1 = int(input("enter the first num: "))
num2 = int(input("enter the second num: "))

if choice == '1':
    print(num1, "+" , num2 ,"=",add(num1,num2))
elif choice == '2':
    print(num1, "-", num2,"=", substract(num1, num2))
elif choice == '3':
    print(num1, "*", num2,"=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2,"=", divide(num1, num2))
elif choice == '5':
    print(num1, "%", num2,"=", percentage(num1, num2))
else:
    print("enter the choice within 1 to 5")
