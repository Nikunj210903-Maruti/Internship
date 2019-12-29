from .manage import create_app, app_init_task
from app.services.sendmail import publish

filename = "sample.csv"


__all__ = ["app", "api", "cache_store", "socket", "jwt", "run_server"]

app = create_app()

app_init_task()


@app.route('/send_mail')
def sample():
    publish(filename)
    return "ok"

def run_server():
    """Eventlet Server"""
    app.run(port=app.config.get('PORT'))
