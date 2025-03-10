num=int(input("Enter number of school days attended this year: "))
attendance=(num/180)*100
if attendance>50:
    print("You have attended school for most of the school year.")
    if attendance>=75:
        print("You are eligible to take the exam.")
    else:
        print("But not enough days to be eligible to take the exam.")
else:
    print("You have not attended school for most of the school year.")
