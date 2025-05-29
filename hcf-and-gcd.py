largest=int(input("Enter the larger number: "))
smallest=int(input("Enter the smaller number: "))

while(smallest):
    store=smallest
    smallest=largest%smallest
    largest=store

print("HCF is equal to ", largest)