import requests
import os
from dotenv import load_dotenv
from models import MetalResponse, StatResponse, StatusResponse

load_dotenv()

class DailyPrice:
    BASE_URL = "https://www.goldapi.io/api/"

    endpoint = {
        "gold": "XAU/USD",
        "silver": "XAG/USD",
        "platinum": "XPT/USD",
        "palladium": "XPD/USD",
        "stat": "stat",
        "status": "status"}

    def __init__(self, access_token):
        self.base_url = self.BASE_URL
        self.access_token = access_token
        self.headers = {
            "x-access-token": f"{self.access_token}",
            "Content-Type": "application/json"
        }

    def get_status(self):
        url = os.path.join(self.base_url, self.endpoint["status"])
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        if response.ok:
            return StatusResponse(**response.json())

    def get_stats(self):
        url = os.path.join(self.base_url, self.endpoint["stat"])
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        if response.ok:
            return StatResponse(**response.json())

    def get_metal_price(self, metal: str):
        url = os.path.join(self.base_url, self.endpoint[metal])
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        if response.ok:
            return MetalResponse(**response.json())
