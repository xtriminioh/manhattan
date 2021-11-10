# Manhattan - Proyecto de vista de informacion
import os
from flask import Flask
from flask import(flash, request, render_template, url_for, redirect)
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.getcwd(),'src/files') 
ALLOWED_EXTENSIONS = {'xlsx'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/dashboard', methods=['GET','POST'])
    def dashboard():
        if request.method == 'POST':
            customer_name = request.form['CustomerName']
            print(customer_name)
        return render_template('search.html')

    @app.route('/upload', methods=['GET','POST'])
    def upload():
        if request.method == 'POST':
            if 'file' not in request.files:
                flash(f'No file part', 'warning')
                return redirect(request.url)
            ffile = request.files['file']

            if ffile.filename == '':
                flash(f'No selected file', 'info')
                return redirect(request.url)

            if ffile and allowed_file(ffile.filename):
                filename = secure_filename(f'{ffile.filename}')
                filename = filename.lower()
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                ffile.save(filepath)
                flash(f'Saved!! file: {filename}', 'success')
                return redirect(request.url)

        return render_template('upload.html')

    return app

