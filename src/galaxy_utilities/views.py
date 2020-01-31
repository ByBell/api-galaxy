from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from galaxy_utilities.utils import allowed_file, upload_to_db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Core function of the app.
    
    Display a simple form to upload a document.
    For the most part, this is taken the official Flask documentation
    http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            content = file.read()
            name = secure_filename(file.filename)

            if upload_to_db(content, name):
                return redirect('/done')

    return '''
    <!doctype html>
    <title>Upload Image to S3</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/done', methods=['GET'])
def feedback():
    return '''
    <!doctype html>
    <title>Feedback</title>
    <h1>Thanks!</h1>
    <p>Your file has been uploaded.</p>
    <p>Go back to <a href="/">home page</a></p>
    '''
