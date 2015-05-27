#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
lib.py
Essential functions/vars to Twitch.py go here
"""

__author__  = 'Steven Leibrock'
__email__   = 'leibrockoli@gmail.com'
__version__ = '1.2.0'

# Constants
API_URL                = 'https://api.twitch.tv/kraken'
TOP_GAMES              = '/games/top'
SEARCH_STR             = '/search/streams'
DEFAULT_LIMIT          = 20
LIVESTREAMER_INSTALLED = True
REQUESTS_INSTALLED     = True
CHAR_LIMIT             = 50

# If Livestreamer is installed, will check to figure out where it is
# Livestreamer installs are in different places based on the OS
LIVESTREAMER_PATH = '/usr/bin/livestreamer'
POSSIBLE_PATHS = ['/usr/bin/livestreamer', '/usr/local/bin/livestreamer']

# Try loading the Requests library
try:
    from requests import get as re_get
except ImportError as e:
    print('Error: {0}'.format(e))
    print('Requests not installed, to install it you can run:')
    print('\n  pip install requests\n')
    print('Defaulting to urllib...')
    from urllib import urlopen
    from json import loads as json_load
    REQUESTS_INSTALLED = False

# Try loading Livestreamer (if failed, tell them how to get)
try:
    from livestreamer import streams as StreamData
    from livestreamer import __version__ as LSV

    # Try to locate where Livestreamer is installed
    from os.path import isfile as where_is_file
    for path in POSSIBLE_PATHS:
        if where_is_file(path):
            LIVESTREAMER_PATH = path
except Exception as e:
    print('Error: {0}'.format(e))
    print('Livestreamer not installed, to install it you can run:')
    print('\n  pip install livestreamer\n')
    LIVESTREAMER_INSTALLED = False


def limit_string(s):
    '''
    Limit a string to the CHAR_LIMIT
    :s is the input string
    '''
    # Daft Punk song variable for extra credit
    too_long = ".." if len(s) > CHAR_LIMIT else ""
    return "{0}{1}".format(s[:CHAR_LIMIT], too_long)


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
    Subtract 1 at the end to make it from [0:(maxv-1)]
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
    # Scan the URL for qualities
    print('Loading {0} ...\n'.format(url))
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
    print('Fetching main Twitch.tv directory...')
    print('Press CTRL+C to quit\n')
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
    print('Getting streams for "{g}"'.format(g=game))
    print('Press CTRL+C to quit\n')
    search_key = game.lower().replace(' ', '%20')
    search_url = '{b}{q}?q=%22{g}%22&limit={l}'.format(
        b=API_URL, q=SEARCH_STR, g=search_key, l=limit)
    blob = load_url(search_url)
    urls = [u['channel']['url'] for u in blob['streams']]
    highest_views = max([len("{0:,}".format(v['viewers'])) for v in
                         blob['streams']])
    for i, stream in enumerate(blob['streams']):
        print('{n:>{f}}) {s: <{cl}}  [viewers: {v:{mv},}]'.format(
                s=limit_string(stream['channel']['status']),
                n=i+1, v=stream['viewers'], f=len(str(DEFAULT_LIMIT)),
                cl=CHAR_LIMIT+2, mv=highest_views))

    if not LIVESTREAMER_INSTALLED:
        print('\n{0}\n!! Livestreamer is not installed !!\n{0}'.format('*'*10))
        return False

    inp = get_input('Select stream> ', 'Try again', len(urls))
    return load_into_livestreamer(urls[inp])

# end