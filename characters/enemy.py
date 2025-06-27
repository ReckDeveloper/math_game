# Enemy Class

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.gender = "male"
        self.outfit = "t-shirt and jeans"
        # ...other enemy attributes...

    def describe(self):
        return f"{self.name} is a man wearing a t-shirt and jeans."
