import logging
import unittest

from nem13ator import nem13ator


TEST_DATA = 'tests/data/AEMO556810778013NEM13.csv'


class TestNEM13ator(unittest.TestCase):
    '''Tests for NEM13ator'''

    def setUp(self):
        # susspress logging messages
        logging.disable(logging.CRITICAL)

    def test_valid_file_path(self):
        processor = nem13ator.NEM13ator(TEST_DATA)
        self.assertIsInstance(processor, nem13ator.NEM13ator)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            nem13ator.NEM13ator('non/existant/file')

    def process_valid_file(self):
        processor = nem13ator.NEM13ator(TEST_DATA)
        self.assertIsInstance(processor.process, list)
