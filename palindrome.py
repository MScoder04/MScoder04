number=int(input("Enter your number: "))
r_number=number
rev=0
while number>0:
    digit=number%10
    rev=rev*10+digit
    number=number//10
if r_number==rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")