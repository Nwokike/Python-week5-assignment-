# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass  # abstract behavior (to be overridden)

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")

# -----------------------------
# Testing polymorphism
# -----------------------------
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # same method, different behavior!
