""" initialize the database"""
from metals.metal_prices import fetch_data, fetch_stats
from metals.models import Prices
from metals import metals

if __name__ == "__main__":
	items = ["Silver", "Gold", "Platinum", "Palladium"]

	metals.create_db_and_tables()

	metals_info = []

	for item in items:
		_, resp_silver = fetch_data(metal=item)
		metal = Prices(**resp_silver['metal_data'])
		metals_info.append(metal)

	metals.insert_all(items=metals_info)

	record = metals.select_record(
		table=Prices,
		where_clause=Prices.metal_name == 'Silver')
	records = metals.select_records(
		table=Prices,
		where_clause=Prices.metal_name == 'Silver')

	print(f"record : {record}")
	print(f"records : {records}")
	print(fetch_stats())
