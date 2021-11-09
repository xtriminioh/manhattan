# Manhattan - Proyecto de vista de informacion
import os
from flask import Flask
from flask import render_template
from flask import request

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

    @app.route('/dashboard', methods=('GET','POST'))
    def index():
        if request.method == 'POST':
            customer_name = request.form['CustomerName']
            print(customer_name)
        return render_template('index.html')

    return app
    
