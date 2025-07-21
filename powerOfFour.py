def powerFour(n):
    count=0
    if (n&(~(n&(n-1)))):
        while (n>0):
            n>>=1
            count+=1
        if(count%2==0):
            return True
        else:
            return False
n=int(input("Enter a number: "))
if powerFour(n):
    print("This number is a power of four.")
else:
    print("This number is not a power of four.")