import unittest
from activities import eat, nap, is_funny, laugh     #import functions you need to test

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("broccoli", is_healthy=True),
            "I'm eating broccoli, because it's healthy"
        )

    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because I like it"
        )

    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""      # can add docstring; docstring will be visible if executing script 298unittest.py -v
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3), "Ugh I overslept.  I didn't mean to nap for 3 hours!"
        )

    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False)
        # self.assertFalse(is_funny("tim"), "tim should not be funny")

    def test_is_funny_anyone_else(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        """laugh returns a laughing string"""
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

if __name__=="__main__":
    unittest.main()
