class Item:
    def __init__(self,name,type,power):
        self.name = name
        self.type = type
        self.power = power

    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nPower: {self.power}\n"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def display_items(self):
        if not self.items:
            print("There are no items present")
        else:

           for item in self.items:
             print(item)

    def find_by_type(self,type):
        
        found = False
        for item in self.items:
           if type.lower() in item.type.lower():
            print(f"{type} found\n")
            found = True
        if not found:
           print(f"The item of type {type} does not exist\n")

    def strongest_item(self):
       if not self.items:
          print("Inventory is empty")
          return

       strongest = self.items[0]
       for item in self.items[1:]:
          if item.power > strongest.power:
             strongest = item
       return strongest
    

          

I1 = Item("Knife","One Handed",59)
I2 = Item("Katana","Two Handed",89)

inventory = Inventory()
inventory.add_item(I1)
inventory.add_item(I2)

inventory.display_items()

inventory.find_by_type("One Handed")

strong = inventory.strongest_item()
if strong:
   print(f"Strongest item is:\n{strong}")            

