#!/usr/bin/python3
#-*- coding: utf-8 -*-

from unittest import main, TestCase
from twitch import *

class TwitchTest(TestCase):

    def test_front_page(self):
        url = "{0}{1}".format(API_URL, TOP_GAMES)
        blob = load_url(url)
        count = 0
        previous_views = None
        for gobj in blob['top']:
            count += 1
            print("{0}: {1}".format(count, gobj['game']['name']))
            if previous_views is not None:
                self.assertTrue(previous_views > int(gobj['viewers']))
            previous_views = int(gobj['viewers'])
        self.assertEqual(count, 10)

    def test_limit_count(self):
        pass

    def test_games_matching_viewers(self):
        pass

if __name__ == "__main__":
    main()
