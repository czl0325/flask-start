# flask-start
入门flask，第一个flask的练习


### flask的常用插件

```
Flask-SQLalchemy：操作数据库；
Flask-migrate：管理迁移数据库；
Flask-Mail:邮件；
Flask-WTF：表单；
Flask-script：插入脚本；
Flask-Login：认证用户状态；
Flask-RESTful：开发REST API的工具；
Flask-Bootstrap：集成前端Twitter Bootstrap框架；
Flask-Moment：本地化日期和时间；
```

### flask文档
- 中文文档： http://docs.jinkan.org/docs/flask/
- 英文文档： http://flask.pocoo.org/docs/0.11/

### flask第一个helloworld项目
```
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run()
```

#### app的run参数
- app.run(host=”0.0.0.0”, port=5000)

#### app查看所有路由
- app.url_map

#### url反解析
- url_for


### 常用的SQLAlchemy字段类型

| 类型名 |python中类型 |  说明|
| :---: | :---: | :---: |
|Integer |int| 普通整数，一般是32位
|SmallInteger  |  int| 取值范围小的整数，一般是16位
|BigInteger  |int或long    |不限制精度的整数
|Float |  float |  浮点数
|Numeric |decimal.Decimal |普通整数，一般是32位
|String  |str| 变长字符串
|Text  |  str |变长字符串，对较长或不限长度的字符串做了优化
|Unicode |unicode |变长Unicode字符串
|UnicodeText |unicode |变长Unicode字符串，对较长或不限长度的字符串做了优化
|Boolean |bool  |  布尔值
|Date  |  datetime.date |  时间
|Time  |  datetime.datetime  | 日期和时间
|LargeBinary |str |二进制文件
