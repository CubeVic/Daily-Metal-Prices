import json
import os
from typing import Tuple
import requests


GOLD = "https://www.goldapi.io/api/XAU/USD"
SILVER = "https://www.goldapi.io/api/XAG/USD"
PLATINUM = "https://www.goldapi.io/api/XPT/USD"
PALLADIUM = "https://www.goldapi.io/api/XPD/USD"

STATS = "https://www.goldapi.io/api/stat"

headers = {
		"x-access-token": os.environ["API_KEY"],
		"Content-Type": "application/json"}
# def _prepare_request() -> Session:
# 	headers = {
# 		"x-access-token": os.environ["API_KEY"],
# 		"Content-Type": "application/json"}
# 	session = Session()
# 	session.headers = headers
# 	return session


def _prepare_answer(data: dict) -> dict:
	metal_name = {
		"XAU": "Gold",
		"XAG": "Silver",
		"XPT": "Platinum",
		"XPD": "Palladium"
	}
	return {'metal_data': {
				'time_stamp': data['timestamp'],
				'metal_symbol': data['metal'],
				'metal_name': metal_name[data['metal']],
				'price': data['price'],
				'currency': data['currency'],
			}
	}


def fetch_data(metal: str = 'silver') -> Tuple[int, dict]:
	metals = {
		'gold': GOLD,
		'silver': SILVER,
		'platinum': PLATINUM,
		'palladium': PALLADIUM}
	url = metals[metal.lower()]
	resp = requests.get(url=url, headers=headers)
	# resp = s.get(url=url)
	# print(resp)
	return resp.status_code, resp.json()
	# # return resp.status_code, {'metal_data': {
	# 			'time_stamp': data['timestamp'],
	# 			'metal_symbol': data['metal'],
	# 			'metal_name': metal_name[data['metal']],
	# 			'price': data['price'],
	# 			'currency': data['currency'],
	# 		}
	# }


def fetch_stats() -> Tuple[int, dict]:
	url = STATS
	resp = requests.get(url=url, headers=headers)
	return resp.status_code, resp.json()


