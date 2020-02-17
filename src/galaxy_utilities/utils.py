import os
from peewee import *
from playhouse.shortcuts import model_to_dict

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

# ENVIRONMENT VARIABLE
DB_NAME = os.getenv('DB_NAME')

db = SqliteDatabase(DB_NAME)

class Messier(Model):
    messier = CharField()
    ngc = CharField()
    decouvreur = CharField()
    annee = IntegerField()
    constellation = CharField()
    objet = CharField()
    ascension = CharField()
    declinaison = CharField()
    mag = FloatField()
    dimension = CharField()
    distance = FloatField()
    saison = CharField()
    visible = CharField()

    class Meta:
        database = db

def return_all_messiers():
    db.connect()

    messiers = []
    for m in Messier.select():
        messiers.append(model_to_dict(m))

    db.close()

    return  messiers

def return_visible_messiers(visibility):
    db.connect()

    messiers = []
    for m in Messier.select().where(Messier.visible == visibility):
        messiers.append(model_to_dict(m))

    db.close()

    return  messiers

def return_season_messiers(season):
    db.connect()

    messiers = []
    for m in Messier.select().where(Messier.saison == season):
        messiers.append(model_to_dict(m))

    db.close()

    return  messiers

def return_distance_messiers(distancemin, distancemax):
    db.connect()

    messiers = []
    for m in Messier.select().where(Messier.distance >= distancemin and Messier.distance <= distancemax):
        messiers.append(model_to_dict(m))

    db.close()

    return  messiers


# Upload with ACL set to "public-read"
def upload_to_db(content, name):
    # get conn
    try:
        filename = str('images/'+name)
    except Exception as e:
        print('str filename error: {}'.format(e))
        return 0
    
    try:
        print("Uploading du fichier: {}".format(filename))
        
        return 1
    except Exception as e:
        print("Error: {}".format(e))
        return 0
