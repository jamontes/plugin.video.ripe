#!/usr/bin/env python
'''
This module contains unit tests and integration tests.
'''

import os
import sys
import unittest
# update path so we can import the lib files.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

import resources.lib.ripe_api as api

class ITTests(unittest.TestCase):

    def test_events(self):
        event_list = api.get_events()
        self.assertTrue(event_list is not None and len(event_list) > 20)

    def test_list_all_videos(self):
        url='https://ripe84.ripe.net/archives/'
        video_items = api.get_videolist(url)
        self.assertTrue(len(video_items) > 50)
        self.assertTrue(len(video_items[0]['url']) > 30)
        self.assertTrue(len(video_items[0]['title']) > 1)

    def test_video_scraper1(self):
        url='https://ripe84.ripe.net/archives/video/863'
        self.assertTrue(len(api.get_playable_url(url)) > 10)

    def test_video_scraper2(self):
        url='https://ripe63.ripe.net/videos/ripe_pc-ripe_pc-20111104-113012.mp4'
        self.assertTrue(len(api.get_playable_url(url)) > 10)


if __name__ == '__main__':
        unittest.main()
