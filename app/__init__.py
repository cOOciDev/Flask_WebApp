import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))



def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_pyfile('../config/config.py')

    # Import and register blueprints
    from app.views.home_views import bp as home_bp
    from app.views.owner_views import bp as ownerpage_bp
    from app.views.modeling_views import bp as modelingpage_bp
    from app.views.animating_views import bp as animatingpage_bp
    from app.views.coding_views import bp as codingpage_bp
    from app.views.news_views import bp as newspage_bp
    from app.views.contactUs_views import bp as contactuspage_bp
    from app.views.havesomefun_views import bp as havesomefunpage_bp
    from app.views.cOOciAcademy_views import bp as cOOciacademypage_bp
    from app.views.cOOciGames_views import bp as cOOcigamespage_bp
    


    app.register_blueprint(home_bp)
    app.register_blueprint(ownerpage_bp)
    app.register_blueprint(modelingpage_bp)
    app.register_blueprint(animatingpage_bp)
    app.register_blueprint(codingpage_bp)
    app.register_blueprint(newspage_bp)
    app.register_blueprint(contactuspage_bp)
    app.register_blueprint(havesomefunpage_bp)
    app.register_blueprint(cOOciacademypage_bp)
    app.register_blueprint(cOOcigamespage_bp)

    return app