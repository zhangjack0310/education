# coding=utf-8
import os

import tornado

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import define, options
from tornado.httpserver import HTTPServer

from library.db import Mysql
from config import local_settings as settings
from server import urls
from tornado.ioloop import PeriodicCallback

def suicide(signum, frame):
    os.system("kill -9 %d" % os.getpid())


def runserver():
    '''启动服务器'''
    tornado.options.parse_command_line()
    # redis
    # Redis.create(host=REDIS['HOST'], password=REDIS['PASSWORD'], port=REDIS['PORT'], db=REDIS['DATABASE'])
    # Redis.async_create(host=REDIS['HOST'], password=REDIS['PASSWORD'], port=REDIS['PORT'], selected_db=REDIS['DATABASE'])
    # 异步 redis

    # Mysql
    Mysql.create()
    # settings.APPLICATION_SETTINGS.update({
    #     "debug": False,
    #     'xsrf_cookies': False,
    #
    # })
    PeriodicCallback(Mysql.ping_db, 5 * 60 * 1000).start()
    Mysql.ping_db()
    application = Application(
        handlers=urls.urlpattern, debug=True,
        **settings.APPLICATION_SETTINGS
    )

    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(options.port)
    print('started')
    IOLoop.instance().start()


if __name__ == '__main__':
    runserver()
