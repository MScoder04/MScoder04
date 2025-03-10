class computer:
    def __init__(self):
        self.__maxprice=100

    def sell(self):
        print("Selling price is {}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice=price

# max price will not change using the object
obj=computer()
obj.sell()
obj.__maxprice=200
obj.sell()

# setmaxprice function has to be used in order to change the price for the private member variable
obj.setmaxprice(200)
obj.sell()