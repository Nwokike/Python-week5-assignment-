# Assignment 1: Smartphone Example

# Parent class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down...")

# Child class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.camera_megapixels = camera_megapixels
    
    def take_photo(self):
        print(f"📸 Taking a {self.camera_megapixels}MP photo with {self.brand} {self.model}.")

    def install_app(self, app_name):
        print(f"📲 Installing {app_name} on {self.brand} {self.model}.")

    # Example of encapsulation (private method)
    def __system_update(self):
        print(f"{self.brand} {self.model} is updating system files...")

    # Public method that uses encapsulated one
    def update(self):
        print(f"🔄 Checking for updates on {self.brand} {self.model}...")
        self.__system_update()


# -----------------------------
# Testing
# -----------------------------
phone1 = Smartphone("Apple", "iPhone 14", "128GB", 12)
phone2 = Smartphone("Samsung", "Galaxy S23", "256GB", 50)

phone1.power_on()
phone1.take_photo()
phone1.install_app("WhatsApp")
phone1.update()
phone1.power_off()

print()

phone2.power_on()
phone2.take_photo()
phone2.install_app("Instagram")
phone2.update()
phone2.power_off()
