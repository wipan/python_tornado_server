# tornado server main function

import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.log
import config
from application import Application

if __name__ == "__main__":
    # enable log with builtin options
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(config.options['port'])
    tornado.ioloop.IOLoop.current().start()