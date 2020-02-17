from flask import Flask, flash, request, redirect, url_for, json, abort
from galaxy_utilities.utils import return_all_messiers, return_visible_messiers, return_season_messiers, return_distance_messiers

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Core function of the app.
    
    Display a simple form to upload a document.
    For the most part, this is taken the official Flask documentation
    http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
    """
    # if request.method == 'POST':
    #     # check if the post request has the file part
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     # if user does not select file, browser also
    #     # submit an empty part without filename
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         content = file.read()
    #         name = secure_filename(file.filename)

    #         if upload_to_db(content, name):
    #             return redirect('/done')

    return '''
    <!doctype html>
    <title>Messier API</title>
    <h1>Messier API</h1>
    <p>
        <a href="/messiers">All messiers</a>
    </p>
    <p>
        <a href="/messiers/visibility/param">Messiers by visibility</a>
    </p>
    <p>
        <a href="/messiers/season/param">Messiers by Season</a>
    </p>
    <p>
        <a href="/messiers/distance/float/float">Messiers by light-year distance</a>
    </p>
    '''

@app.route('/messiers', methods=['GET'])
def get_all_messier():
    """Return all available messiers.
    
    In JSON format.
    """
    messiers = return_all_messiers()
    return json.jsonify(messiers)


@app.route('/messiers/visibility/<visibility>', methods=['GET'])
def get_visible_messier(visibility):
    """Return all available messiers.
    
    In JSON format.
    """
    visibilityOptions = ['oeil', 'telescope']
    try:
        visibilityOptions.index(visibility)
    except ValueError:
        abort(400, description="Bad parameter : should be 'oeil' or 'telescope'")
    else:
        messiers = return_visible_messiers(visibility)
        return json.jsonify(messiers)


@app.route('/messiers/season/<season>', methods=['GET'])
def get_season_messier(season):
    """Return all available messiers.
    
    In JSON format.
    """
    seasonOptions = ['ete', 'hiver', 'automne', 'printemps']
    try:
        seasonOptions.index(season)
    except ValueError:
        abort(400, description="Bad parameter : should be 'printemps', 'ete', 'automne' or 'hiver'")
    else:
        messiers = return_season_messiers(season)
        return json.jsonify(messiers)

@app.route('/messiers/distance/<distancemin>/<distancemax>', methods=['GET'])
def get_distance_messier(distancemin, distancemax):
    """Return all available messiers.
    
    In JSON format.
    """
    try:
        float(distancemin)
        float(distancemax)
    except ValueError:
        abort(400, description="Bad parameter : should be type float")
    else:
        messiers = return_distance_messiers(distancemin, distancemax)
        return json.jsonify(messiers)
