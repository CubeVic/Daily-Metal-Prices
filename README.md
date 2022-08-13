![Logo_metal_prices](Metal_prices.png)
# Daily Metal Prices
## Description
in the future will be a microservice that will provide the daily prices of different precious metals in USD, for now it provide prices from a single API (https://www.goldapi.io/) in the future is expected to have its own logic and fetch the prices form other sources. 

## Table of Contents

## How to Install and Run the Project
To use it: 
1.  Clone it.
2. Run the `Initialize.py` this will create the database `metal_prices.db` and populate it with the prices of the day, the metals supported at this point are: 

* Silver (**XAG**).
* Gold (**XAU**).
* Platinum (**XPT**).
* Palladium (**XPD**).

> you will need to add an API key on `os.environ["API_KEY"]`, this is located on `metal>metal_prices>_prepare_request() > "x-access-token": os.environ["API_KEY"]`

## How to Use the Project

At this stage there are two main functions:
* `fetch_data()`: it will receive "Silver", "Gold", "Platinum", "Palladium" as a parameter, and it will return a tuple, first argument is the status code, second a dictionary with the price and metal information.
````commandline
(200, {'metal_data': {'time_stamp': 1660381675, 'metal_symbol': 'XAG', 'metal_name': 'Silver', 'price': 20.829, 'currency': 'USD'}})
````
* `fetch_stats()`: it will return the usage stats for the current API as a tuple, first parameter the status code, second a dictionary with the stat information.

```commandline
(200, {'requests_today': 40, 'requests_yesterday': 0, 'requests_month': 40, 'requests_last_month': 0})
```

## License  
[MIT license](LICENSE)