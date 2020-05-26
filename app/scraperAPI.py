import requests
import json



TOKEN='2950883621624529'
ENDPOINT = 'https://www.superheroapi.com/api.php/'+TOKEN+'/'
ID =0
POWERSTATS ='/powerstats'
BIOGRAPHY ='/biography'
APPARENCE ='/apparence'
WORK ='/work'
CONNECTIONS ='/connections'
IMAGE ='/image'
NAME=''
SEARCHNAME ='search/'




def getHero(x):
    r = requests.get(ENDPOINT+str(x))
    data = r.json()   
    id=data.get('id')
    name=data.get('name')
    image=data.get('image').get('url')
    powerstats=getPowerstats(data.get('powerstats'))
    appearance=getAppearance(data.get('appearance'))
    biography=getBiography(data.get('biography'))
    work=getWork(data.get('work'))
    connections=getConnections(data.get('connections'))        
    return {'id':id, 'name':name , 'image': image,'powerstats':powerstats,'appearance':appearance, 'biography':biography,'work':work, 'connections':connections, }

def getPowerstats(powerstats):
    combat=powerstats.get('combat')
    durability=powerstats.get('durability')
    intelligence=powerstats.get('intelligence')
    power=powerstats.get('power')
    speed=powerstats.get('speed')
    strength=powerstats.get('strength')
    return {'combat':combat , 'durability': durability, 'intelligence':intelligence,'power':power, 'speed':speed, 'strength':strength}


def getAppearance(apparance):
    eyeColor=apparance.get('eye-color') 
    gender=apparance.get('gender')
    hairColor=apparance.get('hair-color')
    height=str(apparance.get('height'))
    race=apparance.get('race')
    weight=str(apparance.get('weight'))
    return {'eye-color':eyeColor , 'gender': gender, 'hair-color':hairColor, 'height':height, 'race':race, 'weight':weight}

def getBiography(biography):
    aliases=str(biography.get('aliases'))
    alignement=biography.get('gealignementnder')
    alterEgos=biography.get('alter-egos')
    firstApparance=biography.get('first-apparance')
    fullName=biography.get('full-name')
    placeOfBirthday=biography.get('place-of-birthday')
    return {'aliases':aliases , 'alignement': alignement, 'alter-egos':alterEgos, 'first-apparance':firstApparance, 'full-name':fullName, 'place-of-birthday':placeOfBirthday}

def getWork(work):
    base=work.get('base')
    ocupation=work.get('ocupation')
    return {'base':base , 'durabocupationility': ocupation}

def getConnections(connections):
    groupAfiliation=connections.get('group-afiliation')
    relatives=connections.get('relatives')
    return {'group-afiliation':groupAfiliation , 'relatives': relatives}


#types = ','.join(list(filter(lambda x: x != '', [_type.get('typA, {}).get('name', '') for _type in data.get('types', [])])))
#ret = {'id':3,'nombre':data.get('name'),'tipos':json.dumps(types),'imagen':data.get('sprites', {}).get('front_default'),}
#print(ret)

#pokemon, created = marvelheroes1.get_or_create(**ret)
a=(getHero(2))
print(' >>> '+str(a['biography']['aliases'])+' <<<')
