import unittest
from __init__ import states


class StatesTest(unittest.TestCase):
    '''tests state abbreviation function'''

    def statestest(self):
        self.assertEqual(states(['Florida']), 'FL')


if __name__ == '__main__':
    unittest.main()

