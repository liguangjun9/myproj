import random
if __name__ == '__main__':
    # 内建结构——列表
    # 创建列表的两种方式，索引0开始不是从1开始
    # 第一种方式
    mlist = list()
    # 第二种方式
    mlist1 = []
    print(type(mlist))
    # 使用append在列表尾部添加数据
    mlist.append("张三")
    print(mlist)
    # 使用insert在列表的指定位置添加数据
    mlist.insert(0,"李斯")
    print(mlist)
    # 删除整个列表的方法
    del mlist
    # 由于已经删除列表，给对象已将不存在，不能输出列表的值
    # 如果输出列表会报错（NameError:name 'mlist' is not defined）
    # print(mlist)
    # 初始化mlist1
    mlist1 = [i for i in range(1,10)]
    print(mlist1)
    # 使用pop从列表删除数据列表，如果不指定参数则删除最后一个数据并返回所要删除的数据
    ty = mlist1.pop()
    print("mlist1.pop() = {name}".format(name = ty))
    print(mlist1)
    # 指定参数删除数据
    mlist1.pop(1)
    print(mlist1)
    # 使用clear（）：保留列表本身，但清空列表中的数据
    mlist1.clear()
    print(mlist1)
    # 创建slist列表
    slist = [i for i in range(5)]
    print(slist)
    # 导包random,将列表打乱
    random.shuffle(slist)
    print(slist)
    # 将列表降序排序
    slist.sort(reverse=True)
    print(slist)
    # 将列表生序排序
    slist.sort()
    print(slist)
    # 将列表打乱顺序
    random.shuffle(slist)
    print(slist)
    # 将列表翻转
    slist.reverse()
    print(slist)
    # 临时升序排列,临时排序需要声明一个变量来接收,生成一个新的列表，不会改变原来列表的排序
    newlist = sorted(slist)
    print(newlist)
    print(slist)
    # 求列表的长度的两种方式
    # 第一种
    l1=slist.__len__()
    print(l1)
    # 第二种
    l2 = len(slist)
    print(l2)
    # 获取当前元素在列表中的位置(_index_返回的是当前元素在列表的位置，而不是索引值)
    for i in slist:
        print("slist[{0}]={1}".format(i.__index__(),i))
    print("slist id is {slistid}".format(slistid = id(slist)))
    print("slist id is {mlistid}".format(mlistid = id(mlist1)))
    # 判断目标元素是否在列表中
    num = 5
    print(num in slist)
    print(num not in slist)