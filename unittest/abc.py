# import unittest2
#
# class TestGame(unittest2.TestCase):
#     def test_input(self):
#         pass
#
#
# TestGame.test_input("Hi")
#
#

from unittest import TestCase


class TestGame(TestCase):
    def setUp(self):
        print("Initiating objects")

    def comp(self, one, two):
        TestCase.assertEqual(one,two)


# tg = TestGame()
# tg.comp("Praveen", "Praveen")

if __name__ == '__main__':
    TestCase.main()
