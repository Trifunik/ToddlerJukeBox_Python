
import sys
import csv
import subprocess
from evdev import InputDevice, categorize, ecodes
from python_telnet_vlc import VLCTelnet

dev = InputDevice(sys.argv[1])
file_path = sys.argv[2]

scancodes = {
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r',
    20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
    50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 57: u' ', 100: u'RALT'
}
dev.grab()

v = VLCTelnet("127.0.0.1", "password", 4212)

value = ""
old_value = ""

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        data = categorize(event)       
        if data.keystate == 1:

            if data.scancode == 28:              
                file = open(file_path, mode='r')
                csv_reader = csv.reader(file, delimiter=';')
                for row in csv_reader:
                    if row[0] == value:
                        if row[1] == "shutdown":
                            proc = subprocess.Popen('shotdown now', shell=True)
                        elif row[1] == "pause":
                            v.pause()
                        elif row[1] == "stop":
                            v.stop()
                            v.clear()
                            old_value = ""
                        elif row[1] == "play":
                            v.play()
                        
                        elif value != old_value:
                            old_value = value
                            v.add(row[1])
                            v.play()
                value=""
                
            else:
                value += u'{}'.format(scancodes.get(data.scancode))
