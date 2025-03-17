file1=open("file_proj1.txt","r")
print(file1.read())

file1=open("file_proj1.txt","w")
file1.write("Student Name: Misha Shahi | Student Age: 15 | Student Grade: 9th | Student Favorite Subject: Math")

file1=open("file_proj1.txt","r")
print(file1.read())
file1.close()