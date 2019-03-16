def checkSex():
    mane = input("输入姓名:")
    sex = input("输入性别")
    # 创建两个个字典
    mdict1 = {'male':'male,男,Mr',}
    mdict2 = {'female':'female,女,Mis'}

    for sexs in mdict1.values():
        if sexs.find(sex)>0:
            print(mdict1+"先生你好")

    for sexs in mdict2.values():
        if sexs.find(sex)>0:
            print(mdict1+"女士你好")

def checkSex1():
    na = input("输入姓名和性别【姓名—性别】")
    nlist = na.split("-")
    print(nlist)
    sex1={"sex":"male,男,Mr"}
    sex2={"sex":"female,Mis,女"}
    for i in sex1.values():
        if i.find(nlist[1])>0:
            print(nlist[0]+"先生你好")
    for i in sex2.values():
        if i.find(nlist[1])>0:
            print(nlist[0]+"女士你好")

def checkSex2():
    mane = input("输入姓名:")
    sex = input("输入性别")
    # 创建两个个字典
    mdict1 = {'male': 'male,男,Mr', }
    mdict2 = {'female': 'female,女,Mis'}

    for sexs in mdict1.values():
        if sexs.find(sex) > 0:
            print(mdict1 + "先生你好")

    for sexs in mdict2.values():
        if sexs.find(sex) > 0:
            print(mdict1 + "女士你好")

    pass
if __name__ == '__main__':
    checkSex1()