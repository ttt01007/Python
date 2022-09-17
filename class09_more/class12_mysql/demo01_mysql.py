import pymysql

# 连接数据库
con = pymysql.connect(host='101.43.160.228', user='root',
                      password='ttt01007', database='ss', port=3306)
# 创建游标
cur = con.cursor()


# # 查询sql
# sql = 'select * from t_test '
# # 执行sql
# cur.execute(sql)
# # 结果显示出来
# print(cur.fetchone())
# print(cur.fetchmany(3))
# print(cur.fetchall())

# 插入sql
# sql = 'insert into t_test values ("1","jianyu","18")'
# 执行sql
# cur.execute(sql)
# 增删改执行的sql要commit
# cur.execute('commit')

# 插入多个sql
sql = 'insert into t_test values (%s,%s,%s)'
values = (('2', 'jianyu2', '18'), ('3', 'jianyu3', '18'))
cur.executemany(sql, values)
# 增删改执行的sql要commit
cur.execute('commit')


# 关闭数据库
con.close()
