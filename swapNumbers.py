def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(f"The value of a after swapping is {a}")
    print(f"The value of b after swapping is {b}")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(f"The value of a before swapping is {a}")
print(f"The value of b before swapping is {b}")
swap(a,b)