# -*- coding: UTF-8 -*-



import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

#创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='hrs',
    charset='utf8mb4'
)
#获取游标
try:
    with conn.cursor() as cu:
        #使用游标对象的execute向数据库发送sql语句
        affected_rows = cu.execute(
            'insert into `tb_dept` values (%s, %s, %s)',
            (no, name, location)
        )
        if affected_rows == 1:
            print("succeed")
    #提交事务
    conn.commit()
except pymysql.MySQLError as err:
    #回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    #关闭连接
    conn.close()
#发出sql语句

#执行语句

#关闭链接

'''

使用`pymysql`操作 MySQL 的步骤如下所示：

1. 创建连接。MySQL 服务器启动后，提供了基于 TCP （传输控制协议）的网络服务。
    我们可以通过`pymysql`模块的`connect`函数连接 MySQL 服务器。
    在调用`connect`函数时，需要指定主机（`host`）、端口（`port`）、
    用户名（`user`）、口令（`password`）、数据库（`database`）、
    字符集（`charset`）等参数，该函数会返回一个`Connection`对象。
2. 获取游标。连接 MySQL 服务器成功后，接下来要做的就是向数据库服务器
    发送 SQL 语句，MySQL 会执行接收到的 SQL 并将执行结果通过网络返回。
    要实现这项操作，需要先通过连接对象的`cursor`方法获取游标（`Cursor`）对象。
3. 发出 SQL。通过游标对象的`execute`方法，我们可以向数据库发出 SQL 语句。
4. 如果执行`insert`、`delete`或`update`操作，需要根据实际情况提交或回滚事务。
    因为创建连接时，默认开启了事务环境，在操作完成后，需要使用连接对象的`commit`
    或`rollback`方法，实现事务的提交或回滚，`rollback`方法通常会放在异常捕获代
    码块`except`中。如果执行`select`操作，需要通过游标对象抓取查询的结果，
    对应的方法有三个，分别是：`fetchone`、`fetchmany`和`fetchall`。
    其中`fetchone`方法会抓取到一条记录，并以元组或字典的方式返回；`fetchmany`
    和`fetchall`方法会抓取到多条记录，以嵌套元组或列表装字典的方式返回。
5. 关闭连接。在完成持久化操作后，请不要忘记关闭连接，释放外部资源。
    我们通常会在`finally`代码块中使用连接对象的`close`方法来关闭连接。

'''


