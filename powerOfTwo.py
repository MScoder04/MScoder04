def power(n):
    if (n==0):
        return 0
    if (n&(~(n-1))==n):
        return 1
    return 0
number=int(input("Enter a number: "))
if power(number)==0:
    print("This number is not a power of two.")
else:
    print("This number is a power of two.")