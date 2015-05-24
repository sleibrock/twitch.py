#!/bin/sh
echo "Attempting to remove Twitch.py from /usr/bin..."
echo "Be sure to check the integrity of this file before removing"
echo "Input your sudo information to do this operation"
sudo rm /usr/bin/twitch

if [ -f "/usr/bin/twitch" ]; then
    echo "Twitch.py was not removed"
    echo "Consult the Readme for more info"
    exit 1
else
    echo "Twitch.py was removed successfully"
fi
exit 0
