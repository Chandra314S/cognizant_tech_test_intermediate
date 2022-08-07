import os
import hashlib
import datetime
import json
import csv
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, Response
from flask import send_from_directory
from werkzeug.utils import secure_filename
from pprint import pprint
from csvconverter import *

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(401)
def ERROR_401(error):
    flash('You\'re not allowed to access.', category='danger')
    return render_template("index.html"), 401

@app.errorhandler(403)
def ERROR_403(error):
    flash('This operation is forbidden.', category='danger')
    return render_template("index.html"), 403

@app.errorhandler(404)
def ERROR_404(error):
    flash(' The resource can not be found.', category='danger')
    return render_template("index.html"), 404

@app.errorhandler(405)
def ERROR_405(error):
    flash('The method of your request is not allowed.', category='danger')
    return render_template("index.html"), 405

@app.errorhandler(413)
def ERROR_413(error):
    flash('Please check the file size you\'re uploading.', category='danger')
    return render_template("index.html"), 413


@app.route("/")
def APP_root():
    return render_template("index.html")

ALLOWED_EXTENSIONS = set(['csv'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/dataupload", methods = ['POST'])
def UploadData():
    print(app.root_path)
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', category='danger')
            return(redirect(url_for("APP_root")))
        file = request.files['file']

        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            flash('No selected file', category='danger')
            return(redirect(url_for("APP_root")))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_time = str(datetime.datetime.now())
            file_uid = hashlib.sha1((upload_time + filename).encode()).hexdigest()

            # Save the File into Uploader
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_uid + "-" + filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_uid + "-" + filename))
            # flash("File Processed sucessfully ",category='info')

            results_path = os.path.join(app.config['RESULTS_FOLDER'], file_uid + "-" + '.json')
            processed_Data = JsonDataParser().DataParser(file_path,results_path)
            # processed_Data = DataParser(file_path,results_path)
            # flash('File download started.', category='success')
            return Response(
                processed_Data,
                mimetype="text/json",
                headers={"Content-disposition":
                        f"attachment; filename=ParsedJsonFile-{filename.split('.')[0]}.json"})

    return(redirect(url_for("APP_root")))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")