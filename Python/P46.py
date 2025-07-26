def menu():
    print("\n<- Menu ->")
    print("1.Add product")
    print("2.View all products")
    print("3.Sell a product")
    print("4.Restock a product")
    print("5.Search by product id")
    print("6.Change name or price")
    print("7.Exit")


class Product:
    new_id = 1
    def __init__(self,name,price,quantity):
        self.id = Product.new_id
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.new_id += 1

    def __str__(self):
        return f"\n----------------------\nProduct ID: {self.id}\nProduct name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\n----------------------"    

class Inventory:
    def __init__(self):
        self.items = []

    def add(self,info):
        self.items.append(info)
        print(info)
        

    def view(self) :
        if self.items == []:
            print("🫙 Inventory is empty")
        else:    
          for product in self.items:
            print(product)

    def helper(self,product_name):
        
        for product in self.items:
            if product.name == product_name:
                return product
        return None    
             
    
    def sell(self,Product_name,quantity_to_sell):
        item = self.helper(Product_name)
        if item and item.quantity and item.quantity >= quantity_to_sell:
            item.quantity -= quantity_to_sell
            print("👍 Your purchase is successfull")
        else: 
            print(f"❌ Unsuccessfull!!!, Please recheck product details\nMaybe less units available")


    def restock(self,product_name,quantity):
        stock = self.helper(product_name)
        if stock and stock.quantity:
          stock.quantity += quantity
          print(f"{stock.name} now has {stock.quantity} pieces available")

        else:
            print("Please enter details of products available")  

    def search(self,id):
        found = False
        for product in self.items:
            if product.id == id:
                print(product)
                found = True
        if not found:
            print("Product with this ID number is not available")        


    def change_name(self,product_name):
        item = self.helper(product_name)
        
        if item:
               New_name = str(input(f"Enter new name of product: ")).capitalize().strip()
               item.name = New_name
               print(item)
                
        else:    
             print("❌ Unsuccessfull!!!, Product name not available")


    def change_price (self,name):
        item = self.helper(name)   
        if item:
                New_price = int(input(f"Enter new price of product: ")) 
                item.price = New_price
                print(item)                
        else:    
                 print("❌ Unsuccessfull!!!, Product name not available")  


inventory = Inventory()

while True:
        menu()
        try:    
          User_input = int(input("Enter (1,2,3,4,5,6,7): "))
        except:
          print("Please enter the valid integers")  
        else:  
          if User_input == 1:
            try:
              Name = str(input("Assign name to the product: ")).capitalize().strip()
              Price = int(input("Set a price of the product: "))
              Quantity = int(input("Number of pieces available: "))
              Assign = Product(Name,Price,Quantity)
              inventory.add(Assign)
            except:
               print("Please enter valid inputs")

          elif User_input == 2:
            inventory.view()

          elif User_input == 3:
            try:
              Product_name = str(input("Enter product name to be sold: ")).capitalize().strip()
              Quantity_ = int(input("Enter number of units to be sold: "))
    
            except:
                print("Please enter valid inputs") 
            else:     
               inventory.sell(Product_name,Quantity_)  
    
    
          elif User_input == 4:
            try:
              name_of_product = str(input("Enter product name: ")).capitalize().strip()
              new_quantity = int(input(f"Enter the number of units to be added of {name_of_product}: "))
   
            except:
                print("Please enter valid inputs")  

            else:
              if new_quantity > 0:
                 inventory.restock(name_of_product,new_quantity)
              else:
                  print("❌ Unsuccessfull!!!, Please enter non negative integers only")        

          elif User_input == 5:
            try:
              product_id = int(input("Enter product ID: "))
              
            except:
                print("Please enter an integer in product ID") 

            else:
                inventory.search(product_id)     

          elif User_input == 6:
            try:
              Command = int(input("Enter '1' to change name, '2' to change price: "))
              name = str(input("Enter initial name of product: ")).capitalize().strip()

                       
            except:
                print("Please enter valid inputs") 

            else:
              if Command == 1:
                  inventory.change_name(name)
                  print("👍 Product name has been changed")

              elif Command == 2:
                  inventory.change_price(name) 
                  print("👍 Product now has a new price") 
              else:
                  print("Please enter the given inputs")       

          elif User_input == 7:
            print("🙏 Thank you for your visit")
            break

          else:
            print("Please enter the valid integers") 
              










                








