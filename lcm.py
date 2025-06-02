largest=int(input("Enter the larger number: "))
a=largest
smallest=int(input("Enter the smaller number: "))
b=smallest

while(smallest):
    store=smallest
    smallest=largest%smallest
    largest=store

lcm=(a*b)/largest
print("The LCM is ",lcm)