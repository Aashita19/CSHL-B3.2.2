class BaseEntity:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

    def use_item(self):
        pass


class Weapon(BaseEntity):
    def __init__(self, item_name, quantity, damage):
        super().__init__(item_name, quantity)
        self.damage = damage

    def use_item(self):
        print(f"{self.item_name} attacks for {self.damage} damage")

    def use_item_on(self, target=None):
        if target is None:
            print(f"{self.item_name} attacks a normal enemy "
                  f"for {self.damage} damage.")
        else:
            print(f"{self.item_name} attacks {target} "
                  f"for {self.damage} damage.")


class Potion(BaseEntity):
    def __init__(self, item_name, quantity, healing_amount):
        super().__init__(item_name, quantity)
        self.healing_amount = healing_amount

    def use_item(self):
        print(f"{self.item_name} restores "
              f"{self.healing_amount} health")


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_inventory(self):
        print("\n--- INVENTORY ---")

        for item in self.items:
            print(f"\nItem: {item.item_name}")
            print(f"Quantity: {item.quantity}")
            item.use_item()


# main program
inventory = Inventory()

sword = Weapon("Iron Sword", 1, 25)
bow = Weapon("Wooden Bow", 1, 15)
health_potion = Potion("Health Potion", 5, 50)
mana_potion = Potion("Mana Potion", 3, 30)

inventory.add_item(sword)
inventory.add_item(bow)
inventory.add_item(health_potion)
inventory.add_item(mana_potion)

inventory.display_inventory()

print("\n--- METHOD OVERLOADING ---")
sword.use_item_on()
sword.use_item_on("Dragon")
