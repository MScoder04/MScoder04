def function1(n):
    sum=n*(n+1)/2
    return sum

def function2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

def function3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
    return sum
    
print(function1(7))
print(function2(7))
print(function3(7))