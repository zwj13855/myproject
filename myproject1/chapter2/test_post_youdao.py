import unittest
from unittest import mock
from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        #import time
        #t=time.time()
        #ts=str(int(round(t * 1000)))
        #print(ts)
        get_ts=mock.Mock(return_value='1586175414453')
        self.assertEqual('1586175414453',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15861754144531')
        self.assertEqual('15861754144531',get_salt())

    def test_get_sign(self):
        get_sign=mock.Mock(return_value='3350c61a4bfbe43a2de36a670add6cb5')
        self.assertEqual('3350c61a4bfbe43a2de36a670add6cb5',get_sign())


if __name__ == '__main__':
    unittest.main()
