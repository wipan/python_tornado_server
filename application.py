# Routing and settings

import tornado.web
from views import handler
import config

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", handler.MainHandler),
            (r"/postpage", handler.PostPageHandler),
            (r"/home", handler.HomeHandler),
            (r"/function", handler.FuncHandler),
            (r"/escape", handler.EscapeHandler),
            (r"/students", handler.StudentsHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **config.settings)