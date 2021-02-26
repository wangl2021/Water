import pymysql
def loginsql(env):
    db = {
        'local': ['192.168.15.111', 'fish', '123456'],
    }
# 打开数据库连接
    db = pymysql.connect(
        host=db[env][0],
        user=db[env][1],
        password=db[env][2],
        database="qa",
        port=3306,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return db
def sqlInfo (env,sql,flag):
    db = loginsql(env)
    if flag == 1:
        curson=db.cursor()
        curson.execute(sql)
        info = curson.fetchall()
        print(info)
        return info

#sqlInfo('local', 'select * from peony', 1)



