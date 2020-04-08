from csv_batch import read
import unittest
import math


class TestRead(unittest.TestCase):
    def setUp(self) -> None:
        self.file = "tests/data/player_stats.csv"
        self.total_lines = 51

    def test_batches(self):
        batch_size = 10
        batches = read(self.file, batchsize=batch_size)
        batch_count = 0
        for _ in batches:
            batch_count += 1
        assert batch_count == math.ceil(self.total_lines / batch_size)

    def test_no_batch(self):
        batches = read(self.file)
        batch_count = 0
        for batch in batches:
            batch_count += 1
        assert batch_count == 1
        assert len(batch) == 51
