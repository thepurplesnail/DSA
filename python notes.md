### Creating objects
`vehicle.py`
```python
class Vehicle:
    def __init__(self, year, model, plate_number, current_speed):
        self.year = year
        self.model = model
        self.plate_number = plate_number
        self.current_speed = current_speed

    def move(self):
        self.current_speed += 1

    def accelerate(self, value):
        self.current_speed += value

    def stop(self):
        self.current_speed = 0
    
    def vehicle_details(self):
        return self.model + ', ' + str(self.year) + ', ' + self.plate_number
```
`truck.py`
```python
from vehicle import Vehicle
class Truck(Vehicle):
    def __init__(self, year, model, plate_number, current_speed, current_cargo):
        super().__init__(year, model, plate_number, current_speed)
        self.current_cargo = current_cargo

    def add_cargo(self, cargo):
        self.current_cargo += cargo

    def remove_cargo(self, cargo):
        self.current_cargo -= cargo
```
### Dictionaries
```python
people = {'Bob':30, 'Mary':25}
people['Sarah']=32 # people = {'Bob':30, 'Mary':25, 'Sarah':32}
people['Bob']=28 # people = {'Bob':28, 'Mary':25, 'Sarah':32}

if 'Bob' in people:
    print('Bob exists!')
else:
    print('There is no Bob!')
```
### Hash Tables
```python
D = {'a': 1, 'c': 3, 'b': 2}
for k,v in D.items():
    print(k,':',v)
```
