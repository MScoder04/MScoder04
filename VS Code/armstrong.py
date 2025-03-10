num=int(input("Enter a number: "))
num_str = str(num)
print(num_str)
for num_str in range (1,10):
    print(f"{num_str**3}")
x=(int(num/100))
y=(int((num-(x*100))/10))
z=(int((num-((x*100)+(y*10)))))
print(x,y,z)
if ((x**3)+(y**3)+(z**3) == num):
    print(str(num)+" is an armstrong number.")
else:
    print(str(num)+" is not an armstrong number.")