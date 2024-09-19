from sqlalchemy.orm import scoped_session
from sqlalchemy import event
from tornado.options import options


class Mysql(object):
    db = None

    def __init__(self):
        event.listens_for(options.session_factory, 'after_flush')

    @staticmethod
    def create():
        Mysql.db = scoped_session(options.session_factory)

    @staticmethod
    def query(*args, **kwargs):
        Mysql.db.commit()
        try:
            return Mysql.db.query(*args)
        except:
            return Mysql.db.rollback()


    @staticmethod
    def save(obj=None, commit=True):
        try:
            if obj:
                Mysql.db.add(obj)
            if commit:
                Mysql.db.commit()
            return True
        except:
            Mysql.db.rollback()
            return False

    @staticmethod
    def ping_db():
        res = Mysql.db.execute("show variables")
        res.fetchall()
        print('ping database......')
