import logging
import sys
import unittest

from rainfall import rainfall

logger = logging.getLogger()
logger.level = logging.DEBUG


class RainfallTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RainfallTestCase, self).__init__(*args, **kwargs)
        self.test_set = [
            {"test": [5, 1, 2, 1, 4], "answer": 8},
            {"test": [3, 2, 1], "answer": 0},
            {"test": [3, 1, 4, 1, 1, 0], "answer": 2},
            {"test": [1, 2, 3, 1, 2, 1, 0, 0, 3, 4, 3, 1], "answer": 11},
        ]

    def setup(self):
        pass

    def test_rainfall(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        for test in self.test_set:
            self.assertEqual(rainfall(test["test"]), test["answer"])


if __name__ == "__main__":
    unittest.main()
