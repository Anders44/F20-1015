# Lecture 05 - Lists

## On Youtube 

Lecture is in 6 parts but a bunch are short (5 minutes).

[Lists part 0 - Introduction - https://youtu.be/RRdSBahKuuY](https://youtu.be/RRdSBahKuuY)<br>
[Lists part 1 - syntax - https://youtu.be/2ozID0tVkUw](https://youtu.be/2ozID0tVkUw)<br>
[Lists part 2 - updating - https://youtu.be/Ikejr3c4xFs](https://youtu.be/Ikejr3c4xFs)<br>
[Lists part 3 - sorting - https://youtu.be/gxoEL9o9Trk](https://youtu.be/gxoEL9o9Trk)<br>
[Lists part 4 - more - https://youtu.be/XRKhJZ7CNGY](https://youtu.be/XRKhJZ7CNGY)<br>
[Lists part 5 - review - https://youtu.be/lodtH8ZCd1I](https://youtu.be/lodtH8ZCd1I)<br>

From Amazon S3 - for download (same as youtube videos)

[Lists part 0 - Introduction](http://uw-s20-2015.s3.amazonaws.com/1015-L-05-Lists-pt00-intro.mp4)<br>
[Lists part 1 - syntax](http://uw-s20-2015.s3.amazonaws.com/1015-L-05-Lists-pt01.mp4)<br>
[Lists part 2 - updating](http://uw-s20-2015.s3.amazonaws.com/1015-L-05-Lists-pt02-updating-lists.mp4)<br>
[Lists part 3 - sorting](http://uw-s20-2015.s3.amazonaws.com/1015-L-05-Lists-pt03-lists-and-sorting.mp4)<br>
[Lists part 4 - more](http://uw-s20-2015.s3.amazonaws.com/1015-L-05-Lists-pt04.mp4)<br>
[Lists part 5 - review](http://uw-s20-2015.s3.amazonaws.com/1015-L-05-Lists-pt6-review.mp4)<br>

# on YouTube - Podcasts

[Human factors in Software Development - https://youtu.be/59xeTopiL0I](https://youtu.be/59xeTopiL0I)<br>
[Computer Trends - Machine Learning - https://youtu.be/vylGM3hn-9c](https://youtu.be/vylGM3hn-9c)<br>

From Amazon S3 - for download (same as youtube videos)

[Human factors in Software Development](http://uw-s20-2015.s3.amazonaws.com/1015-PodCast-Human-Factors.mp3)<br>
[Computer Trends - Machine Learning](http://uw-s20-2015.s3.amazonaws.com/1015-PodCast-Computer-Trends-Machine-Learning.mp3)<br>


## One of a Time v.s. a List of results - Tools that are fantastic but don't use a list.

Compare use of Photoshop v.s. GIMP when you have 121000 images to watermark.

## What are lists - syntax for them.

Use square for lists, round for tuples.

```
list1 = [ "abc", 3 ]
```

## Accessing the elements in a list.

```
a = list1[0]
list1[0] = "def"
list1.remove ( 3 )
list1.append ( 4 )
print ( list1 )
del list1[1:2]
print ( list1 )
```

## List Comprehensions

```

list1 = [ 4, 2, 20, 1,0,10,3 ]

l2 = [ i for i in list1 if i < 10 ]
print ( l2 )

for i in range(10):
	print i

sqr = [ i*i for i in range(10) ]
sqr2 = [ i**2 for i in range(10) ]

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)


```
