from peewee import *
from playhouse.shortcuts import model_to_dict
import requests
import json


psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='marvelDB_A', password='marvel123')

#psql_db = PostgresqlDatabase('db', user='postgres', host='marvel6_db', password='user123',autocommit=True, autorollback=True )


class BaseModel(Model):
    class Meta:
       database = psql_db


class heroes(BaseModel):
    id = PrimaryKeyField(null=False)  
    name = CharField()
    image = CharField()


class powerstats(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    combat = IntegerField()
    durability = IntegerField()
    intelligence = IntegerField()
    power = IntegerField()
    speed = IntegerField()
    strength = IntegerField()

class works(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    base = CharField()
    ocupation = CharField()

class connections(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    group-afiliation = CharField()
    ocupation = CharField()

class biography(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    aliases = CharField()
    alignement = CharField()
    alter-egos = CharField()
    first-apparance = CharField()
    full-name = CharField()
    place-of-birthday = CharField()
    publisher = CharField()

class appearance(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    eye-color = CharField()
    gender = CharField()
    hair-color = CharField()
    height = CharField()
    race = CharField()
    weight = CharField()


heroes.create_table()
#powerstats.create_table()

#create heroes
her= heroes.create(name="thor",image="https://www.image.com")
power= powerstats.create(id=her,combat=100, durability=100,  intelligence=100, power=100, speed=100, strength=100 )



#ENDPOINT = 'https://pokeapi.co/api/v2/pokemon/3'
#
#r = requests.get(ENDPOINT)
#data = r.json()
#
#types = ','.join(list(filter(lambda x: x != '', [_type.get('type', {}).get('name', '') for _type in data.get('types', [])])))
#ret = {'id':3,'nombre':data.get('name'),'tipos':json.dumps(types),'imagen':data.get('sprites', {}).get('front_default'),}
#print(ret)
#
#pokemon, created = marvelheroes1.get_or_create(**ret)
#print(f"Pokemon {'Created' if created else 'Existing'}: {pokemon.nombre}")

