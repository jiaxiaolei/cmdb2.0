# *_* coding=utf8 *_*

import os
import sys
import logging

from tornado.options import options, define, parse_command_line
from django.core.wsgi import get_wsgi_application

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "conf.settings"

define('port', type=int, default=8000)
# deploy or debug
define('mode', default='debug')


def main():
    parse_command_line()

    if options.mode.lower() == "debug":
        from tornado import autoreload
        autoreload.start()

    wsgi_app = tornado.wsgi.WSGIContainer(get_wsgi_application())

    tornado_app = tornado.web.Application(
        [('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
         ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    logging.warn("[CMDB] CMDB is running on localhost:%d", options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
