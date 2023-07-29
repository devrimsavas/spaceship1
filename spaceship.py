
class Spaceship:

    def  __init__(self,name,ship_type):
        self.name=name
        self.ship_type=ship_type
        
        self.engine_one=None
        self.engine_two=None

        self.fuel_tank=0

        self.pilot=None 

        self.location=None

        self.total_laser=0
        self.shield=0

        self.ignition=False

    def  __str__(self):
        return f"name: {self.name}- class: {self.ship_type}- location {self.location} fueltanks {self.fuel_tank}"

    def set_location(self,location):
        self.location=location

    def full_tank(self,fuel_amount):

        self.fuel_tank+=fuel_amount

        return self.full_tank


    def check_fuel(self):
        if self.fuel_tank==0:
            print("fuel tank is empty.")
            return False
        elif self.fuel_tank<1000:
            print(f"you have only {self.fuel_tank} liters.Not enough for flight")
            return False

        elif self.fuel_tank>1000:
            print(f"you have {self.fuel_tank} liters. Enough for flight")
            return True;

    def set_pilot(self,pilot):

        self.pilot=pilot
       

        return f"Pilot assigned {pilot} "


    def check_pilots(self):
        if not self.pilot:
            print(f"you need pilots.the ship {self.name} has no pilot")
            return False
        else:

            print("pilot assigned")
            return True
        
    def check_flight_list(self):
        flight_list_text=""
        if self.pilot:

            flight_list_text=f"""
Checklist for spaceship {self.name}

1-fuel level         : {self.fuel_tank}
2-Pilot             : {self.pilot}
3-Spaceship location : {self.location}
"""
        print(flight_list_text)
        if (self.check_fuel() and self.check_pilots()):
            print(f"-Check List completed:\n-No malfunction found\n-Ready to launch\n-STATUS OKAY")
            return True
        else:
            print(f"-Check list not completed.\n-You cannot launch the ship.\n-Check systems again\n-STATUS ERROR")
            return False

    def start_ignition(self):

        if not self.location:
            print("Cannot lift off.Spaceship is still in production center")
            
        elif self.check_flight_list():
            self.ignition=True
            print("ignition positive")
            print("lift off")

        else:
            self.ignition=False 

