# -*- coding: utf-8 -*-
from typing import Optional
from sqlmodel import SQLModel, Field


class Prices(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	time_stamp:  int
	metal_symbol: str
	metal_name: str
	price: float
	currency: str
