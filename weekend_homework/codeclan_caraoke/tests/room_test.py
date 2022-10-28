import unittest

from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("room_1", 30)
    
    def test_add_guest(self):
        garry = Guest("Garry", 40)
        self.room_1.add_guest(garry)
        self.assertEqual(1,len(self.room_1.guests))
    

    
