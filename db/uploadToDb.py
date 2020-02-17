from peewee import *
import pandas as pd
import random
import unidecode

DB_NAME = 'database.db'

df = pd.read_csv('messier_wiki.csv')

"""
Cleaning and preparing input dataset
"""
df['Annee'] = df['Annee'].astype('int')

df['Mag'] = df['Mag'].str.replace(pat='\"', repl='')
df['Mag'] = df['Mag'].str.replace(pat=',', repl='.')
df['Mag'] = df['Mag'].astype('float')

df['Distance'] = df['Distance'].str.replace(pat='\"', repl='')
df['Distance'] = df['Distance'].str.replace(pat=' ', repl='')
df['Distance'] = df['Distance'].str.replace(pat=',', repl='.')
df['Distance'] = df['Distance'].str.replace(pat='a.l.', repl='')
df['Distance'] = df['Distance'].str.replace(pat='?', repl='0.0')
df['Distance'] = df['Distance'].astype('float')

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

print("Connecting to db")
db.connect()
print("... OK")

print("Creating table")
db.create_tables([Messier])
print("... OK")

print("Saving to db")
for index, row in df.iterrows():
    messier = Messier.create(
        messier = row["Messier"],
        ngc = row["NGC"],
        decouvreur = row["Decouvreur"],
        annee = int(row["Annee"]),
        constellation = row["Constellation"],
        objet = row["Objet"],
        ascension = row["Ascension"],
        declinaison = row["Declinaison"],
        mag = float(row["Mag"]),
        dimension = row["Dimension"],
        distance = float(row["Distance"]),
        saison = unidecode.unidecode((row["Saison"]).lower()),
        visible = "oeil" if random.randint(0, 1) == 1 else "telescope"
    )

    try:
        messier.save()
    except:
        print("error")

print("... OK")

print("Closing db")
db.close()
print('... OK')
