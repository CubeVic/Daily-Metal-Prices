# -*- coding: utf-8 -*-
import json
import os
from typing import Tuple
import requests

BASE_URL = "https://www.goldapi.io/api/"

endpoint = {
	"gold":"XAU/USD",
	"silver":"XAG/USD",
	"platinum":"XPT/USD",
	"palladium":"XPD/USD",
	"stat":"stat"}

headers = {
		"x-access-token": os.environ["API_KEY"],
		"Content-Type": "application/json"}


def fetch(data: str = 'stat') -> Tuple[int, dict]:
	url = f"{BASE_URL}{endpoint[data]}"
	resp = requests.get(url=url, headers=headers)
	resp.raise_for_status()
	return resp.json()
