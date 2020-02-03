import os
from peewee import *

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

# ENVIRONMENT VARIABLE
DB_NAME = os.getenv('DB_NAME')
GALAXY_TABLE = os.getenv('GALAXY_TABLE')

db = SqliteDatabase(DB_NAME)

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
        bucket.put_object(Bucket=BUCKET_NAME, Key=filename, Body=content)
        
        return 1
    except Exception as e:
        print("Error: {}".format(e))
        return 0
