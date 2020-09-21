# Lecture 09 - Dictionaries

## Youtube

[Dictionaries - https://youtu.be/cxXLXf5tG9g](https://youtu.be/cxXLXf5tG9g)<br>
[Visualize Dictionaries - https://youtu.be/lVxpcDKj2tY](https://youtu.be/lVxpcDKj2tY)<br>
[Accessing Dictionaries - https://youtu.be/icIvRmC2CJ0](https://youtu.be/icIvRmC2CJ0)<br>
[Syntax Review - https://youtu.be/icIvRmC2CJ0](https://youtu.be/icIvRmC2CJ0)<br>

From Amazon S3 - for download (same as youtube videos)

[Dictionaries](http://uw-s20-2015.s3.amazonaws.com/1015-L-09-pt1-dictionaries.mp4)<br>
[Visualize Dictionaries](http://uw-s20-2015.s3.amazonaws.com/1015-L-09-pt2-Visualize-Dictionary-and-Loop.mp4)<br>
[Accessing Dictionaries](http://uw-s20-2015.s3.amazonaws.com/1015-L-09-pt3-accessing-dictionaries.mp4)<br>
[Syntax Review](http://uw-s20-2015.s3.amazonaws.com/1015-L-09-pt4-syntax-review.mp4)<br>

## First how you do this when you don't have a dictionary

Without python dictionaries:

```
want = 'tom'
key = [ 'bob', 'jane', 'tom' ]
val = [ 18, 19, 16 ]

age = -1
ii = 0
while ( ii < len(key) ):
    if key[ii] == want:
        age = val[ii]
    ii = ii + 1

if age > 0:
    print ( f"Found: {want} age {age}" )
else:
    print ( f"not found {want}" )
```

Using a dictionary:

```
want = 'tom'
di = { 'bob':18, 'jane':19, 'tom':16 }
if want in di:
    age = di[want]
    print ( f"Found: {want} age {age}" )
else:
    print ( f"not found {want}" )

```
