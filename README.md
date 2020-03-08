tvcom
======
**tvcom** is a  wrapper script for speaking to an LG tv (37LG5000) via an RS-232 serial connection. It was designed to be extensible and could potentially work on similar models. 

## Prerequisites

- Python3
- pyserial module (pip install pyserial)

## Usage

- Run it with python3 e.g python3 **tvcom**

````
./tvcom [-lh] [-k name/long_name] [-c "long_name desc" ] [-r "name keycode" ]

-l, --list:           Get a list of defined long_names for commands
-k, --list_keycodes:  Get a list of keycodes for a given long_name (expects arg)
-c, --command:        Run a command using long_name and description, get these values from -l and -k, default command is status
-r, --raw_command:    Run a command using name and keycode, get these values from -l and -k
-h, --help:           Display this message
````

# Example

````
$ ./tvcom -k volume
###############
keycode	desc
###############
FF	status
00-64	0-100
$ ./tvcom -c volume status
10
$ ./tvcom -c volume 20
$ ./tvcom -c volume status
20
$ 
````

