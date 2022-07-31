import json
import os
from typing import Tuple

from requests import Session

GOLD = "https://www.goldapi.io/api/XAU/USD"
SILVER = "https://www.goldapi.io/api/XAG/USD"
PLATINUM = "https://www.goldapi.io/api/XPT/USD"
PALLADIUM = "https://www.goldapi.io/api/XPD/USD"

STATS = "https://www.goldapi.io/api/stat"


def _prepare_request() -> Session:
	headers = {
		"x-access-token": os.environ["API_KEY"],
		"Content-Type": "application/json"}
	session = Session()
	session.headers = headers
	return session


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
	s = _prepare_request()
	resp = s.get(url=url)
	return resp.status_code, _prepare_answer(json.loads(resp.text))


def fetch_stats() -> Tuple[int, dict]:
	s = _prepare_request()
	url = STATS
	resp = s.get(url=url)
	return resp.status_code, json.loads(resp.text)


