Changelog
=========

# 1.4.0

* Adding webbrowser support for non-livestreamer devices

# 1.3.1

* Fixing code to support automatic best-quality

# 1.3.0

* Supports Python 2
* Removes non-printable characters (according to string.printable)
* Strips trailing whitespace from printed listings

# 1.2.2

* Fixing issue with improper importing
* Removed unnecessary imports from app.py

# 1.2.0

Implementing Distutils as the main way of installing Twitch.py

* Removed shell scripts, as Distutils now replaces that method
* Moved twitch.py into it's own package folder
* Split up code from twitch.py into lib.py
* Added info to Twitch/info.py
* Removed debug options from all code, including -d/--debug
* Moved unit testing into Twitch/ package
* Added dist folder, this will store older package tarballs

# 1.1.0

Most recent minor version yet. Starting changelog here.

* Ability to access Twitch's JSON API
* Can select streams to load into Livestreamer
* Can pick games directly via --game option
* Can limit amount of listings via --limit option
