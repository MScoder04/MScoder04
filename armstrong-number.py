input=int(input("Enter the number: "))
l=len(str(input))
temp=input
result=0
while temp > 0:
    digit=temp%10
    #  '%' means remainder
    result=result+(digit**l)
    temp=temp//10
    # '//' means floor division; rounded value toward the low side
if result==input:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")