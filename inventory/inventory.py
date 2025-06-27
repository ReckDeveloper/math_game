# Inventory System

class Inventory:
    def __init__(self):
        self.items = []
        # ...other inventory attributes...

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
