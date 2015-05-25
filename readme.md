Twitch.py
=========

:video_game: Twitch on the Shell :toilet:

## About

Ever wanted to check out Twitch streams without going to their horribly 
bloated, javascript-ridden website? Well now you can!

Thanks to the power of the Twitch JSON API (that barely works) we can 
check frontpage games, streams and so on all from the command line!

The program works in tangent with Livestreamer, so if you have Livestreamer 
installed you can boot streams directly into Livestreamer.

## Usage

The program initially starts with the front page of Twitch, so that it just 
tells you what the Top Games on Twitch currently are. To do that just run the 
program (you need Python in your $PATH to run it as an executable)
```
$ ./twitch.py
```

This will show you the top 10 games on Twitch right now. From here you will 
be asked to input a number to pick which game's directory you want to check out.

Once you pick a directory, you can select a stream to boot into Livestreamer 
(if you have Livestreamer installed that is)

If you want to show more games/streams, use the -l option to pick more
```
$ ./twitch.py -l 20
```

If you want a game's listing immediately, you can use this option
```
$ ./twitch.py -g <game>
```

Where 'game' is the game you want to check out, ie:
```
$ ./twitch.py -g Dota 2
```
No quotes required.

You can mix and match these options.
```
$ ./twitch.py -l 20 -g Dota 2
```

## Installation

Included are some scripts to install Twitch.py to your $PATH location, where 
you can call it globally across your shell. Pick the script for your system 
appropriately.

Once it's installed, you can run 
```
$ twitch
```
without needing the .py extension

This only works on Linux at the moment, not implemented for OSX/Windows yet.

## Uninstallation

You can run the uninstall scripts to remove Twitch from the $PATH locations.

Be sure to check the MD5 values before running these scripts.

* uninstall_linux: 478da7b83f9f65356fc50b9155d5efac 

## Requirements

* Python 3
* Requests (optional)
* Livestreamer (optional)

No support for Python 2 is planned.

## Problems

Report any issues to the Issue Tracker, or check the FAQ for anything else.

:toilet:
