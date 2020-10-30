m4_changequote(`[[[',`]]]')

# Lecture 17 - Object Homework

[More on Objets and HeatPad - Homework  -  https://youtu.be/BtZhlpXS8b0]( https://youtu.be/BtZhlpXS8b0)<br>
[An object used to implement a Binary Tree - https://youtu.be/eRMPnPVDaBs](https://youtu.be/eRMPnPVDaBs)<br>

From Amazon S3 - for download (same as youtube videos)

[More on Objets and HeatPad - Homework ](http://uw-s20-2015.s3.amazonaws.com/1015-L-17-pt1-objects-and-heatpad.mp4)<br>
[An object used to implement a Binary Tree](http://uw-s20-2015.s3.amazonaws.com//Users/philip/Desktop/1015-L-17-pt2-tree-demo.mp4)<br>

Our "van" system has a heater, cooler and batteries - and we can run it.   Our next step is to take advantage of 
a little bit of free energy.  Remember that before the voltage on the solar panels is 0.4 volts higher than the
voltage on the batteries the solar charger can not charge.   On cold days we can take advantage of this early
morning ramp up.  

By adding a electric "heating" pad to the battery compartment and a new switch we can take this power
and run it through the heating pad and pre-warm the battery.

One important detail is that we turn off the heating pad before the voltage is too high - if we leave it on
then we will burn out the heating pad.  So we can run it from about 6 volts to 12.4 - the point where we
could possibly take solar and convert it to charge the battery.  In reality the we need 0.4 volts more than
the battery.  The heating pad specification says it can take up to 15.5 volts.

The panels themselves can produce up to 19.8 volts - the charge regulator cuts this off at the 12.8 maximum
for the batteries.

Homework 6 - Add a new "class" to the set of classes that run the battery management system to use a 
heating pad.





## Classes and data structures

Often classes are sued to encapsulate the interface to some sort of data that we access.

Let's talk about a "tree" and how we could build a "tree" class in Python.

First - why use a tree?  The answer is speed - but how will a tree effect our code.

What is a "tree"?

How we use Tuples to represent a "tree".

What are the operations on a "tree"?


```
m4_include(tree.py)
```

Now we can use it something like a dictionary, but having the ability to spit out
the data in a sorted order or reverse sorted order is useful.   Also the ability
to insert at a low cost (and delete at a low cost) is also useful.



