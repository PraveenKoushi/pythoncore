import unittest


class Metadata(unittest.TestCase):
    a = 100
    b = 200

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compareString(self):
        a = "one"
        b = "one"
        print("Comparing Strings")
        # self.assertIs(a,b,"Both the Strings are not equal")

    def compareNum(self):
        print("Comparing Strings")
        print(self.a)
        print(self.b)
        c=self.a
        d=self.b
        #self.assertEquals(self.a, self.b, "numbers are equal")
        #self.assertEquals(c,d,"Not Equal")
        print("a and b values are".format(c,d))


obj = Metadata(5, 5)
# obj.compareString(self="Hi")
obj.compareNum()
