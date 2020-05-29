from peewee import *
from playhouse.shortcuts import model_to_dict

psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='marvelDB_A', password='marvel123')
# psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='localhost', password='marvel123')

class BaseModel(Model):
    class Meta:
       database = psql_db

class heroes(BaseModel):
    id = PrimaryKeyField(null=False)  
    name = CharField()
    image = CharField()


class powerstats(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    combat = CharField(null=True)
    durability = CharField(null=True)
    intelligence = CharField(null=True)
    power = CharField(null=True)
    speed = CharField(null=True)
    strength = CharField(null=True)

class work(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    base = CharField(null=True)
    occupation = CharField(null=True)

class connections(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    groupAffiliation = CharField(null=True)
    relatives = CharField(null=True)

class biography(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    aliases = CharField(null=True)
    alignment = CharField(null=True)
    alterEgos = CharField(null=True)
    firstAppearance = CharField(null=True)
    fullName = CharField(null=True)
    placeOfBirth = CharField(null=True)
    publisher = CharField(null=True)

class appearance(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    eyeColor = CharField(null=True)
    gender = CharField(null=True)
    hairColor = CharField(null=True)
    height = CharField(null=True)
    race = CharField(null=True)
    weight = CharField(null=True)

