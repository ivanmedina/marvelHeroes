from peewee import *
from playhouse.shortcuts import model_to_dict

#psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='marvelDB', password='marvel123')
psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='marvelDB_A', password='marvel123')

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
    relatives = CharField()

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

