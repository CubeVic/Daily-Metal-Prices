# -*- coding: utf-8 -*-
from decimal import Decimal
from pydantic import BaseModel


class StatusResponse(BaseModel):
    result: bool


class MetalResponse(BaseModel):
    timestamp: int
    metal: str
    currency: str
    exchange: str
    symbol: str
    prev_close_price: Decimal
    open_price: Decimal
    low_price: Decimal
    high_price: Decimal
    open_time: int
    price: Decimal
    ch: Decimal
    chp: Decimal
    ask: Decimal
    bid: Decimal
    price_gram_24k: Decimal
    price_gram_22k: Decimal
    price_gram_21k: Decimal
    price_gram_20k: Decimal
    price_gram_18k: Decimal


class StatResponse(BaseModel):
    requests_today: int
    requests_yesterday: int
    requests_month: int
    requests_last_month: int
