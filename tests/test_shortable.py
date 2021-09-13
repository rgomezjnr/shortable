#!/usr/bin/env python 

import unittest
import logging

from shortable import shortable

#class TestValidReadOldShortStatus(unittest.TestCase):
#    def setUp(self):
#        self.shortable = shortable.Shortable()
#        self.file_name = 'valid_shortable.json'
#
#    def test_valid_read_old_short_status(self):
#        self.shortable.read_old_short_status('valid_shortable.json')
#        self.assertIs(self.old_short_status, dict)
#        self.assertGreaterEqual(len(self.shortable.read_old_short_status), 1)
#
#    def tearDown(self):
#        self.shortable
#        self.file_name

#class TestInvalidReadOldShortStatus(unittest.TestCase):
#    def setUp(self):
#        self.shortable = shortable.Shortable()
#        self.file_name
#
#    def test_invalid_read_old_short_status(self):
#        self.shortable.read_old_short_status('invalid_old_short_status_not_dict.json')
#        self.shortable.read_old_short_status('invalid_shortable_less_than_1_asset.json')
#        self.shortable.read_old_short_status('invalid_shortable_empty.json')
#        self.assertRaises(shortable database is not type dict)
#        self.assertRaises(shortable database length less than 1)
#
#    def tearDown(self):
#        self.shortable
#        self.file_name

class TestNonShortableToShortable(unittest.TestCase):
    def setUp(self):
        self.shortable = shortable.Shortable()
        self.shortable.old_short_status = {'AMZN': False, 'MSFT': False, 'TSLA': False}
        self.shortable.new_short_status = {'AMZN': True, 'MSFT': True, 'TSLA': True}
        self.expected_report = 'AMZN now shortable\nMSFT now shortable\nTSLA now shortable\n'

    def test_non_shortable_to_shortable(self):
        self.shortable.check_short_status_changes()
        self.assertEqual(self.shortable.old_short_status, self.shortable.new_short_status)
        self.assertEqual(self.shortable.report, self.expected_report)

    def tearDown(self):
        del self.shortable
        del self.expected_report

class TestShortableToNonShortable(unittest.TestCase):
    def setUp(self):
        self.shortable = shortable.Shortable()
        self.shortable.old_short_status = {'AMZN': True, 'MSFT': True, 'TSLA': True}
        self.shortable.new_short_status = {'AMZN': False, 'MSFT': False, 'TSLA': False}
        self.expected_report = 'AMZN now non-shortable\nMSFT now non-shortable\nTSLA now non-shortable\n'

    def test_shortable_to_non_shortable(self):
        self.shortable.check_short_status_changes()
        self.assertEqual(self.shortable.old_short_status, self.shortable.new_short_status)
        self.assertEqual(self.shortable.report, self.expected_report)

    def tearDown(self):
        del self.shortable
        del self.expected_report

class TestNoneToShortable(unittest.TestCase):
    def setUp(self):
        self.shortable = shortable.Shortable()
        self.shortable.old_short_status = {'AMZN': None, 'MSFT': None, 'TSLA': None}
        self.shortable.new_short_status = {'AMZN': True, 'MSFT': True, 'TSLA': True}
        self.expected_report = 'AMZN now shortable, previous status unknown\nMSFT now shortable, previous status unknown\nTSLA now shortable, previous status unknown\n'

    def test_none_to_shortable(self):
        self.shortable.check_short_status_changes()
        self.assertEqual(self.shortable.old_short_status, self.shortable.new_short_status)
        self.assertEqual(self.shortable.report, self.expected_report)

        for asset in self.shortable.old_short_status:
            self.assertIsNotNone(asset)

    def tearDown(self):
        del self.shortable

class TestNoneToNonShortable(unittest.TestCase):
    def setUp(self):
        self.shortable = shortable.Shortable()
        self.shortable.old_short_status = {'AMZN': None, 'MSFT': None, 'TSLA': None}
        self.shortable.new_short_status = {'AMZN': False, 'MSFT': False, 'TSLA': False}
        self.expected_report = 'AMZN now non-shortable, previous status unknown\nMSFT now non-shortable, previous status unknown\nTSLA now non-shortable, previous status unknown\n'

    def test_none_to_non_shortable(self):
        self.shortable.check_short_status_changes()
        self.assertEqual(self.shortable.old_short_status, self.shortable.new_short_status)
        self.assertEqual(self.shortable.report, self.expected_report)

        for asset in self.shortable.old_short_status:
            self.assertIsNotNone(asset)

    def tearDown(self):
        del self.shortable

class TestNoShortableStatusChange(unittest.TestCase):
    def setUp(self):
        self.shortable = shortable.Shortable()
        self.shortable.old_short_status = {'AMZN': True, 'MSFT': True, 'TSLA': True}
        self.shortable.new_short_status = {'AMZN': True, 'MSFT': True, 'TSLA': True}
        self.expected_log = ['INFO:root:No change to shortable status of AMZN',
                             'INFO:root:No change to shortable status of MSFT',
                             'INFO:root:No change to shortable status of TSLA']

    def test_no_shortable_status_change(self):
        with self.assertLogs('root', level='INFO') as cm:
            self.shortable.check_short_status_changes()
            logging.getLogger('root').info('No change to shortable status of AMZN')
            logging.getLogger('root').info('No change to shortable status of MSFT')
            logging.getLogger('root').info('No change to shortable status of TSLA')
            self.assertEqual(cm.output, self.expected_log)

    def tearDown(self):
        del self.shortable
        del self.expected_log

#class TestNoExistingShortListDatabase(unittest.TestCase):
#class TestInvalidAsset(unittest.TestCase):
#class TestInvalidAssetStatus(unittest.TestCase):
#class TestSingleAssetinDatabase(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
