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
    "test:1": 0,     # Test Circuit
    "switch:1": 0,   # Charger(input)
    "switch:2": 0,   # Output
    "switch:3": 0,   # Fan
    "switch:4": 0,   # Heater
    "switch:5": 0,   # AC
    "bat_level:0": 12.0,      # Current Charge Level
    "solar_avail:0": 13.3,    # Output from Solar
    "usage:0": 0.3,           # Being Used
    "bat_temp:0": 58,           # Being Used
    "air_temp:0": 58,           # Being Used
}

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
        list_of_tuples[ii] = ( int(list_of_tuples[ii][0]), int(list_of_tuples[ii][1]), int(list_of_tuples[ii][2]), int(list_of_tuples[ii][3]), float(list_of_tuples[ii][4]) )
        ii = ii + 1

    # display after concerting int data.
    print(list_of_tuples)



    # Step Through it, 1 step at a time

    # Set values usage, solar_avail
