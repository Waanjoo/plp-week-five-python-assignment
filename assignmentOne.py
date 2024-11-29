class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.battery = 100

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def check_battery(self):
        print(f"Battery level: {self.battery}%")

    def charge(self, minutes):
        self.battery += minutes // 10

# Example usage
phone1 = Smartphone("Apple", "iPhone 15", 256, "Black")
phone2 = Smartphone("Samsung", "Galaxy S24", 512, "White")

phone1.make_call("+1234567890")
phone2.send_message("+9876543210", "Hello")
phone1.check_battery()
phone1.charge(30)
phone1.check_battery()