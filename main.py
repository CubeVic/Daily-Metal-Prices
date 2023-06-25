# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from api_call import DailyPrice


if __name__ == "__main__":
    load_dotenv()
    key = os.environ.get("API_KEY")
    api_call = DailyPrice(access_token=key)
    print(api_call.get_status())
    print(api_call.get_stats())
    print(api_call.get_metal_price(metal='silver'))
    print(api_call.get_stats())
