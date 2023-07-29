from spaceship import Spaceship

def select_ship_from_hangar():
    global hangar
    if not hangar:
        print("No ships in the hangar")
        return None

    show_hangar()
    while True:
        try:
            index_ship = int(input("Choose the ship: "))
            if 0 <= index_ship < len(hangar):
                return hangar[index_ship]
            else:
                print("Invalid selection. Please choose a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")

def create_new_spaceship():
    ship_name=input("Enter name for new spaceship:  ").strip()
    ship_type=input("Spaceship class ?:  ").strip()

    new_ship=Spaceship(ship_name,ship_type)
    hangar.append(new_ship)

    print("you have created a new spaceship and added to hangar")

    print(f"{new_ship}\n")
    

def set_ship_location():
    global hangar

    ship_to_locate=select_ship_from_hangar()
    if ship_to_locate:
        location=input("Spaceship location?  ")
        ship_to_locate.set_location(location)
    

def display_ship_situation():

    global hangar
    ship_to_panel=select_ship_from_hangar()
    if ship_to_panel:
        ship_to_panel.check_flight_list()


def check_fuel_situation():
    global hangar
    ship_to_check_fuel=select_ship_from_hangar()
    if ship_to_check_fuel:
        ship_to_check_fuel.check_fuel()


def full_tanks():
    global hangar
    ship_to_fill_fuel=select_ship_from_hangar()
    if ship_to_fill_fuel:

        fuel_amount=int(input("how much liters?"))
        ship_to_fill_fuel.full_tank(fuel_amount)
 



def assign_pilots():
    global hangar
    ship_to_pilot=select_ship_from_hangar()
    if ship_to_pilot:

        pilot1=input("pilot  ")

        ship_to_pilot.set_pilot(pilot1)
    

def launch_spaceship():

    global hangar
    ship_to_launch=select_ship_from_hangar()
    if ship_to_launch:
        ship_to_launch.start_ignition()


def show_hangar():
    header_text="|Index|   Ship Name   |   Ship Class  | Fuel Amount |      Pilots        |     Location    |"
    print(header_text)
    for index,ship in enumerate(hangar):
        pilots_str = ship.pilot if ship.pilot else "No Pilots"
        location_str=ship.location if ship.location else "Production Place"
        print(f"|{index:^5}|{ship.name:^15}|{ship.ship_type:^15}|{ship.fuel_tank:^13}|{pilots_str:^20}|{location_str:^17}|")


def turn_off_control():
    global fly
    select=input("you want to turn control off ?")
    if select=="y":
        fly=False
        

    else:
        print("Control remains on")
        


menu_text="""

1- Create a New Spaceship
2- set location for spaceship
3- display cockpit panel
4- check fuel level
5- fill tanks
6- Assign pilots
7- launch spaceship 
8-Show hangar

9-Turn off Control

your commands sir--> """


hangar=[]
fly=True

while fly:
    selection=int(input(menu_text))
    if selection==1:
        create_new_spaceship()

    elif selection==2:
        set_ship_location()

    elif selection==3:

        display_ship_situation()

    elif selection==4:
        check_fuel_situation()

    elif selection==5:

        full_tanks()

    elif selection==6:
        assign_pilots()

    elif selection==7:
        launch_spaceship()

    elif selection==8:
        show_hangar()
    elif selection==9:
        turn_off_control()


    else:
        print("Invalid Selection")
        
        


                        
