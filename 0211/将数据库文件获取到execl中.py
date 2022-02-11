# -*- coding: UTF-8 -*-
import pymysql
import openpyxl

#创建工作表
wb = openpyxl.Workbook()
s1 = wb.active
#添加表头
s1.title = '部门信息'
s1.append(('编号','部门名称','部门所在地'))

#创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='hrs',
    charset='utf8mb4'
)
#或取游标
try:
    with conn.cursor() as cu:
# 发送sql语句
        cu.execute(
            "select `dno`, `dname`, `dloc` from `tb_dept`"
        )
        #抓取数据
        row = cu.fetchone()
        while row:
            #将数据写入excel文件
            s1.append(row)
            row = cu.fetchone()
    #保存文件
    wb.save('hrs_tb_dept.xlsx')
except pymysql.MySQLError as err:
    print(type(err), err)
#关闭链接
finally:
    conn.close()





