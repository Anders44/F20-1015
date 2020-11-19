

# Lecture 24 - Classification using TensorFlow

TensorFlow has implemented a higher level library called Keras - this takes the nice interface
of Keras and allows you all the benefits of the underlying TensorFlow library.

This is what we are going to use for a classification demo (and homework).

You can use classification on images - to tell cats from dogs in pictures.  This makes for a cute
demo but it takes a long time to train the demo (long time being 10 to 15 minutes on most
student computers).  This can be addressed by tuning-down the image sizes to itty bitty images
of cats and dogs - but then you get inaccurate results.   So...

I picked a data set that is not images - it is a list of cars.  It has all the features
that we need to cover - and - more importantly since it is a tiny data set - we can train
our system in a few seconds and get good results!


So... for images you would want to read in the images, size them the same, convert them from
color to black and white then train.   With a table of data you have other considerations.

Let me demo a "shirt"/"shoe" classification example.  This only takes a little bit on
my system - a fairly fast system with a GPU.    The code for this is mostly the same
as the "car" demo - except for the feature engineering.

The first one of these is a thing called *one hot encoding*.  Let me explain it this way:

Suppose that you have 2 addresses:

```
438 4th St
```

and 

```
13814 W. Atlantic Ave
```

These could be ranked as '1' in '13814' is lower than '4' in '438' so it is less important.
Or we could look at the number as a number, in which case 438 is less than 13814.
Or we could look at it as the location on the globe and it turns out that 438 4th is
north of 13814 and north is better, or ...

None of these make any sense at all.   So we need to encode the data so that it removes
bias from the data set.   One of the most common was of encoding this is "one hot encoding".
This means that each address would be converted into a 1 for that address and a 0 for all
other addresses.   This means that data matching with the address "438 4th St..." would be
a 1 in the "438 8th St" column and a 0 in all the other address columns.  If you have
5 million addresses in your data set then you have 5 million address columns.

Each of these columns is one detention in our "tensor".  Suddenly a 3d model looks
really simple and "millions" of dimensions is a reality.

Our little data set with cars has a bunch of "columns" like this.   In each case we
will convert a "text" column into a numeric one hot encoded set of columns.

Another thing is that our "model" in TensorFlow only works on number so converting 
from a text column to a set of number columns makes a lot of sense.

This is part of our "feature" engineering - another part is just understanding the
data.  In most machine learning projects "feature" engineering is the primary activity
that you engage in.  The 2nd activity is building a working system for handling
the data.  We will get back to the "system" later.


Let's run the "car" demo - then we will dig into the code and how it works.




