file1=open("file2.txt","w")
file1.write("This is file 2. ")
file1.write("This file is has text inside. ")
file1.write("This file is for file2new.py. ")
file1.write("It is very good.")
file1.close()

file1=open("file2.txt","r")
print(file1.read())

file2=open("file3.txt","w")

for line in file1.readlines():
    print(line)
    if not (line.startswith("This")):
        print(line)
        file2.write(line)
file1.close()
file2.close()

file2=open("file3.txt","r")
print(file2.readlines())
file2.close()