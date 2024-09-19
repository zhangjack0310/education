import tornado
import tornado.web
import json
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.set_allow_origin()

    def set_allow_origin(self):
        """Set allow origin"""
        # self.set_header(
        #     'Access-Control-Allow-Headers',
        #     'Origin, X-Requested-With, Content-Type, Accept',
        # )
        # self.set_header("Access-Control-Allow-Headers", "X-Requested-With, accept, content-type, xxxx")

        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header('Access-Control-Allow-Methods', 'GET, HEAD, POST, OPTIONS, DELETE')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Origin', '*')

    def options(self):
        self.set_header(
            'Access-Control-Allow-Headers',
            'Origin, X-Requested-With, Content-Type, Accept',
        )
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header('Access-Control-Allow-Methods', 'GET, HEAD, POST, OPTIONS')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_status(204)
        self.finish()


    def finish(self, chunk=None):
        self.response_data = {
            'code': 1,
            'msg': 'success'
        }
        data = {
            'code': self.response_data.get('code'),
            'msg': self.response_data.get('msg'),
            'data': chunk or {}
        }
        return super(BaseHandler, self).finish(chunk=json.dumps(data))
