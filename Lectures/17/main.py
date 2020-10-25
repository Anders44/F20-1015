"""
Main program : Batter Management System
---------------------------------------

1. read in the set of values
2. Create all of the objects
3. run the "state" machine that calls objects to turn/on/off stuff

"""

import sys
import csv

import charger_switch
import output_switch
import fan_switch
import heater_switch
import ac_switch

import simulated_system

world_state = {
    "switch:1": 0,   # Charger(input)
    "switch:2": 0,   # Output
    "switch:3": 0,   # Fan
    "switch:4": 0,   # Heater
    "switch:5": 0,   # AC
    "switch:6": 0,   # HeatingPad
    "bat_level:0": 12.0,      # Current Charge Level
    "solar_avail:0": 13.3,    # Output from Solar
    "usage:0": 0.3,           # Being Used
    "bat_temp:0": 58,           # Being Used
    "air_temp:0": 58,           # Being Used
    "raw_solar:0": 9,           # Raw pwoer from solar panels
}

bat_min_temp = 35
bat_max_temp = 90

raw_solar_on = 6        # Min voltage where solar will be run to heating pad.
raw_solar_off = 12.4    # Max voltage where solar will be run to heating pad.

# print ( f"{world_state}" )

fn = "data.1.csv"
if len(sys.argv) > 1 :
    fn = sys.argv[1]

# print ( f"fn={fn}" )  # print to verify that we get the command line argument.

# Setup Objects
charger = charger_switch.charger_switch()
output = output_switch.output_switch()
fan = fan_switch.fan_switch()
heater = heater_switch.heater_switch()
ac = ac_switch.ac_switch()

simulated_system.system_init ( world_state )

charger.turnOff()
world_state = simulated_system.get_state()
if world_state["switch:1"] == 1:
    print ( "Error 1, world_state={world_state}" )

charger.turnOn()
world_state = simulated_system.get_state()
if world_state["switch:1"] == 0:
    print ( "Error 2, world_state={world_state}" )

charger.turnOff()



# Read in Input Data
# open file in read mode
with open(fn, 'r') as read_ref:
    # csv.reader() takes a file_ref as an input.
    # This is a chunk of data that associates the name/mode
    # with the actual file on the system and allows reading
    # and writing of the file.
    csv_reader = csv.reader(read_ref)

    # Get all rows of csv from csv_reader object as list of tuples
    list_of_tuples = list(map(tuple, csv_reader))

    # Input Columns Are:
    # Time, BatTemp, AirTemp, SunAvail, BatAvail


    # display all rows of csv
    # print(list_of_tuples)


    # Convert tuples to internal format 
    ii = 1
    while ii < len(list_of_tuples):
        list_of_tuples[ii] = ( int(list_of_tuples[ii][0]), int(list_of_tuples[ii][1]), int(list_of_tuples[ii][2]), int(list_of_tuples[ii][3]),
        float(list_of_tuples[ii][4]), float(list_of_tuples[ii][5]) )
        ii = ii + 1

    # display after concerting int data.
    print(list_of_tuples)


    # Step Through it, 1 step at a time
    # Turn Off Charger
    charger.turnOff()
    ii = 1
    while ii < len(list_of_tuples):

        world_state = simulated_system.get_state()
        # Set values usage, solar_avail
        # Time, BatTemp, AirTemp, SunAvail, BatAvail, Usage
        #    0,       1,       2,        3,        4,     5
        world_state[ "bat_level:0"   ] = list_of_tuples[ii][4]
        world_state[ "solar_avail:0" ] = list_of_tuples[ii][3]
        world_state[ "bat_temp:0"    ] = list_of_tuples[ii][1]
        world_state[ "air_temp:0"    ] = list_of_tuples[ii][2]
        world_state[ "usage:0"       ] = list_of_tuples[ii][5]
        


        ################################################################
        # Main Processing                                              #
        ################################################################

        if world_state[ "bat_temp:0" ] < bat_min_temp and world_state[ "solar_avail:0" ] > world_state[ "bat_level:0" ]:
            if charger.isOn(): # If On... Turn Off Charger
                charger.turnOff()
            heater.turnOn() # Turn On Heater
            fan.turnOff() # Turn Off Fan
            ac.turnOff() # Turn Off AC
            print ( "case 1" )

        elif world_state[ "bat_temp:0" ] > bat_max_temp and world_state[ "bat_temp:0" ] > world_state[ "air_temp:0" ] and world_state[ "air_temp:0" ] < ( bat_max_temp - 10 ) :
            if charger.isOn(): # If On... Turn Off Charger
                charger.turnOff()
            fan.turnOn() # Turn On Fan
            ac.turnOff() # Turn Off AC
            heater.turnOff() # Turn Off Heater
            print ( "case 2" )

        elif world_state[ "bat_temp:0" ] > bat_max_temp and world_state[ "bat_temp:0" ] > world_state[ "air_temp:0" ] :
            if charger.isOn(): # If On... Turn Off Charger
                charger.turnOff()
            fan.turnOff() # Turn Off Fan
            ac.turnOn() # Turn On AC
            heater.turnOff() # Turn Off Heater
            print ( "case 3" )

        elif world_state[ "solar_avail:0" ] > world_state[ "bat_level:0" ] and world_state[ "bat_temp:0" ] >= bat_min_temp and world_state[ "bat_temp:0" ] <= bat_max_temp :
            charger.turnOn() # If Off... Turn On Charger
            print ( "case 4" )

        else:
            #  { 'bat_level:0': 12.4, 'solar_avail:0': 0, 'bat_temp:0': 28, 'air_temp:0': 25, 'usage:0': 0.2}
            # Report Possible Error 
            print ( f"case 5 - nothing to do, {world_state}" )


        
 
        ii = ii + 1

