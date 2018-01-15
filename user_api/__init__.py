"""Main entry point
"""
from pyramid.config import Configurator
#from urllib.parse import urlparse
# from gridfs import GridFS
# from pymongo import MongoClient


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    # config.include('pyramid_swagger')
    config.add_static_view('static', 'static', cache_max_age=3600)

    # db_url = urlparse(settings['mongo_uri'])
    # config.registry.db = MongoClient(
    #     host=db_url.hostname,
    #     port=db_url.port,
     

    # def add_db(request):
    #     db = config.registry.db[db_url.path[1:]]
    #     if db_url.username and db_url.password:
    #         db.authenticate(db_url.username, db_url.password)
    #     return db

    # def add_fs(request):
    #     return GridFS(request.db)

    # config.add_request_method(add_db, 'db', reify=True)
    # config.add_request_method(add_fs, 'fs', reify=True)

    config.add_route('user.getAll', '/user')

    config.scan("user_api.views")

    return config.make_wsgi_app()
