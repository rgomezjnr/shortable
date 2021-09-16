# shortable
Keep track of asset shortable status, and receive a notification when shortable status changes, e.g. from HTB to ETB

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [winotify](https://github.com/versa-syahptr/winotify)
- [alpaca-trade-api](https://github.com/alpacahq/alpaca-trade-api-python)

## Installation
    git clone https://github.com/rgomezjnr/shortable

    pip install alpaca-trade-api

Set alpaca API key environment variables
    
Schedule shortable to routinely run using Windows Task Scheduler.

## Usage

## Files
- shortable.json

Dictionary database for recording asset shortable status. Use JSON format such as follows:

`{"AMZN": true, "MSFT": true, "TSLA": true}`

## Support
If you find an issue or have any feedback please submit an issue on [GitHub](https://github.com/rgomezjnr/shortable/issues).

If you would like to show your support donations are greatly appeciated via:
- [GitHub Sponsors](https://github.com/sponsors/rgomezjnr)
- [PayPal](https://paypal.me/rgomezjnr)
- [Bitcoin:](bitcoin:bc1qh46qmztl77d9dl8f6ezswvqdqxcaurrqegca2p) bc1qh46qmztl77d9dl8f6ezswvqdqxcaurrqegca2p
- [Ethereum:](ethereum:0xAB443e578c9eA629088e26A9009e44Ed40f68678) 0xAB443e578c9eA629088e26A9009e44Ed40f68678

## Authors
[Robert Gomez, Jr.](https://github.com/rgomezjnr)

## Source code
https://github.com/rgomezjnr/shortable

## License
[MIT](https://github.com/rgomezjnr/shortable/blob/master/LICENSE.txt)
