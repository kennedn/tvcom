tvcom
======
**tvcom** is a  wrapper script for speaking to an LG tv (37LG5000) via an RS-232 serial connection. It was designed to be extensible and could potentially work on similar models. 

## Prerequisites

* Python3
* pyserial module (pip install pyserial)
* A serial connection to the RS-232 port on the tv, the following variable will need modified in tvcom if you're serial port differs (Raspi GPIO is /dev/ttyAMA0):
>  ```python
>  tv_serial = Serial('/dev/ttyAMA0', timeout=serial_timeout)
>  ```
>  To test your serial connection it may be worth manually connecting to the serial port and sending a known command, for example the below will connect to the serial port with local echo enabled so you can see what you are typing, a command is then send that asks for the status of the tv's power (ka for power, ff for status). If you get a response back as is shown below then your connection is working.
>  ```console
>  picocom --echo /dev/ttyAMA0
>  ka 00 ff
>  a 01 OK01x
>  ```

## Usage

- Run it with python3 e.g python3 **tvcom**

```console
./tvcom [-lh] [-k name/long_name] [-c "long_name desc" ] [-r "name keycode" ]

-l, --list:           Get a list of defined long_names for commands
-k, --list_keycodes:  Get a list of keycodes for a given long_name (expects arg)
-c, --command:        Run a command using long_name and description, get these values from -l and -k, default command is status
-r, --raw_command:    Run a command using name and keycode, get these values from -l and -k
-h, --help:           Display this message
```

# Example

The below example lists the commands available for the volume keycode, returns the current status of volume, changes the volume to 20 and confirms the change happened with another status.

-c and status are assumed if not otherwise specified

```console
$ ./tvcom -k volume
KEYCODE	DESCRIPTION
FF	status
00-64	0-100
$ ./tvcom -c volume status
10
$ ./tvcom -c volume
10
$ ./tvcom volume
10
$ ./tvcom volume 20
$ ./tvcom volume
20
$ 
```

