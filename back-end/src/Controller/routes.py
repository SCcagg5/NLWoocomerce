from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',            ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])               )
    @app.route('/input/',           ['OPTIONS', 'POST'],        lambda x = None: call([connect, input])  )
    def base():
        return
