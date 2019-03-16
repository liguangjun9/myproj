if __name__ == '__main__':
    # 1.	编写Python程序判断字符串是否重复。（50分）
    # 2.	编写Python程序打印输出字符串中重复的所有字符串。（50分）
    # 3.	#把下面的klist作为字典的键
    klist =  [
    "good ","good ","study",
    " good ","good","study ",
    "good "," good"," study",
    " good ","good"," study ",
    "good ","good ","study",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",]
    mlist1=klist[::1]
    print(mlist1)
    # 创建set集合，并将去除空格后的元素放到集合中去重
    mset = {i.strip() for i in klist}
    # 将去从重后的数据放到mlist中
    mlist = [i.strip() for i in mset]
    # 创建字典
    mdict = {}
    for i in mset:
        # 以键值对的形式将数据放入到字典中
        mdict[i] = mlist.count(i)
        # 通过for循环遍历出重复的字符串
        if mlist.count(i):
            print(i)
    print(mdict)
    # 创建set集合,将klist中的元素去除左右空格并放入mset集合中
    mset = {i.strip() for i in klist}
    klist1 = [i.strip() for i in klist]
    # 判断是否有重复
    if len(klist)!=len(mset):
        print("字符串有重复")
    else :
        print("字符串没有重复")
    # 创建列表并将去重后的字符串放入
    newklist = [i for i in mset]
    print(newklist)
    for i in newklist:
        for j in i:
            # 打印出所有重复字符
            print(j)
    coun = 0
    # 创建字典
    mdic = {}
    for i in mset:
        # 以键值对的形式
        mdic[i]=klist1.count(i)
    print(mdic)

