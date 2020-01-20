import cherrypy

from app import app

if __name__ == '__main__':
    try:
        # Mount the application
        cherrypy.tree.graft(app, "/")

        # Set the configuration of the web server
        cherrypy.config.update({
            'log.screen': True,
            'server.socket_port': app.config['PORT'],
            'server.socket_host': '::',
            'server.thread_pool': 30,
            'server.shutdown_timeout': 1
        })
        cherrypy.engine.start()
        cherrypy.engine.block()
    except KeyboardInterrupt:
        cherrypy.engine.stop()


