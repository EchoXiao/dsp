# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> - pwd
  - mkdir
  - rmdir
  - touch file1
  - rm file1
  - mv file1 file2
  - ls -a
  - mv file1-oldpath newpath
  - cat #short preview of the file
  - cd #change directory

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` is the linux command to show current files in the directory. The extra key `-a` stands for `-all`, which will list out all the hidden files. `-l` will display long list of all the information about the files it contains. `-lh` will display long list of informations in human readable formats. Combining all the keys together `-lah` will display all the files within the directory with a long detail list in human readable format. `-t` will display the files from most recently modified to oldest. Lastly, `-Glp` will display colorized output with long list of information for each files, and an extra slash (`/') after each filename if that file is a directory.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> - `ls -a`
  - `ls -l`
  - `ls -lt`
  - `ls -c`
  - `ls -u`

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> Xargs command is designed to construct argument lists and invoke other utility. xargs reads items from the standard input or pipes, delimited by blanks or newlines, and executes the command one or more times with any initial-arguments followed by items read from standard input.

The below command line will find all the files in the current and below directories with extension ending in .java, then it will look for word "Stocks" within each file.

```console
$ find . -name "*.java" | xargs grep "Stock"`
```

Read more: http://javarevisited.blogspot.com/2012/06/10-xargs-command-example-in-linux-unix.html#ixzz4kcRX3rai

 

