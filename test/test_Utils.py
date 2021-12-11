import sys
sys.path.append("./src/")
import unittest
from datetime import datetime
from undefined.Utils import time

class TestUDFunction(unittest.TestCase):
    def test_time(self):
        now = datetime.now()
        self.assertEqual(time()[:8], now.strftime("%H:%M:%S:%f")[:8])