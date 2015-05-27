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

## Installation

_setup.py_ is a Distutils installer, in order to install this package system-wide, 
try using:
```
$ python setup.py install
```

This will require administrator privileges (so it may require a _sudo_ on Unix)

## Usage


```
$ twitch.py
```

This will show you the top 20 games on Twitch right now. From here you will 
be asked to input a number to pick which game's directory you want to check out.

Once you pick a directory, you can select a stream to boot into Livestreamer 
(if you have Livestreamer installed that is)

If you want to show more games/streams, use the -l option to pick more
```
$ twitch.py -l 30
```

If you want a game's listing immediately, you can use this option
```
$ twitch.py -g <game>
```

Where 'game' is the game you want to check out, ie:
```
$ twitch.py -g Dota 2
```
No quotes required.

You can mix and match these options.
```
$ twitch.py -l 30 -g Dota 2
```

## Uninstallation

Twitch.py should be uninstalled through your system's normal uninstallation 
methods.

* Windows: Control Panel > Add or Remove Software
* Linux: apt-get (Debians), rpm (Fedoras), pacman (Archlinux)
* OSX: No clue, HELP

## Requirements

* Python 3
* Requests (optional)
* Livestreamer (optional)

No support for Python 2 is planned.

## Problems

Report any issues to the Issue Tracker, or check the FAQ for anything else.

:toilet:
