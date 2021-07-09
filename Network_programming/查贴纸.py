import pymysql

# 创建连接'
user = 'versa'
password = 'ZmnRZhvy7iTnVjl'
host = 'rm-uf68ea46v74l36g67.mysql.rds.aliyuncs.com'
database = 'versa'
a = '207191703441690624'
conn = pymysql.connect(user=user,
                       password=password,
                       host=host,
                       database=database,
                       port=3306,
                       charset='utf8',
                       autocommit=False)

# 获取游标
cur = conn.cursor()
# 执行sql语句
sql = 'SELECT category_name from sticker_category where category_id = '+ a +';'
res = cur.execute(sql)
# 获取执行结果
ret = cur.fetchall()
print(ret)
# 关闭游标和链接
cur.close()
conn.close()
