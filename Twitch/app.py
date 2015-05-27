#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Twitch.py - Twitch on the CLI
See readme.md for more info
'''

from argparse import ArgumentParser
from subprocess import call
from Twitch.info import __version__
from Twitch.lib import *


def main(*args, **kwargs):
    """
    Runner main function
    """
    parser = ArgumentParser(
        description='Interact with Twitch.tv',
        prog='twitch.py')
    parser.add_argument('-g', type=str, nargs='+', metavar='text',
                        help='The game whose directory you wish to scan')
    parser.add_argument('-l', '--limit', type=int, default=DEFAULT_LIMIT, 
                        metavar='LIM', help='Number of streams to fetch')
    parser.add_argument('-v', '--version',action='version',
                        version='%(prog)s ver.{0}'.format(__version__))
    try:
        args = parser.parse_args()
        if args.g is None or args.g == '':
            main_directory(args.limit)
        else:
            scan_game_directory(' '.join(args.g), args.limit)
    except KeyboardInterrupt as e:
        print('\nQuitting...')
    except Exception as e:
        print("Error encountered: {0}".format(e))
    print('\nAll done!')


if __name__ == '__main__':
    main()
# end
