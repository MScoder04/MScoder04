roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
int_form=0
input=(input("Enter a roman value: "))
for i in range (len(str(input))):
    if i+1 < len(str(input)) and roman[input[i]] < roman[input[i+1]]:
        int_form=int_form-roman[input[i]]
    else:
        int_form=int_form+roman[input[i]]
print(int_form)