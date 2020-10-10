
m4_changequote(`[[[', `]]]')

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
m4_include(vehicle1.py)
```

Ouptut:

```
m4_include(out1.py)
```


When we run it we don't get a useful output for the objects this can be fixed with
a string conversion.  That is the function `__str__`.


```
m4_include(vehicle2.py)
```

Ouptut:

```
m4_include(out2.py)
```
