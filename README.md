tvcom
======
**tvcom** is an assistance module that provides a friendly interface for commanding LG tvs via a serial connection. 

It was designed to be extensible and could potentially work on similar models, most probably those produced between 2009 and 2011.

All raw serial codes that made this script possible were extracted from the user manual for model 37LG5000, you may be able to find similar documentation for your own LG TV by checking your models manual for a section on RS-232 setup:
https://www.lg.com/uk/support

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

You can use -l to obtain a list of valid commands. You can then obtain the valid values for the command by passing -k [keycode or Description]. Below is an example of powering the television on.

-c is assumed if no flags are passed

```console
$./tvcom -l
ka	power
kc	aspect_ratio
kd	screen_mute
ke	volume_mute
kf	volume
kg	contrast
kh	brightness
ki	colour
kj	tint
kk	sharpness
kl	osd_select
km	remote_lock
kt	balance
ku	colour_temp
kz	abnormal_state
jp	ism_method_plasma
jq	power_saving_plasma
ju	auto_configure_vga
mb	add_skip
mc	ir_key
mg	backlight_lcd
xb	input_select
$ ./tvcom -k power
KEYCODE	DESCRIPTION
00	off
01	on
FF	status
$ ./tvcom power status
off
$ ./tvcom power on
$ ./tvcom power status
on
$ 
```

