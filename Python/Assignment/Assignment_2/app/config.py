__all__ = ['configure_app']

def configure_app(app):
    app.config['SECRET_KEY'] = "amqp://guest:guest@localhost:5672/%2F"
    app.config['HOST'] = "localhost"
    app.config['USER'] = "root"
    app.config['PASSWORD'] = ""
    app.config['DATABASE_NAME'] = "Inventory"

