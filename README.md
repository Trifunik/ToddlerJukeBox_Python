# ToddlerJukeBox
Toddlers can be their own DJ with RFID cards

## What is it?
This is a short Python script that reads the ID number from an NFC card and plays the corresponding folder link using the VLC media player.
The script is started by a service in the background. The communication with VLC is done via telnet.

## Pre-conditions?
### Python
1. pip install python-telnet-vlc
2. pip install evdev
3. in toddlerjukebox.service set the path to ToddlerJukeBox.py, RFID reader and the playlist
4. cp toddlerjukebox.service /etc/systemd/system
5. enable and start the service

### VLC media player
1. To enable telnet control of VLC, open VLC, go to Tools > Preferences, show "All" settings, and enable the "Telnet" interface in the "Interface" section, then set a password. 
2. cp vlc.service /etc/systemd/user


## How does it work?
The script is started by the service. It waits till for VLC to start. Each RFID card has an ID that corresponds to a path in the text file that is used as a database; the IDs and the corresponding links must to be separated by semicolons.
The file has to look like follows:
```
<ID>;<LINK>;
<ID>;stop;      // to stop the play list
<ID>;shutdowm;  // turn off the computer if Node-RED runs as sudo
```

## How to get the ID?
The card reader is recognised by the operating system as a keyboard. All you need to do is open an editor and place the card on the reader. You will immediately see the ID number.
