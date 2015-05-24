#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
# Twitch.py - Twitch on the CLI

## About

Ever wanted to check what Twitch streams are on
without going to Twitch's web page? Now you can!

With this tool you can see what streams are on,
how many viewers, and even boot a URL into
Livestreamer if you have it installed!

## Usage

Simply run the file.
```
twitch.py
```

This will open up the program. If you want a specific game try
```
twitch.py -g <name of game>
```

## Requirements

- Python 3
- Requests library (from Pip) (optional)
- Livestreamer (from Pip)
- Internet (please god have internet)

## Installing

Pass the file an -i or --install to run install code.
(Only works on *nix so far)
'''

__author__ = 'Steven Leibrock'
__email__ = 'leibrockoli@gmail.com'
__version__ = '1.1.1'

from argparse import ArgumentParser
from subprocess import call

# Constants
API_URL = 'https://api.twitch.tv/kraken'
TOP_GAMES = '/games/top'
SEARCH_STR = '/search/streams'
DEFAULT_LIMIT = 10
LIVESTREAMER_INSTALLED = True
REQUESTS_INSTALLED = True
CHAR_LIMIT = 50
DEBUG = False

# Livestream qualities
# Set USE_AUTO_QUALITY to False if you want to select quality
# instead of using AUTO_QUALITY automatically
USE_AUTO_QUALITY = True
AUTO_QUALITY = 'source'

# If on a Windows platform, you will probably
# need to change this path to where Livestreamer.exe is
LIVESTREAMER_PATH = '/usr/bin/livestreamer'
POSSIBLE_PATHS = ['/usr/bin/livestreamer', '/usr/local/bin/livestreamer']

# Try loading the Requests library
try:
    from requests import get as re_get
except ImportError as e:
    print('Error: {0}'.format(e))
    print('Requests not installed, to install it you can run:')
    print('\n\tpip install requests')
    print('Defaulting to urllib')
    from urllib import urlopen
    from json import loads as json_load
    REQUESTS_INSTALLED = False

# Try loading Livestreamer (if failed, tell them how to get)
try:
    print('Checking for Livestreamer...')
    from livestreamer import streams as StreamData
    from livestreamer import __version__ as LSV
    print('Livestreamer version: {v}'.format(v=LSV))

    # Try to locate where Livestreamer is installed
    from os.path import isfile as where_is_file
    for path in POSSIBLE_PATHS:
        if where_is_file(path):
            LIVESTREAMER_PATH = path
except Exception as e:
    print('Error: {0}'.format(e))
    print('Livestreamer not installed!')
    print('To install Livestreamer, run the following code:\n')
    print('\n   pip install livestreamer')
    LIVESTREAMER_INSTALLED = False


def install_file():
    '''
    Install the twitch.py file to user binaries
    POSIX : install to /usr/bin
    MSDOS : install to C:/Windows/System32 (?)
    OSX   : No ty
    '''
    from os import name as os_name
    from os.path import dirname, realpath, join

    if os_name == 'posix':
        fname = __file__.split('/').pop()
        process = ['sudo', 'cp',
                   join(dirname(realpath(__file__)), fname),
                   '/usr/bin/{0}'.format(fname)]
        print('Activating "{0}"'.format(' '.join(process)))
        call(process)
        chmod = ['sudo', 'chmod', '+x', '/usr/bin/{0}'.format(fname)]
        print('Activating "{0}"'.format(' '.join(chmod)))
        call(chmod)
    else:
        print("Can't install twitch.py on this system automatically")
        return False
    return True


def limit_string(s):
    '''
    Limit a string to the CHAR_LIMIT
    :s is the input string
    '''
    return "{0}..".format(s[:CHAR_LIMIT])


def load_url(url):
    '''
    Return a dictionary of the JSON
    This function will either use urllib or requests
    based on what's installed
    '''
    if REQUESTS_INSTALLED:
        return re_get(url).json()
    return json_load(urlopen(url).read().decode('utf-8'))


def get_input(disp_str, err_str, maxv):
    '''
    Fetch input from the user and return the number given
    '''
    inp = None
    while inp is None:
        try:
            inp = int(input(disp_str))
            if inp < 1 or inp > maxv:
                inp = None
        except ValueError:
            print(err_str)
    return inp - 1


def load_into_livestreamer(url):
    '''
    Load a URL into Livestreamer
    :url is the target URL to load
    '''
    print('Loading {0} ...\n'.format(url))

    # Check for USE_AUTO_QUALITY
    if USE_AUTO_QUALITY:
        print('Using auto-quality "{0}" ...\n'.format(AUTO_QUALITY))
        q = AUTO_QUALITY
    else:
        # Scan the URL for qualities
        qualities = StreamData(url)
        names = [q.lower() for q in qualities.keys()]
        for i, q in enumerate(names):
            print('[{ind}] {qual}'.format(ind=i+1, qual=q))
        inp = get_input('Enter quality> ', 'Try again', len(names))
        print('Using quality "{0}" ...\n'.format(names[inp]))
        q = names[inp]
    call([LIVESTREAMER_PATH, url, q])
    return True


def main_directory(limit):
    '''
    Fetch the top games on Twitch
    :limit determines how many results will be fetched
    '''
    print('Fetching main Twitch.tv directory...\n')
    url = '{0}{1}?limit={2}'.format(API_URL, TOP_GAMES, limit)
    blob = load_url(url)
    longest = max([len(g['game']['name']) for g in blob['top']])
    game_titles = [g['game']['name'] for g in blob['top']]
    for i, game_blob in enumerate(blob['top']):
        print('{n:>{fill2}}) {gt:<{fill}}   [viewers: {vc:7,}, chans: {cc:5,}]'.
              format(gt=game_blob['game']['name'], vc=game_blob['viewers'],
                     cc=game_blob['channels'], fill=longest, n=i+1,
                     fill2=len(str(DEFAULT_LIMIT))))
    inp = get_input('Enter number> ', 'Try again', len(game_titles))
    return scan_game_directory(game_titles[inp], limit)


def scan_game_directory(game, limit):
    '''
    Scan game directory
    :game is the game streams to find
    :limit is how many to fetch
    This code also includes input to select Stream to open
    '''
    print('Getting streams for "{g}"\n'.format(g=game))
    search_key = game.lower().replace(' ', '%20')
    search_url = '{b}{q}?q=%22{g}%22&limit={l}'.format(
        b=API_URL, q=SEARCH_STR, g=search_key, l=limit)
    blob = load_url(search_url)
    urls = [u['channel']['url'] for u in blob['streams']]
    highest_views = max([len("{0:,}".format(v['viewers'])) for v in
                         blob['streams']])
    print('Total streams: {0}'.format(blob['_total']))
    print('Total fetched: {0}\n'.format(len(blob['streams'])))
    for i, stream in enumerate(blob['streams']):
        print('{n:>{f}}) {s: <{cl}}  [viewers: {v:{mv},}]'.format(
                s=limit_string(stream['channel']['status']),
                n=i+1, v=stream['viewers'], f=len(str(DEFAULT_LIMIT)),
                cl=CHAR_LIMIT+2, mv=highest_views))

    if not LIVESTREAMER_INSTALLED:
        print('{0}\n!! Livestreamer is not installed !!\n{0}'.format('*'*10))
        return False

    inp = get_input('Select stream> ', 'Try again', len(urls))
    return load_into_livestreamer(urls[inp])

if __name__ == '__main__':
    parser = ArgumentParser(
        description='Interact with Twitch.tv',
        prog='twitch.py')
    parser.add_argument('-g', '--game', type=str, nargs='+', metavar='GAME',
                        help='The game whose directory you wish to scan')
    parser.add_argument('-l', '--limit', type=int, default=DEFAULT_LIMIT, 
                        metavar='LIM', help='Number of streams to fetch')
    parser.add_argument('-i', '--install', const=True, default=False,
                        action='store_const', help='Install the file')
    parser.add_argument('-d', '--debug', help='Debug the program',
                        action='store_const', default=False, const=True)
    parser.add_argument('-v', '--version',action='version',
                        version='%(prog)s ver.{0}'.format(__version__))
    parser.add_argument('-q', '--qual', const=True, default=False,
                        action='store_const', help='Disable auto-quality')
    try:
        args = parser.parse_args()
        print(args)

        # Check for a file install
        if args.install:
            was_installed = install_file()
            if was_installed:
                print("Twitch.py has been installed!")
            else:
                print("Twitch.py failed to install")
            quit()
        if args.game is None or args.game == '':
            main_directory(args.limit)
        else:
            scan_game_directory(' '.join(args.game), args.limit)
    except KeyboardInterrupt as e:
        print('\nQuitting...')
    except Exception as e:
        print("Error encountered: {0}".format(e))
    print('\nAll done!')

# end
