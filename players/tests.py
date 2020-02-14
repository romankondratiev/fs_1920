from django.test import TestCase
from .models import Player

class PlayerTestCase(TestCase): #Test Case for object creation

    def setUp(self):
        Player.objects.create(
        name="test", 
        age=100,
        photo="test", 
        nationality="test", 
        overall=100, 
        club="test", 
        value="test", 
        position="test", 
        value_int=100 )

        Player.objects.create(
		name="test_second",
		age=200,
		photo="test_second",
		nationality="test_second", 
		overall=200,
		club="test_second", 
		value="test_second",
		position="test_second", 
		value_int=200 )

    def test_players(self):
        first = Player.objects.get(age=100)
        second = Player.objects.get(age=200)
        self.assertEqual(first, 'test')
        self.assertEqual(second, 'test_second')

