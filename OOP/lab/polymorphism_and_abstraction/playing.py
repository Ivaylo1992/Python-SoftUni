def start_playing(instance):
    return instance.play()

# Test Code
class Children:
 def play(self):
    return "Children are playing"

piano = Children()
start_playing(piano)
# Children are playing

# Test Code
class Guitar:
    def play(self):
        return "Playing the guitar"
guitar = Guitar()
start_playing(guitar)
# Playing the guitar

import unittest


class PlayingTest(unittest.TestCase):
    def test(self):
        class Test:
            def play(self):
                return "test"

        res = start_playing(Test())
        self.assertEqual(res, "test")


if __name__ == '__main__':
    unittest.main()
