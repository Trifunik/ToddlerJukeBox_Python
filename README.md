# ToddlerJukeBox_Python

# How to start service
  sudo cp vlc.service /etc/systemd/user
  systemctl --user enable vlc.service 
  systemctl --user start vlc.service 
  
  systemctl --user status vlc.service 
  