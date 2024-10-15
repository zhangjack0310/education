import json
from tornado.options import options
from web import BaseHandler
from .services import StudentService
from tornado.web import RequestHandler
import traceback
import time
from functools import reduce
from library.oss import OSSService

work_type_map = {'低压电工作业': '电工作业', '高压电工作业': '电工作业', '电力电缆作业': '电工作业', '继电保护作业': '电工作业', '电气试验作业': '电工作业',
                 '防爆电气作业': '电工作业', '熔化焊接与热切割作业': '焊接与热切割作业',
                 '压力焊作业': '焊接与热切割作业', '登高架设作业': '高处作业', '高处安装、维护、拆除作业': '高处作业', '制冷与空调设备运行操作作业': '制冷与空调作业',
                 '制冷与空调设备安装修理作业': '制冷与空调作业',
                 '地下有限空间监护作业': '有限空间作业'}


class StudentInfoHandler(BaseHandler):
    def get(self):
        info = dict()
        self.finish(info)


    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body)
            # result = reduce(lambda x, y: x and y, data.values())
            # if not result:
            #     return self.finish({'success': 1, "data": {}, "insert": False, "reason": "信息填写不全"})
            # print(data.get("work_project"))
            # print(work_type_map)
            # print(work_type_map.get(data.get("work_project", ""), ""))
            data["work_type"] = work_type_map.get(data.get("work_project", ""), "")
            # print(data)
            res = StudentService.insert_student_info(data)
            self.json({'success': 1, "data": res, "insert": res})
        except:
            print(traceback.format_exc())
            self.json({'success': 1, "data": {}, "insert": False})



class GetOssTokenHandler(BaseHandler):
    def get(self):
        token_info = OSSService.gen_oss_token_info()
        return self.json(token_info)
