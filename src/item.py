
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def taken(self):
        print(f"Picked up {self.name}. Use it wisely...")
    
    def dropped(self):
        print(f"Dropped {self.name}.This item is no longer weighing you down!")
        
    def examine(self):
        print(f"{self.name}: \n{self.description}")
    
    