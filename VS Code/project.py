class library:
    def __init__(self, list, name):
        self.booklist=list
        self.name=name
        self.lendDict={}
    def displayBooks(self):
        print(f"We have following books in our library {self.name}")
        for book in self.booklist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lend a book database updated, you can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the booklist.")
    def returnBook(self,book):
        self.lendDict.pop(book)
    
books=library(["Python", "F451", "The Giver", "Harry Potter", "Percy Jackson", "KOTLC"], "Read A Lot!")
while(True):
    print("Enter your choice to continue")
    print("1. Display Books\n 2. Lend a book\n 3. Add a book\n 4.Return a book")
    ch=input("Enter your choice:")
    if ch not in ["1", "2", "3", "4"]:
            print("Enter a valid option")
    else:
            ch=input()
    if ch=="1":
            books.displayBooks()
    elif ch=="2":
            book=input("Enter the book's name:")
            user=input("Enter your name:")
            books.lendBook(user,book)
    elif ch=="3":
            book=input("Enter the name of the book you want to add:")
            books.addBook(book)
    elif ch=="4":
            book=input("Enter the name of the book you want to return:")
            books.returnBook(book)
    else:
        print("Invalid option")
    print("Press 'Q' to quit and 'C' to continue")
    ch1=""
    while (ch1!="C" and ch!="Q"):
        ch1=input()
        if ch1=="Q":
            exit()
        elif ch1=="C":
            continue