# shortable
Receive an alert if an asset becomes shortable, e.g. from HTB to ETB, or vice versa

## Summary
shortable is a Python script for tracking the short selling availability of assets. The script works by maintaining a
database of assets and their shorting availability (either true, shortable, easy-to-borrow (ETB) or false, non-shortable,
hard-to-borrow (HTB)). When the script notices the asset shortable condition has changed since the last run, it notifies
the user with a Windows 10 toast notification. This may be helpful in quickly acting on ETB or HTB changes of assets or
gauging market sentiment. The script currently only supports the Alpaca Securities broker but could be expanded to other
brokers that have API access.

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [winotify](https://github.com/versa-syahptr/winotify)
- [alpaca-trade-api](https://github.com/alpacahq/alpaca-trade-api-python)

## Setup
1. Install shortable using pip:
```
    pip install shortable
```
2. Create API keys using the [Alpaca dashboard](https://app.alpaca.markets/login). Refer to Alpaca's [API v2](https://alpaca.markets/docs/api-documentation/api-v2/) and [API Documentation](https://alpaca.markets/docs/api-documentation/) for more details.
3. Set environment variables APCA_API_KEY_ID and APCA_API_SECRET_KEY for the Windows user account.
shortable can be used with Alpaca paper accounts by setting APCA_API_BASE_URL=https://paper-api.alpaca.markets. Refer to
[Alpaca Environment Variables](https://github.com/alpacahq/alpaca-trade-api-python#alpaca-environment-variables).

## Usage
1. Define assets to track in [shortable.json](#shortablejson).
2. Run the script. When there are no asset shortable changes there is no output or notification. Check [shortable.log](#shortablelog) to verify operation.
3. Optionally schedule shortable to routinely run using Windows Task Scheduler.

## Files
### shortable.json
Dictionary database for recording asset shortable status. Use JSON format such as follows:
```
{"AMZN": true, "MSFT": true, "TSLA": true}
```

### shortable.log
Log file indicating checks for shortable status, changes to shortable status, and when toast notifications are fired.

## Support
If you find an issue or have any feedback please submit an issue on [GitHub](https://github.com/rgomezjnr/shortable/issues).

If you would like to show your support donations are greatly appeciated via:
- [GitHub Sponsors](https://github.com/sponsors/rgomezjnr)
- [PayPal](https://paypal.me/rgomezjnr)
- [Bitcoin:](bitcoin:bc1qh46qmztl77d9dl8f6ezswvqdqxcaurrqegca2p) bc1qh46qmztl77d9dl8f6ezswvqdqxcaurrqegca2p
- [Ethereum:](ethereum:0xAB443e578c9eA629088e26A9009e44Ed40f68678) 0xAB443e578c9eA629088e26A9009e44Ed40f68678

## Author
[Robert Gomez, Jr.](https://github.com/rgomezjnr)

## Source code
https://github.com/rgomezjnr/shortable

## License
[MIT](https://github.com/rgomezjnr/shortable/blob/master/LICENSE.txt)
