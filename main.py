from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
import json

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
#设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/book'
#设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def to_json(inst, cls):
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        d[c.name] = v
    return json.dumps(d, cls=DateEncoder)


class Book(db.Model):
    # 定义表名
    __tablename__ = "bookinfo"
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    btitle = db.Column(db.String(64), unique=True)
    bpub_date = db.Column(db.DateTime, default=datetime.now)
    bread = db.Column(db.Integer, default=0)
    bcomment = db.Column(db.Integer, default=0)
    isDelete = db.Column(db.Integer, default=0)
    hero = db.relationship("Hero", backref="book")

    def __repr__(self):
        return '书籍:%s' % self.btitle

    @property
    def serialize(self):
        return to_json(self, self.__class__)


class Hero(db.Model):
    # 定义表名
    __tablename__ = "heroinfo"
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    hname = db.Column(db.String(64))
    hgender = db.Column(db.Integer)
    bcomment = db.Column(db.Integer, default=0)
    isDelete = db.Column(db.Integer, default=0)
    hbook_id = db.Column(db.Integer, db.ForeignKey("bookinfo.id"))

    def __repr__(self):
        return '人物:%s' % self.btitle


@app.route("/")
def index():
    return jsonify(Book.query.all())


if __name__ == '__main__':
    app.run()