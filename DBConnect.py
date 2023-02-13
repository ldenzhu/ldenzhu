# !/usr/bin/env python
# coding:utf-8

# Author:WHD

import pymysql

#定义创建表函数
def creat_table():
    # 创建数据库连接
    dbconn = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             passwd="871226Whd",
                             db="scientist",
                             charset='utf8')
    # 创建游标
    cursor = dbconn.cursor()

    #sql语句，如果不存在ethwallet table，则创建ethwallet table，一共walletid，walletname，walletaddr，privatekey，mnemonic，walletpath共6个变量
    sql = """CREATE TABLE IF NOT EXISTS ethwallet (
        walletid INT,
        walletname VARCHAR(40) NOT NULL,
        walletaddr VARCHAR(100) NOT NULL,
        privatekey VARCHAR(100) NOT NULL,
        mnemonic VARCHAR(100) NOT NULL,
        walletpath VARCHAR(100) NOT NULL )DEFAULT CHARSET=utf8;"""

    # 执行SQL，
    cursor.execute(sql)

    print("CREATE TABLE OK")

    dbconn.close()

#定义数据库插入操作
def dbinsertdata():
    # 创建数据库连接
    dbconn = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             passwd="871226Whd",
                             db="scientist",
                             charset='utf8')
    # 创建游标
    cursor = dbconn.cursor()

    # SQL插入语句
    sql = """
        INSERT INTO ethwallet(walletid,walletname,walletaddr,
        privatekey,mnemonic,walletpath)
        VALUES (%d,%s,%s,%s,%s,%s)""" % (walletid,walletname,walletaddr,privatekey,mnemonic,walletpath)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        dbconn.commit()
        print("insert success")
    except Exception as e:
        # Rollback in case there is any error
        dbconn.rollback()
        print("insert error")
        print('错误明细是', e)



    # 关闭游标
    cursor.close()

    # 关闭连接
    dbconn.close()

walletid = 1
walletname = "wallet1"
walletaddr = "0xffffffffffffffff"
privatekey = "0xfhsoihfoishfiosdhfiosd"
mnemonic = 'scrub crystal total farm element heart celery two huge steel market head'
walletpath = "m/44'/60'/0'/0/0"


#creat_table()
dbinsertdata()


