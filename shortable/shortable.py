#!/usr/bin/env python 

import json
import logging
import argparse
import textwrap

import alpaca_trade_api as alpaca
from winotify import Notification

#API = alpaca
#BROKER = alpaca

class Shortable():
    def __init__(self):

        self.old_short_status = dict()
        self.new_short_status = dict()
        self.report = ""
        self.api = alpaca.REST()

    def __del__(self):
        del self.old_short_status
        del self.new_short_status
        del self.report
        del self.api

    def read_old_short_status(self):
        with open('shortable.json', 'r') as shortable:
            self.old_short_status = json.load(shortable)

    def get_new_short_status(self):
    #def get_new_short_status(self, broker_api):
        #if self.api == 'ALPACA':
        #if self.api == alpaca.REST():
        #    for asset in self.old_short_status:
        #        asset_update = self.api.get_asset(asset)
        #        self.new_short_status[asset] = asset_update.shortable

        for asset in self.old_short_status:
            asset_update = self.api.get_asset(asset)
            self.new_short_status[asset] = asset_update.shortable

    def check_short_status_changes(self):
        for (old_short, old_short_stat), (new_short, new_short_stat) in zip(self.old_short_status.items(), self.new_short_status.items()):

                # DEBUG
                #print(asset)
                #print("Tradable: {}".format(asset_update.tradable))
                #print("Shortable: {}".format(asset_update.shortable))
                #print("Easy-to-Borrow: {}".format(asset_update.easy_to_borrow))

                if old_short_stat is False and new_short_stat is True:
                    logging.info('%s now shortable', old_short)
                    self.report += '{} now shortable\n'.format(old_short)
                elif old_short_stat is True and new_short_stat is False:
                    logging.info('%s now non-shortable', old_short)
                    self.report += '{} now non-shortable\n'.format(old_short)
                elif old_short_stat is None and new_short_stat is True:
                    logging.info('%s now shortable, previous status unknown', old_short)
                    self.report += '{} now shortable, previous status unknown\n'.format(old_short)
                elif old_short_stat is None and new_short_stat is False:
                    logging.info('%s now non-shortable, previous status unknown', old_short)
                    self.report += '{} now non-shortable, previous status unknown\n'.format(old_short)
                else:
                    # no change to asset shortable status
                    logging.info('No change to shortable status of %s', old_short)

        # Update old shortable status to new shortable status
        self.old_short_status = self.new_short_status

    # Write new updated short list to file, clearing old list
    def write_new_short_status(self):
        with open('shortable.json', 'w') as shortable:
            shortable.seek(0)
            shortable.truncate()
            json.dump(self.new_short_status, shortable)

    # Create Windows 10 notification if new shortble status to report
    def send_notification(self):
        if self.report:
            logging.info('%s', self.report)

            toast = Notification(app_id='📉 shortable', title='📉 shortable', msg=self.report)
            toast.build().show()
            logging.info('toast notification fired')

# Entry point for running launch script after installing package, see setup.py
def run():
    parser = argparse.ArgumentParser(
        prog='shortable',
        description='Receive an alert if an asset becomes shortable, e.g. from HTB to ETB, or vice versa',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
            Setup
            1. Define assets to track in shortable.json e.g. {"AMZN": true, "MSFT": true, "TSLA": false}.
            2. Run shortable from the same directory as shortable.json. When there are no asset shortable changes there is no output or notification. Check shortable.log to verify operation.
            3. Optionally schedule shortable to run routinely using Windows Task Scheduler.
            ''')
    )
    #parser.add_argument('ASSET', type=str.upper, help='Ticker of asset to check')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    args = parser.parse_args()

    #logging.basicConfig(filename='shortable.log', encoding='utf-8', level=logging.INFO)
    logging.basicConfig(filename='shortable.log', level=logging.INFO, format='%(asctime)s %(message)s')

    shortable = Shortable()
    shortable.read_old_short_status()
    shortable.get_new_short_status()
    shortable.check_short_status_changes()
    shortable.write_new_short_status()
    shortable.send_notification()

if __name__ == '__main__':
    run()
