import random
import pymysql


# 注意更换此处信息为你自己的数据库信息
parmas = {
    'host': 'localhost',
    'port': 3306,
    'user': 'atm',
    'passwd': 'balance',
    'db': 'test',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}

mydb = pymysql.connections.Connection(**parmas)  # 连接数据库




# 查看身份证状态
def id_status(id):
    mycursor = mydb.cursor()
    sql = f"select * from card where id='{id}' and status = 1 "

    if mycursor.execute(sql):  #### 1 表示被锁定  0 表示没有别锁定
        return False
    else:
        return True


# 插入用户信息
def insert_user(name, tel, id):
    mycursor = mydb.cursor()  # 获取游标
    sql = "insert into user values(%s,%s,%s)"
    info = (name, tel, id)
    mycursor.execute(sql, info)
    mydb.commit()
    mycursor.close()


# 随机生成卡号
def randomCardNum():
    cardnum = ''
    for i in range(6):
        cardnum += str(random.randint(0, 9))
    mycursor = mydb.cursor()
    sql = f"select cno from card where cno = '{cardnum}'"
    card = mycursor.execute(sql)
    mycursor.close()
    if card == cardnum:
        randomCardNum()
    return cardnum


# 插入卡信息
def insert_card(cno, id, pwd, balance, status):
    mycursor = mydb.cursor()  # 获取游标
    sql = "insert into card values(%s,%s,%s,%s,%s)"
    info = (cno, id, pwd, balance, status)
    mycursor.execute(sql, info)
    mydb.commit()
    mycursor.close()


# 查看是否存在卡
def isExistCard(cardNum):
    sql1 = f"select cno from card where cno='{cardNum}'"
    mycursor = mydb.cursor()
    if mycursor.execute(sql1):
        mycursor.close()
        return True
    else:
        mycursor.close()
        return False


# 查看卡状态
def card_status(cardNum):
    sql = f"select * from card where cno='{cardNum}' and status = 0"
    mycursor = mydb.cursor()
    if mycursor.execute(sql):
        mycursor.close()
        return True
    else:
        mycursor.close()
        return False
# 账号解锁函数
def unlock_card(cardNum,id):
    mycursor = mydb.cursor()
    sql1 = f"select * from card where cno='{cardNum}' and id = '{id}'"
    if mycursor.execute(sql1):
        sql2 = f"update card set status = 0 where cno='{cardNum}'"
        mycursor.execute(sql2)
        mydb.commit()
        mycursor.close()
        return True
    else:
        mycursor.close()
        return False
# 账号锁定函数
def lock_card(cardNum):
    mycursor = mydb.cursor()
    sql = f"update card set status = 1 where cno='{cardNum}'"
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()

# 注销账户函数
def del_account(cardNum):
    mycursor = mydb.cursor()
    sql1 = f"delete from card where cno='{cardNum}'"
    mycursor.execute(sql1)
    mydb.commit()
    mycursor.close()
    # 此处后续添加内容，若用户帐下无卡，则删除用户信息

# 检测密码
def is_pwd_correct(account, Pwd):
    mycursor = mydb.cursor()  # 获取游标
    sql = f"select pwd from card where cno='{account}'"
    mycursor.execute(sql)
    pwd=mycursor.fetchall()
    mycursor.close()
    if Pwd == pwd[0]['pwd']:
        return True
    else:
        return False

# 查看余额是否足够取款或转账
def is_cash_enough(account, num):
    mycursor = mydb.cursor()  # 获取游标
    sql = f"select balance from card where cno='{account}'"
    mycursor.execute(sql)
    pwd = mycursor.fetchall()
    mycursor.close()
    if int(num) <= pwd[0]['balance']:
        return True
    else:
        return False

# 取款写入数据库
def cash_out(account, num):
    mycursor = mydb.cursor()  # 获取游标
    sql1 = f"select balance from card where cno='{account}'"
    mycursor.execute(sql1)
    pwd = mycursor.fetchall()
    num = pwd[0]['balance']-int(num)
    sql2 = f"update card set balance= '{num}' where cno ={account}"
    mycursor.execute(sql2)
    mydb.commit()
    mycursor.close()

# 存款写入数据库或转账写入数据库
def deposit(account,num):
    mycursor = mydb.cursor()  # 获取游标
    sql1 = f"select balance from card where cno='{account}'"
    mycursor.execute(sql1)
    pwd = mycursor.fetchall()
    num = pwd[0]['balance'] + int(num)
    sql2 = f"update card set balance= '{num}' where cno ={account}"
    mycursor.execute(sql2)
    mydb.commit()
    mycursor.close()

# 查询余额，返回余额值
def inquiry(account):
    mycursor = mydb.cursor()  # 获取游标
    sql = f"select balance from card where cno='{account}'"
    mycursor.execute(sql)
    pwd = mycursor.fetchall()
    num=pwd[0]['balance']
    mycursor.close()
    return num


