from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas

engine = create_engine('postgresql://localhost/pokemon')
Base = declarative_base()

class Nature(Base):
    __tablename__ = 'natures'

    id = Column(Integer, primary_key=True)
    nature = Column(String(255))
    attack = Column(String(10))
    defense = Column(String(10))
    spattack = Column(String(10))
    spdefense = Column(String(10))
    speed = Column(String(10))


session = Session(engine)


natures = session.query(Nature).delete()
session.commit()

natures_df = pandas.read_csv('data/natures.csv')

for index, row in natures_df.iterrows():
    nature = Nature()
    nature.nature = row['nature']
    nature.attack = row['attack']
    nature.defense = row['defense']
    nature.spattack = row['spattack']
    nature.spdefense = row['spdefense']
    nature.speed = row['speed']
    session.add(nature)

session.commit()



natures = session.query(Nature).all()

for nature in natures:
    print 'Nature: ', nature.nature
    print 'attack: ', nature.attack
    print 'defense: ', nature.defense
    print 'spattack: ', nature.spattack
    print 'spdefense: ', nature.spdefense
    print 'speed: ', nature.speed
    print ''
