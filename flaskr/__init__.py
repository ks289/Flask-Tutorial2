import os

from flask import Flask

def create_app(test_config=None):
    # creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    
    if test_config is None:
        # loading instance config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # loading the test config if specified
        app.config.from_mapping(test_config)
        
    # ensuring the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # simple page for now
    @app.route('/hello')
    def hello():
        return 'Hello'
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app