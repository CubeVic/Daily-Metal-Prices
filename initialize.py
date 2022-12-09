# -*- coding: utf-8 -*-
""" initialize the database"""
from metals import metals
from metals.metal_prices import fetch_data
from metals.metals import insert_all
from metals.models import Prices


def initialize_records():
	items = ["Silver", "Gold", "Platinum", "Palladium"]
	metals_info = []

	for item in items:
		_, resp_silver = fetch_data(metal=item)
		metal = Prices(**resp_silver['metal_data'])
		metals_info.append(metal)

	insert_all(items=metals_info)


if __name__ == "__main__":
	metals.create_db_and_tables()
	metals.initialize_records()
