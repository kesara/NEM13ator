import logging
import os
import unittest

from nem13ator import nem13ator
from data.migrations.db_0000_initial import main as db


TEST_DATA = 'tests/data/AEMO556810778013NEM13.csv'
TEST_DB = 'tests/data/test.db'


class TestNEM13ator(unittest.TestCase):
    '''Tests for NEM13ator'''

    def setUp(self):
        # susspress logging messages
        logging.disable(logging.CRITICAL)

        # delete database file if exits
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

        # initiate test database
        db(TEST_DB)

    def test_valid_file_path(self):
        processor = nem13ator.NEM13ator(TEST_DATA, TEST_DB)
        self.assertIsInstance(processor, nem13ator.NEM13ator)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            nem13ator.NEM13ator('non/existant/file', TEST_DB)

    def process_valid_file(self):
        processor = nem13ator.NEM13ator(TEST_DATA, TEST_DB)
        self.assertIsInstance(processor.process, int)
        self.assertEqual(processor.process, 10)
