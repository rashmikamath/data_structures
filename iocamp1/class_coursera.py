class Character:
    def __init__(self,name,initial_health):
        self.name=name
        self.health=initial_health
        self.inventory=[]

    def __str__(self):
        s="Name:"+ self.name
        s += "health" + str(self.health)
        s += "inventory" + str(self.inventory)
        return s

    def grab(self, item):
        self.inventory.append(item)

    def get_health(self):
        return self.health

def example():
    me=Character("Bob",20)
    print (str(me))
    me.grab("Pencil")
    me.grab("Paper")
    print(str(me))
    print("Health",me.get_health())
example()