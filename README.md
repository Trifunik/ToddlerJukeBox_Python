# ToddlerJukeBox_Python

# Setup
1. Set telnet in VLC
2. Add VLC to /etc/xdg/autostart/
3. Set python script as unser 
  sudo cp vlc.service /etc/systemd/user
  systemctl --user enable vlc.service 
  systemctl --user start vlc.service 
  
  systemctl --user status vlc.service 
  