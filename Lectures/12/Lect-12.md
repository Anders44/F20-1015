# Lecture 12 - Basic Command Line Commands

[Using the command Line - https://youtu.be/lQFz4O8sqVA](https://youtu.be/lQFz4O8sqVA)<br>

From Amazon S3 - for download (same as youtube videos)

[Using the command Line](http://uw-s20-2015.s3.amazonaws.com/1015-L-12-command-line-overview.mp4)<br>

## Basic Linux Commands

These are the commands at the command line that will get you through most situations.

## Getting help in Linux

- man – view manual pages for Linux commands
- echo - just echo back what you type in (Print statement)

## Linux directory management commands

Navigating filesystems and managing directories:

- pwd – current directory
- cd – change directory
- mkdir – make new directory
- rmdir – remove directories in Linux
- ln – make links and symlinks to files and directories

## Linux Shell Commands

- clear – clear screen
- history – show history of previous commands

## Time and Date commands

- date – show current date and time
- cal - show a calendar


## Linux file operations

Navigating filesystem and managing files and access permissions:

- ls – list files and directories
- cp – copy files (work in progress)
- rm – remove files and directories (work in progress)
- mv – rename or move files and directories to another location
- chmod – change file/directory access permissions
- chown – change file/directory ownership
- find - search file system for a file

# Text file operations in Linux

Most of important configuration in Linux is in clear text files, these commands will let you quickly inspect files or view logs:

- cat – concatenate files and show contents to the standard output
- more – basic pagination when viewing text files or parsing Linux commands output
- head – show the first 10 lines of text file (you can specify any number of lines)
- tail – show the last 10 lines of text file (any number can be specified)
- grep – search for patterns in text files
- vi - editor used on most systems.
- awk - a programming language for text.

## Networking commands in Linux

Figure out your network setup.

- hostname – your computers hostname - Often this is used on the network as the name.
- ifconfig – show and set IP addresses (found almost everywhere) (ipconfig on windows)
- ping – check if remote host is reachable via ICMP ping

## Process management

Listing processes and confirming their status, and stopping processes if needed:

- ps – list processes
- top – show tasks and system status
- kill – kill a process (stop application running)


# Remote access commands

ssh is really the only way to go, but it’s important to know telnet as well:

- telnet – clear-text (insecure) remote access protocol - useful for testing connectivity.
- ssh – Secure SHell – encrypted remote access client (see scp also)

# File transfers commands

Know how to copy files between servers or just download some package from the web:

- scp – secure (encrypted) version of cp command (see ssh also)
- curl – download files from remote servers, HTTP/HTTPS 
- wget – download files from remote servers, HTTP/HTTPS and FTP
- rsync - copy and syncronized directory trees

## Source Code Control System

- git init .
- git status
- git add 
- git commit
- git push origin master
- git checkout
- git pull


## Details on Vim

Interactive Vim Tutorial: [https://www.openvim.com/](https://www.openvim.com/)


