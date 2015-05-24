Twitch.py
=========

:video_game: Twitch on the Shell :toilet:

## About

Ever wanted to check out Twitch streams without going to their horribly 
bloated, javascript-ridden website? Well, now you can!

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

This will show you the top 10 games on Twitch right now. If you want more, 
set the limit to an amount desired.
```
$ ./twitch.py -l 20
```

If you want a game's listing immediately, you can use this option
```
$ ./twitch.py -g <game>
```

Where <game> is the game you want to check out, ie:
```
$ ./twitch.py -g Dota 2
```
No quotes required.

You can mix and match these options.
```
$ ./twitch.py -l 20 -g Dota 2
```

## Installation

You can install Twitch.py to your binary $PATH, the code has some functionality
to install it for us
```
$ ./twitch.py -i
```
This will run an install function that will run code to copy the file to a 
place where you can run it globally on your shell.

This only works on Linux at the moment, not implemented for OSX/Windows yet.

## Requirements

* Python 3
* Requests (optional)
* Livestreamer (optional)
i
I plan on porting it to Python 2, as it shouldn't be too painful to do, and I'm 
sure most people haven't moved on to Python 3 yet.

## Problems

Report any issues to the Issue Tracker, or check the FAQ for anything else.

:toilet:
