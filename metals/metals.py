# -*- coding: utf-8 -*-
""" API for the database """

import sqlalchemy
from sqlmodel import SQLModel, create_engine, Session, select
from sqlmodel.sql.expression import SelectOfScalar, Select

db_engine = sqlalchemy.future.engine.Engine


def define_db(database_name: str) -> str:
	"""Define the database"""
	return f"sqlite:///{database_name}.db"


def define_engine(sql_url, echo=False):
	"""Define the engine"""
	# these two lines is to solve the warning
	SelectOfScalar.inherit_cache = True  # type: ignore
	Select.inherit_cache = True  # type: ignore
	return create_engine(sql_url, echo=echo)


def configuration() -> db_engine:
	"""Create the database"""
	sql_url = define_db(database_name="metal_prices")
	return define_engine(sql_url=sql_url, echo=False)


def create_db_and_tables():
	"""Create database and all tables"""
	database_engine = configuration()
	SQLModel.metadata.create_all(database_engine)


def insert(item):
	"""Insert one record"""
	database_engine = configuration()
	with Session(database_engine) as session:
		session.add(item)
		session.commit()


def insert_all(items: list):
	for item in items:
		insert(item=item)


def select_record(table, where_clause):
	"""Select the first Record"""
	database_engine = configuration()
	with Session(database_engine) as session:
		statement = select(table).where(where_clause)
		return session.exec(statement=statement).first()


def select_records(table, where_clause):
	"""Select several records"""
	database_engine = configuration()
	with Session(database_engine) as session:
		statement = select(table).where(where_clause)
		return session.exec(statement=statement).all()
