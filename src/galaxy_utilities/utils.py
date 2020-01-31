import os

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

# ENVIRONMENT VARIABLE
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')

def allowed_file(filename):
    try:
        name, ext = filename.rsplit('.', 1)
    except ValueError:
        return False
    return ext.lower() in ALLOWED_EXTENSIONS


# Upload file

def get_session():
    """Return a boto3 Session object, with the appropriate credentials."""
    session = ACCESS_KEY_ID + SECRET_ACCESS_KEY
    return session



def get_bucket(session=None):
    """Return a Bucket object, corresponding to your own bucket."""
    bucket = BUCKET_NAME
    return bucket

# Upload with ACL set to "public-read"
def upload_to_db(content, name):
    # get session
    session = get_session()

    # get bucket
    bucket = get_bucket(session)

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
