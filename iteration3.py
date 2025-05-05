def squaretime(n):
    iteration=0
    for i in range (1,n+1):
        for j in range (1,n+1):
            print("*",end=" ")
            iteration+=1
        print()

    print(iteration)
squaretime(10)

# The complexity here is O(n^2)