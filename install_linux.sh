#!/bin/sh
echo "Installing Twitch.py to /usr/bin/twitch..."
echo "If you don't trust this software, don't provide sudo information"

sudo cp ./twitch.py /usr/bin/twitch
sudo chmod +x /usr/bin/twitch

if [ -f "/usr/bin/twitch" ]; then
    echo "Twitch.py was successfully installed"
else
    echo "Failed to install Twitch.py"
    exit 1
fi
exit 0
