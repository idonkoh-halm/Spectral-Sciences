import random
class Inventory:
    totalinventory=[]
    currentinventory=[]
    def __init__(self):
        self.totalinventory.append(self)
        self.currentinventory.append(self)
    def addto(self,inventoryitem):
        self.totalinventory.append(self)
        self.currentinventory.append(self)
    def removefrom(self):
        self.currentinventory.remove(self)
    def returning(self):
        self.currentinventory.append(self)
def test_new_inventitem():
    b=raw_input('Prompt asking about new item')
    Inventory().addto(b)
    print (b, "was added to the list")
test_new_inventitem() 