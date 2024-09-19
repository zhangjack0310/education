from sqlalchemy import Table, Column, Integer, String, SmallInteger, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from library.db import Mysql

# from config.production_settings import some_engine, meta
# meta.reflect(some_engine)
from sqlalchemy.ext.declarative import declarative_base
BaseModel = declarative_base()


class Base(BaseModel):
    __abstract__ = True

    @classmethod
    def filter_by(cls, **kwargs):
        return Mysql.query(cls).filter_by(**kwargs)

    def save(self, obj=None, commit=True):
        return Mysql.save(obj=obj, commit=commit)



# class StudentInfo(Base):
#     __tablename__ = 'student_info'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(64), comment="姓名")
#     gender = Column(String(64), comment="性别")
#     age = Column(String(64), comment="年龄")
#     birthday = Column(String(64), comment="生日")
#     cert_no = Column(String(64), comment="身份证号")
#     education = Column(String(64), comment="教育程度")
#     company = Column(String(64), comment="所在单位")
#     phone = Column(String(64), comment="手机号")
#     first_qualified = Column(String(64), comment="取证/复审")
#     work_type = Column(String(64), comment="工种类别")
#     work_project = Column(String(64), comment="工种")
#     first_qualified_date = Column(String(64), comment="初次取证日期")
#     last_check_date = Column(String(256), comment="上次复审日期")
#     work_cert_no = Column(String(64), comment="证件编号")
#     theory_exam_time = Column(DateTime, comment="理论时间")
#     opration_exam_time = Column(DateTime, comment="实操时间")
#     is_notified = Column(String(64), comment="是否通知到学员")
#     status = Column(String(64), comment="学员状态")
#     remark = Column(String(64), comment="备注")
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now)

def create_database():
    Base.metadata.create_all()


if __name__ == '__main__':
    create_database()

