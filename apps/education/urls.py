from tornado.web import url
from tornado.options import options
from .handlers import StudentInfoHandler
from .handlers import GetOssTokenHandler


base_url = r'/education/'
urlpattern = (
    # 用户信息
    url(base_url + 'student_info/$', StudentInfoHandler),
    url(base_url + 'oss/get_token/$', GetOssTokenHandler),
)
