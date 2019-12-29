from flask import Flask
from .config import configure_app

__all__ = ['create_app', 'app_init_task', 'ws_init']

def create_app():
    """Initialize Flask Application"""
    app = Flask(__name__, template_folder="template")
    configure_app(app)
    return app

def init_task(api):
    from .resources.index import Index
    from .resources.update_page import Update_page
    from .resources.delete_page import Delete_page
    from .resources.search_page import Search__page
    from .resources.insert_page import Insert_page
    from .resources.insert import Insert
    from .resources.update import Update
    from .resources.delete import Delete
    from .resources.search import Search

    api.add_resource(Index, '/')
    api.add_resource(Update_page, '/update_page')
    api.add_resource(Delete_page, '/delete_page')
    api.add_resource(Search__page, '/search_page')
    api.add_resource(Insert_page, '/insert_page')
    api.add_resource(Insert, '/insert')
    api.add_resource(Update, '/update')
    api.add_resource(Delete, '/delete')
    api.add_resource(Search, '/search')
