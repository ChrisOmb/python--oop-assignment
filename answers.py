# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"
    
    def discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        return f"New price after {percentage}% discount: ${self.price}"


class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life, is_waterproof):
        super().__init__(brand, model, price)
        self.battery_life = battery_life
        self.is_waterproof = is_waterproof
    
    def display_info(self):
       
        info = super().display_info()
        return f"{info}, Battery Life: {self.battery_life} hours, Waterproof: {self.is_waterproof}"
    
    def waterproof_test(self):
        return "Passed waterproof test!" if self.is_waterproof else "Failed waterproof test!"


smartphone = Smartphone("Apple", "iPhone 15", 1200)
print(smartphone.display_info())
print(smartphone.discount(10)) 
smartwatch = Smartwatch("Samsung", "Galaxy Watch 6", 400, 48, True)
print(smartwatch.display_info())
print(smartwatch.waterproof_test())
