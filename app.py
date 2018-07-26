import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

from handlers import main


define('port', default=8000, help='run port', type=int)


class Applications(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', main.IndexHandler),
            ('/explore', main.ExploreHandler),
            ('/post/(?P<post_id>\d+)', main.PostHandler),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
        )
        super(Applications,self).__init__(handlers, **settings)


applications = Applications()
if __name__ == "__main__":
    parse_command_line()
    print('服务运行在%s端口上' % options.port)
    applications.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
