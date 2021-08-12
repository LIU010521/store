'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''

import random
def luck_draw():
    a = random.randint(1,45)
    if a <= 10:
        return 1
    elif 10 < a <= 30:
        return 2
    elif 30 < a <= 45:
        return 3

shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]
# 1.空的购物车
mycart = []
#  2.初始化您的余额
money = input("请输入您本月工资：")
money = int(money)

# 展示商品
for key, value in enumerate(shop):
    print(key, value)

n = luck_draw()
if n == 1:
    print("恭喜你抽中联想电脑全5折券")
    for key in range(len(shop)):
        if shop[key][0] == "lenovo PC":
            shop[key][1] *= 0.5

elif n == 2:
    print("恭喜你抽中老干妈全1折券")
    for key in range(len(shop)):
        if shop[key][0] == "老干妈":
            shop[key][1] *= 0.1

elif n == 3:
    print("恭喜你抽中华为全6折券")
    for key in range(len(shop)):
        if shop[key][0] == "HUAWEI  WATCH PRO 20":
            shop[key][1] *= 0.6

# 3.正常购物
i = 1
while i <= 20:
    chose = input("请输入您想要的商品：")
    if chose.isdigit():     #判断字符串chose是否是数字，如果是返回True，不是返回False
        chose = int(chose)
        if chose > len(shop): # len
            print("没有改号商品！请重新输入！")
        else:
            # 钱够不够
            if money > shop[chose][1]:
                mycart.append(shop[chose])
                money = money - shop[chose][1] # 减去价格
                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("对不起，您输入错误，别瞎弄！")


    i = i + 1


count = []

for key,value  in enumerate(mycart): #统计每个商品在列表中出现几次
    if value in mycart[:key]:
        continue
    count.append(mycart.count(mycart[key]))

#删除二维列表这重复的行，必须先把列表中每个元素转化为tuple，因为list不可哈希但是tuple可哈希
mycart = list(set([tuple(t) for t in mycart]))

for k in mycart:    #tuple换回list
    mycart[mycart.index(k)] = list(k)

print("以下是您的购物小条，请拿好！")
print("---------------------------------------")
for key,value  in enumerate(mycart):
    print(key,"------",value[0],"  价格：￥",value[1],"  数量:",count[key])
print("---------------------------------------")
print("您的余额还剩：￥",money)