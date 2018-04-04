'''
Author: Daryll Osis
Date: April 4, 2018
Description: A simple program that still focus on class and inheritance. it has methods addTax to add 
             tax to the price, sellProduct which changes the status of the item to "sold", returnItem 
             changes the price and the status of the item depending on the reason of why the item is 
             return and displayInfo which basically prints out the attributes of the item.
'''

class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

        #runs the displayInfo() everytime a new instance is created
        self.displayInfo()
    
    #add tax to the price.
    def addTax(self):
        tax = self.price * 0.12
        self.price += tax
        return  self

    #changes the status of the item once this method is called and the item is sold.
    def sellProduct(self):
        self.status = "sold"
        return self

    #changes the price and the status of the item depending on the reason for return. 
    def returnItem(self, reason_for_return):
        if(reason_for_return == "defective"):
            self.price = 0
            self.status = "defective"
        if(reason_for_return == "unhappy"):
            self.price = self.price*0.8
            self.status = "used"
        return self

    #displays the information about the item.
    def displayInfo(self):
        print("Item name:", self.item_name)
        print("Price:", self.price)
        print("Weight:", self.weight)
        print("Brand:", self.brand)
        print("Status:", self.status)


#add an inheritance
product1 = Product(520, "Yeezy Boost 350", 0.3, "Adidas")

#return the item with the reason of return being "unhappy"
product1.returnItem("unhappy").displayInfo()

#sells the product.
# product1.sellProduct().displayInfo()