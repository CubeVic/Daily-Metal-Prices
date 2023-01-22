# -*- coding: utf-8 -*-
import os
from typing import Tuple
from dotenv import load_dotenv
import requests
import random

load_dotenv()
BASE_URL = "https://www.goldapi.io/api/"

endpoint = {
	"gold":"XAU/USD",
	"silver":"XAG/USD",
	"platinum":"XPT/USD",
	"palladium":"XPD/USD",
	"stat":"stat"}

headers = {
		"x-access-token": os.environ.get(f"API_KEY{random.randint(1,2)}"),
		"Content-Type": "application/json"}


def fetch(data: str = 'stat') -> Tuple[int, dict]:
	url = f"{BASE_URL}{endpoint[data]}"
	resp = requests.get(url=url, headers=headers)
	resp.raise_for_status()
	return resp.json()

if __name__ == "__main__":
	print(fetch(data="silver"))
