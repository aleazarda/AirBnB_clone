![HolbertonBnB Logo](https://github.com/TZITA/AirBnB_clone/blob/main/Additionals/HBNBlogo.png)
# *HolbertonBnB*
## AirBnB Clone

---

## Description

HolbertonBnB is a complete web application.

This project only implements the back-end console and basic file storage engine.

## Classes

HolbertonBnB has the following classes:

1. BaseModel
2. FileStorage
3. User
4. State
5. City
6. Amenity
7. Place
8. Review

## Console

The console is a command line interpreter used to manage the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes of the  application.

### Console Usage

The HolbertonBnB console can be run both interactively and non-interactively. 

To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the 
file `console.py`:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```
