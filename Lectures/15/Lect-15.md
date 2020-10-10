


# Lecture 15 - Cool Little Objects

An object is a mix of data and code.

Let's model vehicles.

How do we associate code and data in a simple class.

"words" that you have to use:

class - the thing that defines that this is an "object"

__init__ - the thing that sets up a class - called a "constructor"

__main__ - the special name that allows you to build tests in the same file as a class.

self - the name that allows you to access the data associated with this "instance" of an object.

an "instances" is the "type" of a class with its data.


This is the definition or "type" for the object.

vehicle1.py:

```

class Vehicle:

    """ this is a constructor """
    def __init__ ( self, manufacturer, vtype, year ):
        self.year = year    
        self.vtype = vtype    
        self.manufacturer = manufacturer    
        self.odometer = 0


    """ this is a Method """
    def SetMilage ( self, n ):
        if n < 0 :
            print ( "Error: can't take milage off" )
        else:
            self.odomoter = self.odomoter + n

v1 = Vehicle( 'Tonka', 'truck', 2020 )
v2 = Vehicle( 'NASA', 'moon rover', 1969 )

print ( f"v1 = {v1}" )
print ( f"v2 = {v2}" )

```



class Vehicle:

    """ this is a constructor """
    def __init__ ( self, manufacturer, vtype, year ):
        self.year = year    
        self.vtype = vtype    
        self.manufacturer = manufacturer    
        self.odometer = 0


    """ this is a Method """
    def SetMilage ( self, n ):
        if n < 0 :
            print ( "Error: can't take milage off" )
        else:
            self.odomoter = self.odomoter + n

v1 = Vehicle( 'Tonka', 'truck', 2020 )
v2 = Vehicle( 'NASA', 'moon rover', 1969 )

print ( f"v1 = {v1}" )
print ( f"v2 = {v2}" )

class Vehicle:

    """ this is a constructor """
    def __init__ ( self, manufacturer, vtype, year ):
        self.year = year    
        self.vtype = vtype    
        self.manufacturer = manufacturer    
        self.odometer = 0


    """ this is a Method """
    def SetMilage ( self, n ):
        if n < 0 :
            print ( "Error: can't take milage off" )
        else:
            self.odomoter = self.odomoter + n

    """ Print out the class """
    def __str__ ( self ) :
        return ( f"Vehicle: {self.vtype} built in {self.year} by {self.manufacturer}" )

v1 = Vehicle( 'Tonka', 'truck', 2020 )
v2 = Vehicle( 'NASA', 'moon rover', 1969 )

print ( f"v1 = {v1}" )
print ( f"v2 = {v2}" )
