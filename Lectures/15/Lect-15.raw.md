
m4_changequote(`[[[', `]]]')

# Lecture 15 - Cool Little Objects

## YouTube

[Python Objects - https://youtu.be/pCYMwbcnRdM](https://youtu.be/pCYMwbcnRdM)<br>

From Amazon S3 - for download (same as youtube videos)

[Python Objects](http://uw-s20-2015.s3.amazonaws.com/1015-L-15-objects.mp4)<br>



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
m4_include(vehicle1.py)
```

Ouptut:

```
m4_include(out1.txt)
```


When we run it we don't get a useful output for the objects this can be fixed with
a string conversion.  That is the function `__str__`.


```
m4_include(vehicle2.py)
```

Ouptut:

```
m4_include(out2.txt)
```

So what are the parts.



Now let's increment the odometer by 2 miles.

```
m4_include(vehicle3.py)
```

And the output is:

```
m4_include(out3.txt)
```


	
## Objects are useful concept in describing a set of data.

Objects group into a hierarchy.

The Term is "inheritance" - that one object can inherit the data and methods from
another object.



```
m4_include(vehicle4.py)
```

And the output is:

```
m4_include(out4.txt)
```


This is *useful*!  Lots of stuff can be modeled in this fusion.  Lot's of software
is done this way - this includes lots of libraries that form Python itself.  This is
why when we refer to strings we say `string.upper()` - we have a `string` object
and it has a method `upper()`.


This isn't the only way to organize data.  But if you have a system that deals with
50% or maybe 80% of data then that is a useful abstraction.

One of the most important object hierarchies is something that you use all the time.
That is the screen and all of the "objects" in your user interface.  When you build a
user interface this system of organization is quite often critical to the entire process
of building the software.


Example! - how a User Interface Works.


Now not all things fall into this kind of a category/hierarchy.


Example! - how a user / authentication system works.



