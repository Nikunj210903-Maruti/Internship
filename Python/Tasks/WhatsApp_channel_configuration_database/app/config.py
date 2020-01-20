def configure_app(app):
    app.config['DATABASE_HOST'] = "localhost"
    app.config['DATABASE_USERNAME'] = "root"
    app.config['DATABASE_PASSWORD'] = "Nikunj210903"
    app.config['KARIX_HOST_URL'] = "http://localhost:5000"
    app.config['KARIX_CONSTANT'] = "karix"
    app.config['KARIX_AUTHANTICATION_URL'] = 'https://api.karix.io/account/'


