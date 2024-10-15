from sqlalchemy import Table, Column, Integer, String, SmallInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models.models import Base
from library.db import Mysql


class StudentInfo(Base):
    __tablename__ = 'student_info1'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), comment="姓名")
    gender = Column(String(64), comment="性别")
    age = Column(String(64), comment="年龄")
    birthday = Column(String(64), comment="生日")
    cert_no = Column(String(64), comment="身份证号")
    education = Column(String(64), comment="教育程度")
    company = Column(String(64), comment="所在单位")
    phone = Column(String(64), comment="手机号")
    first_qualified = Column(String(64), comment="取证/复审")
    work_type = Column(String(64), comment="工种类别")
    work_project = Column(String(64), comment="工种")
    first_qualified_date = Column(String(64), comment="初次取证日期")
    last_check_date = Column(String(256), comment="上次复审日期")
    work_cert_no = Column(String(64), comment="证件编号")
    theory_exam_time = Column(DateTime, comment="理论时间")
    opration_exam_time = Column(DateTime, comment="实操时间")
    is_notified = Column(String(64), comment="是否通知到学员")
    status = Column(String(64), comment="学员状态")
    remark = Column(String(64), comment="备注")
    province = Column(String(64), comment="省")
    city = Column(String(64), comment="市")
    area = Column(String(64), comment="区")
    health_file_url = Column(String(256), comment="健康证明")
    cert_scan_url = Column(String(256), comment="身份证复印件")
    person_pic_url = Column(String(256), comment="个人照片")
    education_scan_url = Column(String(256), comment="学历证明")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)


def create_database():
    Base.metadata.create_all()


if __name__ == '__main__':
    Mysql.db.execute("show variables")
    # create_database()
