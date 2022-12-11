# -*- coding: utf-8 -*-
from typing import Optional
from sqlmodel import SQLModel, Field


class Prices(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	timestamp: int
	metal: str
	currency: str
	exchange: str
	symbol: str
	prev_close_price: float
	open_price: float
	low_price: float
	high_price: float
	open_time: int
	price: float
	ch: float
	chp: float
	ask: float
	bid: float
	price_gram_24k: float
	price_gram_22k: float
	price_gram_21k: float
	price_gram_20k: float
	price_gram_18k: float
