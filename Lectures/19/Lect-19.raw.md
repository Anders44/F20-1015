m4_changequote(`[[[',`]]]')

<style>
.pagebreak { page-break-before: always; }
.half { height: 200px; }
</style>

# Lecture 19 - Building our game.

[Install for Game - https://youtu.be/Fm3Ncly1ssE](https://youtu.be/Fm3Ncly1ssE)<br>
[Game Overview - https://youtu.be/wU77inWHpDs](https://youtu.be/wU77inWHpDs)<br>

From Amazon S3 - for download (same as youtube videos)

[Install for Game](http://uw-s20-2015.s3.amazonaws.com/1015-L-19-pt1.mp4)<br>
[Game Overview](http://uw-s20-2015.s3.amazonaws.com/1015-L-19-pt2-run-game.mp4)<br>

The space invaders  game is in Chapter 12, 13, 14 in the book.   You can access the code at [https://github.com/ehmatthes/pcc](https://github.com/ehmatthes/pcc).

on Mac or Linux in a dermal:

```
$ cd
$ mkdir Projects
$ cd Projects
$ git clone https://github.com/ehmatthes/pcc
$ cd pcc
```

On Windows in the PowerShell:

```
C:\> mkdir Projects
C:\> cd Projects
C:\Projects\> git clone https://github.com/ehmatthes/pcc
C:\Projects\> cd pcc
```

Basically all the code is there.  So let's get it running using the VSCode tool.

Demo of using VS Code for hello-ty.py and the game.

Let's walk through the code.  We will need to have a good understanding of how the
code works to integrate it with TensorFlow.

Your task (homework/assignment) is a "hello world" for the game and TensorFlow.

200pts - Homework 8.  Get all of this installed, pygame, use git to pull a copy of the
game down, install TensorFlow.  Use the "hello-tf.py" program to run and get the
version of TensorFlow.

Hello World for TensorFlow:

```
m4_include(hello-tf.py)
```

When I run it I get:



```
2020-11-01 11:25:41.636582: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'libcudart.so.10.1'; dlerror: libcudart.so.10.1: cannot open shared object file: No such file or directory
2020-11-01 11:25:41.636636: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
TensorFlow Version: 2.3.1

```


## GPUs and NPUs


