from sqlalchemy import create_engine, MetaData
import os
import pymysql
import config.production_settings
from library.db import Mysql
from apps.education.models import StudentInfo
from sqlalchemy.orm import sessionmaker
Mysql.create()
from PIL import Image, ImageDraw, ImageFont
template_image_path = "/Users/laobzhang/PycharmProjects/education/test_form.jpg"


def form_student_application(student_id=20):
    cert_name = '身份证'
    right = '√'
    student = Mysql.query(StudentInfo).filter(StudentInfo.id == student_id).first()
    print(student)
    print(dir(student))

    name = student.name
    gender = student.gender
    age = student.age
    birthday = student.birthday
    education = student.education
    cert_no = student.cert_no
    company = student.company
    phone = student.phone



    # 打开一个已存在的图片
    image = Image.open(template_image_path)

    # 创建一个可以在给定图片上绘图的对象
    draw = ImageDraw.Draw(image)

    # 设置字体和大小
    font = ImageFont.truetype('Songti.ttc', size=22)

    # 设置文字颜色
    fill_color = (0, 0, 0)  # 红色文字

    # 在图片上添加文字
    draw.text((360, 335), name, font=font, fill=fill_color)
    draw.text((630, 335), gender, font=font, fill=fill_color)
    draw.text((840, 335), age, font=font, fill=fill_color)

    draw.text((350, 420), cert_name, font=font, fill=fill_color)
    draw.text((650, 420), cert_no, font=font, fill=fill_color)

    draw.text((315, 500), birthday, font=font, fill=fill_color)
    draw.text((840, 500), education, font=font, fill=fill_color)

    if len(company) <= 17:
        draw.text((310, 575), company, font=font, fill=fill_color)
    else:
        font_company = ImageFont.truetype('Songti.ttc', size=18)
        draw.text((300, 575), company, font=font_company, fill=fill_color)
    draw.text((840, 575), phone, font=font, fill=fill_color)

    first_qulified = student.first_qualified
    if first_qulified == "取证":
        work_type = student.work_type
        work_project = student.work_project

        draw.text((600, 665), work_type, font=font, fill=fill_color)
        draw.text((600, 760), work_project, font=font, fill=fill_color)
    else:
        work_type = student.work_type
        work_project = student.work_project
        first_qualified_date = student.first_qualified_date
        last_check_date = student.last_check_date
        work_cert_no = student.work_cert_no
        draw.text((600, 850), work_type, font=font, fill=fill_color)
        draw.text((600, 935), work_project, font=font, fill=fill_color)
        draw.text((520, 1025), first_qualified_date, font=font, fill=fill_color)
        draw.text((870, 1025), last_check_date, font=font, fill=fill_color)
        draw.text((600, 1120), work_cert_no, font=font, fill=fill_color)

    draw.text((910, 1205), right, font=font, fill=fill_color)
    image_name = "{}-{}-{}".format(work_project,first_qulified,name)
    # 保存修改后的图片
    image.save(f'{image_name}.jpg')


if __name__ == '__main__':
    form_student_application()
