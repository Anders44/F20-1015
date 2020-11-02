# Buuild an Object in a Hierarcny

Due Nov 9

200 pts.



The utility of this project is that you actually are working on a system that could be used in the
real world.  This is simplified from an entire "van" control system - but it is part of the system.
Our simplified system leaves off thins like measure the level of water and other tanks in the system
and useful information like using a GPS combined with a calendar to tell you how much to tilt the
solar panels into the sun.

1. Add a "heating_pad"  switch and object to the van controller.  The main program already has the
data being read in for the raw_solar field and it is in data.2.csv.
2. There is an input that provides the "raw" voltage from the solar panels.  If this is 0.4 volts less than the minimum
charging voltage, and the battery is too cool, then turn on the heating pad.  Leave it on until the voltage	
rises es enough on the batteries - or until the voltage is enough to charge.  If the batteries are
still to cool - but we are getting enough voltage - then turn on the "heater" and bring the batteries	
up to temperature.
This "if" construct needs to be added to the main program - so near line 133 in the file - at the	
first test before the other "if"/"ifelse"(around line 133) constructs.
3. Make certain to turn off the "heating-pad" in the other if/else cases - so that you never have the case	
of the heating-pad on while the cooling system is trying to cool the batteries at the same time.

When I run the program I do it at the command line in VSCode - with 

```
python main.py data.2.csv
```

But I think that you can just run it with the little blue triangle at the top of the VSCode
window.

You will need to use [github.com/Univ-Wyo-Education/F20-1015](github.com/Univ-Wyo-Education/F20-1015)
to get the files for this assignment.  Clone the class files and
do your work in the directory .../Assignments/06.   To do this you will need to start Visual Studio Code
and tell it to navigate to a directory, then create a project in that directory.   The class lecture
will walk through this process.


