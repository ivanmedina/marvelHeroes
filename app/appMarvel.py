from flask import Flask, render_template
from peewee import *
from playhouse.shortcuts import model_to_dict
from modelsMarvel import *

app = Flask(__name__, static_url_path='/static')



@app.route('/')
def index():
    heros=heroes.select(heroes.id, heroes.name)

    return render_template('index.html',heroes =heros)

@app.route('/hero/<string:idHero>')
def heroById(idHero):
    if(idHero.isdigit()):
        if(0<int(idHero)<735):
            hero=heroes.select().where(heroes.id==idHero)
            if( len(hero) >0):
                        
                pwrsts=powerstats.select().where(powerstats.id==idHero).dicts()
                biog=biography.select().where(biography.id==idHero).dicts()
                appr=appearance.select().where(appearance.id==idHero).dicts()      
                conn=connections.select().where(connections.id==idHero).dicts()       
                wrk=work.select().where(work.id==idHero).dicts()
                hero={'hero':hero[0], 'powerstats':pwrsts[0], 'biography':biog[0], 'appearance':appr[0], 'connections':conn[0], 'work':wrk[0]}
                # pwr=powerstats.alias()
                # bio=biography.alias()
                # her=heroes.alias()
                # hero=(heroes
                #     .select( heroes, powerstats, biography, appearance, connections, work)
                #     .join(powerstats)
                #     .switch(heroes)
                #     .join(biography)
                #     .switch(heroes)
                #     .join(appearance)
                #     .switch(heroes)
                #     .join(connections)
                #     .switch(heroes)
                #     .join(work)
                #     .where(heroes.id==idHero))
                # hero=hero.dicts()[0]
            
                return render_template('hero.html',hero =hero)

    return render_template('heroNotFound.html',  id_Hero=idHero)




if __name__ == "__main__":
    app.run(host="0.0.0.0")
    psql_db.close()
