"""
The {register_vehicle func} is doing alot (Many responsibilities):
    it: generates ID, Lisence plate, computes_catalogue price, tax percentage 
    and prints out all info
NOTE:{register_vehicle func} has low cohesion, has a lot of responsibilities
NOTE:{register_vehicle func} is HIGHLY COUPLED: 
Directly relying on implementation  details of the {Registry class}, has to know about (
    generate_vehicle_id
    generate_vehicle_license
)
FIXME:SIDE-EFFECTS: Hard to add another brand of vehicle, have to sift through conditions
NOTE:SOLUTION: SEPERATE  & COLLECT INFORMATION
"""
import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo


class VehicleRegistry:
    """Container for these two functions.
    Need to instanciate this class in order to access the functions
    """
    vehicle_info = {}
    def add_vehicle_info(self,brand,electric,catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand,electric,catalogue_price)
        
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        text_1 = f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}"
        return f"{text_1}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
    
    def create_vehicle(self, brand):
        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)

class Application:
    def register_vehicle(self, brand: string):
        # compute the catalogue price
        # FIXME:Data is not stored logically
        # FIXME:Coupling btwn brand_name and catalogue prices
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 6000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of catalogue price, except for Electric cars where it is 2%)
        # FIXME:tax calculation depends on whether a brand is electric or not
        # but not on the individual brand names
        tax_percentage = 0.05
        if brand == "Tesla MOdel 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02
        payable_tax = tax_percentage * catalogue_price

        # prints out the vehicle registration information
        print("Registration complete. Vehicle information")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print("Payable tax: {payable_tax}")


app = Application()
app.register_vehicle("BMW 5")
