import pymysql as pymysql

# 链接数据库
conn = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='test', charset='utf8')

# 创建游标
cursor =conn.cursor()

# sql语句
"""
# 建表
sql = '''CREATE TABLE zhang (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;'''

# 插入数据
sql = 'INSERT INTO USER1(name, age) VALUES (%s, %s);'
username = 'lisi'
age = 20

# 插入多条数据
sql = 'insert into zhang(name, age) values(%s, %s);'
data = [('zhangsan', 23), ('lisi', '25'), ('zhaoliu', 29)]

# 删除数据
sql = 'delete from zhang where id=%s'

# 查询
sql = 'select * from zhang where id=2'
# 执行查询语句
cursor.execute(sql)
# 查询一条数据
res = cursor.fetchone()

# 修改
sql = 'update zhang set name=%s where age=%s'
username = 'zqiang'
age = 23

"""
sql = 'select * from zhang'
cursor.execute(sql)
ret = cursor.fetchall()

# try:
#     # 执行sql语句
#     cursor.execute(sql, [username, age])
#     # 提交事物
#     conn.commit()
#     # 事物提交后，回去刚插入的id
#     last_id = cursor.lastrowid()
#
# except Exception as e:
#     # 有异常，回滚事物
#     conn.rollback()

# 关闭游标
cursor.close()

# 关闭链接的数据库
conn.close()

print(ret)
