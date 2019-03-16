if __name__ == '__main__':
    # 1.	编写Python程序判断字符串是否重复。（50分）
    # 2.	编写Python程序打印输出字符串中重复的所有字符串。（50分）
    # 3.	#把下面的klist作为字典的键

    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up", ]

    # 创建set集合，并将去除空格后的元素放到集合中去重
    mset = {i.strip() for i in klist}
    # 将去从重后的数据放到mlist中
    mlist = [i.strip() for i in mset]
    # 方法1
    mdict = {}
    for i in mlist:
        mdict[i] = i
    print("mdict  = {mdict}".format(mdict = mdict))
    # 方法2
    mdict1 = {k: k for k in mlist}
    print("mdict  = {mdict1}".format(mdict1=mdict1))

    L = ['Hello', 'World', 'IBM', 'Apple']
    l = [i.lower() for i in L]
    print(l)

    L1 = ['Hello', 'World', 12.5, 'IBM', 'Apple', 6]
    l1 = []
    for i in L1 :
        if isinstance(i,str):
            l1.append(i.lower())
        else:
            l1.append(i)
    print(l1)

    l2= [str(i)+j for i in L1 for j in L]
    print(l2)

    def funl(l0):
        for i in l0:
            if isinstance(i, str):
                l1.append(i.lower())
            else:
                l1.append(i)
            return l1

    print(funl(L1))