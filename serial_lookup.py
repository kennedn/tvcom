#!/usr/bin/python

# Defines an object that allows corrolation between LG raw command + keycode pairs and
# Human readable descriptions of the commands / keycodes via a dictionary.
class SerialLookup():
    lookups = []

    def __init__(self, name, long_name,lookup_table, is_slider=False, read_only=False):
        self.name = name
        self.long_name = long_name
        self.lookup_table = lookup_table
        self.read_only = read_only
        # If set we will assume a value from 0 - 100 is always specified as a keycode
        # and convert to and from hex accordingly
        self.is_slider = is_slider
        # Reverses the key : value dict to a value: key dict for easier lookup later on
        self.inverse_table = {value: key for key, value in self.lookup_table.items()}
    # Try to return a value for a given key (human readable description)
    # If we are a slider we want to just return an integer reprensentation
    # of a speficied hex value

    def get_desc(self, key):
        if self.is_slider:
            # Convert to clamped in with a fallback of None
            try:
                return max(0, min(100, int(key, 16)))
            except ValueError:
                return None
        else:
            return self.lookup_table.get(key.upper(), None)

    # Try to return a keycode for a description value given
    # If we are a slider we want to just return a hex representation
    # of a speficied decimal number
    def get_keycode(self, value):
        if self.is_slider and value != "status":
            # Clamp int and convert to hex
            try:
                return "{:x}".format(int(max(0, min(100, int(value)))))
            except ValueError:
                return None
        else:
            # Just return status if we are read_only
            if self.read_only:
                return "FF"
            return self.inverse_table.get(value.lower(), None)

    # List all the defined commands
    @staticmethod
    def list():
        print("NAME\tLONG_NAME")
        for i in SerialLookup.lookups:
            print(i.name + "\t" + i.long_name)

    # List all the defined keycodes for a given command
    @staticmethod
    def list_keycodes(command):
        # If len is 2, assume we were passed a raw command (name)
        if (len(command) == 2):
            inst = SerialLookup.get_inst_from_name(command)
        # else assume we were passed a normal command (long_name)
        else:
            inst = SerialLookup.get_inst_from_long(command)

        # Create a tuple list from our dictionary, and sort alphanumerically
        dict_tuple = [(k, v) for k, v in inst.lookup_table.items()]
        dict_tuple.sort()
        # print our list, add some fluff if we are a slider
        print("KEYCODE\tDESCRIPTION")
        for key, value in dict_tuple:
            print("{0}\t{1}".format(key, value))
        if (inst.is_slider):
            print("00-64\t0-100")

    # Try and return an instance of the SerialLookup object that has a given raw name (name)
    @staticmethod
    def get_inst_from_name(name):
        return next((i for i in SerialLookup.lookups if i.name == name.lower()), None)

    # Try and return an instance of the SerialLookup object that has a given name (long_name)
    @staticmethod
    def get_inst_from_long(long_name):
        return next((i for i in SerialLookup.lookups if i.long_name == long_name.lower()), None)


###################################################################################
# Add keycode information here if required                                        #
# Each entry is an instance of SerialLookup and thus needs                        #
# to be initialised with name, long_name and then a dict of keycode and desc      #
###################################################################################
d = {"00": "off",
     "01": "on",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("ka", "power", d))
SerialLookup.lookups.append(SerialLookup("kd", "screen_mute", d))
SerialLookup.lookups.append(SerialLookup("ke", "volume_mute", d))
SerialLookup.lookups.append(SerialLookup("kl", "osd_select", d))
SerialLookup.lookups.append(SerialLookup("km", "remote_lock", d))

d = {"FF": "status"}
SerialLookup.lookups.append(SerialLookup("kf", "volume", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("kg", "contrast", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("kh", "brightness", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("ki", "colour", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("kj", "tint", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("kk", "sharpness", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("kt", "balance", d, is_slider=True))
SerialLookup.lookups.append(SerialLookup("mg", "backlight_lcd", d, is_slider=True))


d = {"01": "4:3",
     "02": "16:9",
     "04": "zoom_1",
     "05": "zoom_2",
     "06": "original",
     "07": "14:9",
     "09": "just_scan",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("kc", "aspect_ratio", d))

d = {"00": "medium",
     "01": "cool",
     "02": "warm",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("ku", "colour_temp", d))


d = {"00": "normal",
     "01": "no_signal",
     "02": "monitor_off_by_remote",
     "03": "monitor_off_by_sleep_time",
     "04": "monitor_off_by_rs232",
     "05": "5v_down",
     "06": "ac_down",
     "07": "monitor_off_by_fan",
     "08": "monitor_off_by_off_timer",
     "09": "monitor_off_by_auto_sleep",
     "0A": "monitor_off_by_av_board",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("kz", "abnormal_state", d, read_only=True))

d = {"01": "inversion",
     "02": "orbiter",
     "04": "white_wash",
     "08": "normal",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("jp", "ism_method_plasma", d))

d = {"00": "0",
     "01": "1",
     "02": "2",
     "03": "3",
     "04": "4",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("jq", "power_saving_plasma", d))

d = {"01": "set"}
SerialLookup.lookups.append(SerialLookup("ju", "auto_configure_vga", d))

# Skipping equalize because its massive
# Skipping tune command because of edge cases


d = {"00": "skip",
     "01": "add",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("mb", "add_skip", d))


d = {"08": "power",
     "0B": "input",
     "F0": "tv_radio",
     "45": "q_menu",
     "43": "menu",
     "AB": "guide",
     "07": "left",
     "06": "right",
     "40": "up",
     "41": "down",
     "44": "ok",
     "28": "return",
     "AA": "info",
     "30": "av_mode",
     "02": "vol_up",
     "03": "vol_down",
     "00": "p_up",
     "01": "p_down",
     "1E": "fav",
     "09": "mute",
     "10": "key_0",
     "11": "key_1",
     "12": "key_2",
     "13": "key_3",
     "14": "key_4",
     "15": "key_5",
     "16": "key_6",
     "17": "key_7",
     "18": "key_8",
     "19": "key_9",
     "53": "list",
     "1A": "q_view",
     "72": "red_key",
     "71": "green_key",
     "63": "yellow_key",
     "61": "blue_key",
     "20": "text",
     "21": "t_option",
     "39": "subtitle",
     "BD": "record",
     "7E": "simplink",
     "79": "ratio",
     "0A": "i_ii",
     "0E": "sleep",
     "26": "time",
     "2A": "reveal",
     "50": "tv_da",
     "62": "update",
     "65": "hold",
     "70": "index"}
SerialLookup.lookups.append(SerialLookup("mc", "ir_key", d))

d = {"00": "digital_tv",
     "10": "analogue_tv",
     "20": "av_1",
     "21": "av_2",
     "22": "av_3",
     "40": "component",
     "60": "vga",
     "90": "hdmi_1",
     "91": "hdmi_2",
     "92": "hdmi_3",
     "FF": "status"}
SerialLookup.lookups.append(SerialLookup("xb", "input_select", d))
