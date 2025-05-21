class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started")

class Car:
    def __init__(self,engine):
        
        self.engine = engine  # Containment: Car contains an Engine

    def start(self):
        self.engine.start()

class Suzuki(Car): # Inheritance: Suzuki is a Car
    def __init__(self, model, engine):
        super().__init__(engine) #Super calls the parent class constructor
        self.model = model
        self.engine = engine
        self.make = "Suzuki"

class ElectricCar:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Charging the car")

class Tesla(Suzuki, ElectricCar): # Multiple inheritance: Tesla is a Suzuki and an ElectricCar
    def __init__(self, model, engine, battery_capacity):
        Suzuki.__init__(self, model, engine) # Calls the constructor of the parent class (note that super is not used here)
        ElectricCar.__init__(self, battery_capacity) 
        self.make = "Tesla"

    def start(self): #polymorphism: Tesla has a different start method than Suzuki
        print(f"{self.make} {self.model} with {self.battery_capacity}kWh battery is starting.")
        self.charge()
        self.engine.start()


# Example usage
engine = Engine(150)
car = Car(engine)
car.start()
Suzuki("Swift", engine).start()
Tesla("Model Suzuki", engine, 100).start()