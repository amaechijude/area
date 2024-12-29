from main import Area
from unittest import TestCase

class TestArea(TestCase):
    def setUp(self):
        self.area = Area()

    def test_square(self):
        self.assertEqual(self.area.square(2), 4.0)
        self.assertEqual(self.area.square(3), 9.0)
        self.assertNotEqual(self.area.square(2),5.0)

    def test_rectangle(self):
        self.assertEqual(self.area.rectangle(2,3), 6.0)
        self.assertNotEqual(self.area.rectangle(2,3), 7.0)