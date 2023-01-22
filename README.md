# Daily Metal Prices

![Logo_metal_prices](Metal_prices.png)

## Description

In the future will be a microservice that will provide the daily prices of different precious metals in USD, for now it provide prices from a single API (https://www.goldapi.io/) in the future is expected to have its own logic and fetch the prices form other sources.

## How to Use the Project

* `fetch`: it will receive "Silver", "Gold", "Platinum", "Palladium" or "stats" as a parameter, and it will return a dictionary with the price and metal information.

```json

{
    'timestamp': 1670742767,
    'metal': 'XAG',
    'currency': 'USD',
    'exchange': 'FOREXCOM',
    'symbol': 'FOREXCOM:XAGUSD',
    'prev_close_price': 23.069,
    'open_price': 23.069,
    'low_price': 22.956,
    'high_price': 23.684,
    'open_time': 1670544000,
    'price': 23.684,
    'ch': 0.615,
    'chp': 2.67,
    'ask': 23.499,
    'bid': 23.434,
    'price_gram_24k': 0.7615,
    'price_gram_22k': 0.698,
    'price_gram_21k': 0.6663,
    'price_gram_20k': 0.6345,
    'price_gram_18k': 0.5711
}

```

* `fetch`: with the argumnet `stats` will return a json containin information about the API usage.

```json
{
    'requests_today': 40,
    'requests_yesterday': 0,
    'requests_month': 40,
    'requests_last_month': 0
}
```

## License
[MIT license](LICENSE)
