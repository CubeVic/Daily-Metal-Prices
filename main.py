# -*- coding: utf-8 -*-
""" initialize the database"""
from metals.metal_prices import fetch
from metals.models import Prices
from metals import metals
from dotenv import load_dotenv
import initialize

load_dotenv()

if __name__ == "__main__":
	metals.create_db_and_tables()
	initialize.initialize_records()
	record = metals.select_record(
		table=Prices,
		where_clause=Prices.metal == 'XAG')
	records = metals.select_records(
		table=Prices,
		where_clause=Prices.metal == 'XAG')
	print(f"record : {record}")
	print(f"records : {records}")
	print(fetch())
	print(fetch(data='silver'))
