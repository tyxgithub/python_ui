import unittest
from testCode.BaseTestCase import *
from testCode.test1 import testa


class testb(unittest.TestCase):
    def test_01(self):
        print ("这是第三个测试")
        self.assertEqual(1,1)


if __name__=='__main__':
    unittest.main()