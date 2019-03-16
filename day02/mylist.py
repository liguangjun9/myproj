if __name__ == '__main__':
    # 两种创建列表的方式
    mlist = list();
    mlist1 = [ ]
    # 在列表尾部添加数据
    mlist.append("1")
    mlist = list();

    print(type(mlist))
    # 在指定位置添加数据
    mlist.insert(0,"学委")
    mlist.append("生委")
    mlist.insert(5,"爱护我")
    print(mlist)
    # 使用pop从列表中删除数据（尾部删除并返回所要删除数据）
    #index:从index位置删除并返回数据，如果index越界会报异常
    mlist.pop()
    print(mlist)
    # 如果不指定具体删除数据，打印时就会报错（没有定义对象）
    del mlist[0]
    print(mlist)
    #删除的是对象，打印时会报错（没有定义对象）；可以指定具体数据进行删除
    #如果该数据不存在会抛出异常
    mlist.remove()
    # 指定删除
    print(mlist)
    #清空列表内部内容，并保留对象
    mlist.clear()