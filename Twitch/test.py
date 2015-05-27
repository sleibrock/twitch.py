#!/usr/bin/python3
#-*- coding: utf-8 -*-

from unittest import main, TestCase
from lib import *

"""
Unit Test for Twitch
This Docstring will list all possible unit tests
In some cases some things can not be fixed even with testing
---

Test 1:
    Do the front-page games go in Order By *Viewer*?
    Additionally, do we fetch at least 10 games (the default)?

    Solution: Draw a number of games and determine if they are already sorted

Test 2:
    Do we retrieve a number of streams equal to the *Limit* variable?

    Solution: Count the number of streams returned by the API

Test 3:
    Do all games add up (relatively close) to their total viewers?

    Solution: fetch up to 100 games and total up the viewers
"""

class TwitchTest(TestCase):

    def setUp(self):
        print("Beginning Unit test...")
        print("----------------------")

    def tearDown(self):
        print("Ending Unit test...")
        print("----------------------")

    def test_front_page(self):
        print("Testing front page...")
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
        print("Successfully got 10 games")

    def test_limit_count(self):
        print("Testing data retrieval...")
        url = "{0}{1}?q=Dota%222&limit={2}".format(API_URL, SEARCH_STR, "{0}")
        s = 0
        expected = sum(range(10,110,10))
        for x in range(10,110,10):
            print("Grabbing {0} streams...".format(x))
            blob = load_url(url.format(x))
            urls = [u['channel']['url'] for u in blob['streams']]
            print("\tGot {0} streams".format(len(urls)))
            s += len(urls) 

        print("Got {0} out of {1} streams".format(s, expected))
        print("Success rate: %{0}".format(str((s/expected)*100)[:5]))
        self.assertEqual(s, expected)

    def test_games_matching_viewers(self):
        pass

if __name__ == "__main__":
    main()
