import os
from peewee import *
from marshmallow_peewee import ModelSchema
import json

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

class MessierSchema(ModelSchema):

    class Meta:
        model = Messier

def return_json_blob():
    # db.connect()

    messier = []
    for m in Messier.select():
        a = json.dump()
        # a = json.dumps(m)
        # try:
        result, errors = MessierSchema().dump(obj=m)
        print(errors)
        # except ValueError:
        #     pass

    # db.close()

    print(messier)
    
    return "result"

def allowed_file(filename):
    try:
        name, ext = filename.rsplit('.', 1)
    except ValueError:
        return False
    return ext.lower() in ALLOWED_EXTENSIONS


# Upload file

def get_sqlite_conn():
    """Return a sqlite3 connection (DB_NAME in environnement variables)."""
    conn = sqlite3.connect(DB_NAME)
    return conn

# Upload with ACL set to "public-read"
def upload_to_db(content, name):
    # get conn
    conn = get_sqlite_conn()

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
