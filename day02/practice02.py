if __name__ == '__main__':

    # 创建字符串
    mstr = "aabbccdef"
    # 创建mlist链表，将字符串通过for循环放入到mlist链表中
    mlist = [i for i in mstr]
    # 创建mset集合，将字符串通过for循环放入到mset集合中
    mset = {i for i in mstr}
    # 因为set有去重属性，可以通过判断mlist和mset的长度，确定字符串中是否有重复
    if mset.__len__()<mlist.__len__():
        print("字符串中有重复")
    else:
        print("字符串中没有重复")
    # 创建一个字典
    mdic = {}
    mlist1 = [i for i in mset]
    print(mlist1)
    for i in mlist1:
        for j in i:
            cout=mlist.count(j)
            print(i,cout)
    # 通过遍历循环将字符与出现次数以键值对的形式放入其中
    for i in mset:
        mdic[i]=mlist.count(i)
    print(mdic)