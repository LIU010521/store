'''
    1.任务1：
    三组开发：工行
    三组开发：农行
    任务2：
        工行与农行跨行转账的手续费
        1.转账2000元以下。    异地同行或跨行转账手续费是ATM转账是1.6元/笔.
        2.转账2000-5000元。   异地同行或跨行转账手续费是ATM转账是4元/笔.
        3.转账5000-10000元。  异地同行或跨行转账手续费是ATM转账是8元/笔
        4.转账10000-50000元。 异地同行或跨行转账手续费是ATM转账是12元/笔。
        5.转账50000元以上。   异地同行或跨行转账手续费是ATM转账金额的0.03%，最高50元。



'''


# 准备数据
bank = {}
bank_name = "中国工商银行昌平回龙观支行ICBC-568-01502"
import random

def bank_addUser(username,password,country,province,street,door,account,money):
    # 是否已满
    if len(bank) >= 100:
        return 3
    # 是否存在
    if username in bank:
        return 2
    # 正常开户
    bank[username] = {
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1
#存款
def bank_savemoney(username,savemoney):
    #是否存在
    if username not in bank:
        return "False"
    #正常存款
    bank[username]["money"] = bank[username]["money"] + savemoney
    return 2

#取款
def bank_drawmoney(username,password,drawmoney):
    #是否存在
    if username not in bank:
        return 1
    #密码是否正确
    elif password != bank[username]["password"]:
        return 2
    #钱不够取
    elif drawmoney > bank[username]["money"]:
        return 3
    #正常取款
    else:
        bank[username]["money"] = bank[username]["money"] - drawmoney
        return "qwq"

#转账
def bank_transfer(username,username2,password,money):
    #是否存在转入转出账号
    if username not in bank or username2 not in bank:
        return 1
    #密码是否正确
    elif password != bank[username]["password"]:
        return 2
    # 钱不够取
    elif money > bank[username]["money"]:
        return 3
    #转出金额减少，转入金额增加
    else:
        bank[username]["money"] -= money
        bank[username2]["money"] += money
        return "qaq"

#查询
def bank_query(username,password):
    #用户是否存在
    if username not in bank:
        return 1
    #密码是否正确
    elif password != bank[username]["password"]:
        return 2
    #打印信息
    else:
        return 3

def addUser():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    country = input("亲输入国籍：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入门牌号：")
    money = int(input("亲初始化您的开卡余额："))
    account = random.randint(10000000,99999999)
    status = bank_addUser(username,password,country,province,street,door,account,money)
    if status == 3:
        print("对不起，银行库已满，请携带证件到其他银行办理！")
    if status == 2:
        print("对不起，您已开过户！请不要重复开户！")
    if status == 1:
        print("恭喜，开户成功！以下是您的开户信息：")
        info = '''
        -----------------------------
                个人信息
            账号：%s
            用户名：%s
            密码：*****
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
        -------------------------------
        '''
        print(info  % (account,username,country,province,street,door,money,bank_name))

#存款
def savemoney():
    username = input("请输入用户名：")
    savemoney = int (input("请输入存款金额："))
    a = bank_savemoney(username,savemoney)
    if a == "False":
        print("对不起，您的账户不存在！")
    if a == 2:
        print("存款成功！您的余额为：",bank[username]["money"])

#取款
def drawmoney():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    drawmoney = int(input("请输入取款金额"))
    b = bank_drawmoney(username,password,drawmoney)
    if b == 1:
        print("对不起，您的账户不存在！")
    if b == 2:
        print("对不起，您的密码错误！")
    if b == 3:
        print("对不起，您的余额不足！")
    if b == "qwq":
        print("取款成功！您的余额为：",bank[username]["money"])

#转账
def transfer():
    username = input("请输入用户名：")
    username2 = input("请输入用户名：")
    password = input("请输入密码：")
    money =int(input("请输入转账金额："))
    c = bank_transfer(username,username2,password,money)
    if c == 1:
        print("对不起，您的账号不存在！")
    if c == 2:
        print("对不起，您的密码错误！")
    if c == 3:
        print("对不起，您的余额不足！")
    if c == "qaq":
        print("转账成功！您的余额为：",bank[username]["money"])

#查询
def query():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    d = bank_query(username,password)
    if d == 1:
        print("该用户不存在！")
    if d == 2:
        print("密码错误！")
    if d == 3:
        print("查询成功，以下为您的个人信息")
        print("当前账户：",bank[username]["account"])
        print("密码：",bank[username]["password"])
        print("余额：",bank[username]["money"])
        print("用户居住地址：",bank[username]["country"])
        print("当前账户的开户行：",bank[username]["bank_name"])

def welcome():
    print("----------------------------------")
    print("-   中国工商银行账户管理系统       -")
    print("----------------------------------")
    print("-  1.开户                         -")
    print("-  2.存钱                         -")
    print("-  3.取钱                         -")
    print("-  4.转账                         -")
    print("-  5.查询                         -")
    print("-  6.Bye!                         -")
    print("----------------------------------")

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        savemoney()
    elif chose == "3":
        drawmoney()
    elif chose == "4":
        transfer()
    elif chose == "5":
        query()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！再弄三次锁定！")





