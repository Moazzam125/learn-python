# Class
                                        # (class) is initial
                                        # () if empty (optional)
                                        # (__init__) is main attribution
                                        # it distance our personal code from conflicit
                                        # (self) in first function is like web
                                        
class cat():
    """Model a cat"""

    def __init__(self, name, age):
        """Name and age attributes"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """A cat sitting by a command"""
        print(self.name + " is now siting!")

    def roll_over(self):
        """A cat rolls over by command"""
        print(self.name + " is rolled over!")

my_cat = cat('tom', '2')
your_cat = cat('kali', '3')

print("My cat's name is " + my_cat.name + ".")
print("My cat's age is " + my_cat.age + ".")
my_cat.sit()
my_cat.roll_over()

print("Your cat's name is " + your_cat.name + ".")
print("Your cat's age is " + your_cat.age + ".")
your_cat.sit()
your_cat.roll_over()

print("\n====================")


# 

class car():
    """A car model"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_discriptive_name(self):
        """Return a neatly formatted name"""
        long_name = self.make + ' ' + self.model + ' ' + str(self.year)
        
        return long_name.title()
    
    def read_odometer(self):
        """Car's real mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Update odometer to a given value.
        Reject the change if it roll it reverse.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("An odometer cann't reverse back.")
        
    def increasement_odometer(self, miles):
        """Add given amount to the odometer"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("An odometer cann't be reversed back.")
    
my_favoriate_car = car('toyota', 'hilux', '2015')
print(my_favoriate_car.get_discriptive_name())

my_favoriate_car.update_odometer(20350)
my_favoriate_car.read_odometer()

my_favoriate_car.increasement_odometer(100)
my_favoriate_car.read_odometer()

print("\n====================")


# Modify an existing attribute

my_favoriate_car.odometer_reading = 10202
print(my_favoriate_car.odometer_reading)

print("\n====================")


# Inheritance
                                                        # No space b/w class name.

class battery():
    """Show the range of battery"""

    def __init__(self, battery_size = 70):
        """Show battery size"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Show battery"""
        print("This car has battery size of " + str(self.battery_size) + ".")

    def get_range(self):
        """Show the battery range it provides"""
        if self.battery_size == 70:
            distance_range = 240
        elif self.battery_size == 85:
            distance_range = 270
        
        print("\nThis car can go about " + str(distance_range) + " km without charge.")


class ElectricCar(car):
    """Represent aspects of car, specific to ElectricCar"""

    def __init__(self, make, model, year):
        """Initialize the characters of parent class(car).
        Specfic to electric car."""
        super().__init__(make, model, year)
        self.battery = battery()

    def describe_battery(self):
        """Describe the battery of electrtic car"""
        print("This electric car has " + self.battery_size + " kWh battery.")

my_electric_car = ElectricCar('tesla', 'model s', str(2019))
print(my_electric_car.get_discriptive_name())

my_electric_car.update_odometer(670)
my_electric_car.read_odometer()

my_electric_car.increasement_odometer(450)
my_electric_car.read_odometer()

my_electric_car.battery.get_range()

print("\n====================")


#Declare proterty to class


class MyClass(object):
    """Decare propery"""

    def __init__(self):
        """using super method"""
        super(MyClass, self).__init__()
        self._numeric_var = 1

@property
    def numeric__var(self):
        return self._numeric_var

print("\n====================")