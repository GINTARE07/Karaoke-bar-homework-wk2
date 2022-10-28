import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Happy")
    
        
    def test_song_has_name(self):
        self.assertEqual("Happy", self.song.song_name)
    

