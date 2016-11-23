#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas

engine = create_engine('postgresql://localhost/pokemon')
Base = declarative_base()

class Ability(Base):
    __tablename__ = 'abilities'

    id = Column(Integer, primary_key=True)
    ability = Column(String(255))
    description = Column(String(4000))


session = Session(engine)


abilities = session.query(Ability).delete()
session.commit()

abilities_df = pandas.read_csv('data/abilities.csv')

for index, row in abilities_df.iterrows():
    ability = Ability()
    ability.ability = row['ability']
    ability.description = row['description']
    session.add(ability)

session.commit()



abilities = session.query(Ability).all()

for ability in abilities:
    print 'Ability: ', ability.ability
    print 'descricao: ', ability.description
    print ''
