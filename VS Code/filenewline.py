file1=open("file_beginner.txt","r")
print(file1.read())
cnt=0
content=[]
content=file1.read()
print(content)
mylist=content.split("\n")
print(mylist)
lines=file1.readlines()
for i in lines:
        cnt += 1
print(cnt)