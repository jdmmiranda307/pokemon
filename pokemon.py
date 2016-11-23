#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas

engine = create_engine('postgresql://localhost/pokemon')
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    item = Column(String(255))
    description = Column(String(4000))


session = Session(engine)


items = session.query(Item).delete()
session.commit()

items_df = pandas.read_csv('data/items.csv')

for index, row in items_df.iterrows():
    item = Item()
    item.id = row['id']
    item.item = row['item']
    item.description = row['description']
    session.add(item)

session.commit()



items = session.query(Item).all()

for item in items:
    print 'item: ', item.item
    print 'descricao: ', item.description
    print ''








    