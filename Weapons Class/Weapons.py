class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage
    
    def getstats(self):
        print(f"{self.name} is a {self.category} dealing {self.damage}.")

class Sword(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.name = name
        self.category = category
        self.damage = damage
        self.damage_category = damage_category

    def getstats(self):
        crit = self.damage*3
        print(f"{self.name} is a {self.category} dealing {self.damage} {self.damage_category} damage. The weapon deals {crit} critical damage")

class Bow(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def getstats(self):
        crit = self.damage*2
        print(f"{self.name} is a {self.category} dealing {self.damage} {self.damage_category} damage. The weapon deals {crit} critical damage")

class LongBow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def getstats(self):
        crit = self.damage*2
        print(f"{self.name} is a {self.category} dealing {self.damage} {self.damage_category} damage. The weapon deals {crit} critical damage")
    
class ShortBow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def getstats(self):
        crit = self.damage*2
        print(f"{self.name} is a {self.category} dealing {self.damage} {self.damage_category} damage. The weapon deals {crit} critical damage")