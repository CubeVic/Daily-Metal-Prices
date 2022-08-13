""" initialize the database"""
from metals.metal_prices import fetch_data, fetch_stats
from metals.models import Prices
from metals import metals

if __name__ == "__main__":

	record = metals.select_record(
		table=Prices,
		where_clause=Prices.metal_name == 'Silver')
	records = metals.select_records(
		table=Prices,
		where_clause=Prices.metal_name == 'Silver')

	print(f"record : {record}")
	print(f"records : {records}")
	print(fetch_stats())
