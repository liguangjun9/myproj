import random
if __name__ == '__main__':
    birth1 = int(input("生日1"))
    birth2 = int(input("生日2"))
    # 判定生日大小
    if birth1<birth2:
        print("第一个人的生日大")
    elif birth2==birth1:
        print("两个人一样大")
    else:
        print("第二个人生日大")



    # 创建列表
    mlist = []
    # 循环生成序列
    for i in range(10):
        mlist.append(random.randint(1,20))
    num = random.randint(1, 50)
    print(mlist)
    print(num)
    # 判定是否存在
    if mlist.count(num)>0:
        print("存在")
    else:
        print("不存在")