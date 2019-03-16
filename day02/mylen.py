if __name__ == '__main__':
    # len()方法
    mlist =[1,2,3,4,5,6]
    # 求链表的长度
    mlen = len(mlist)

    print(mlen)

    print(type(mlist))
    for l in mlist:
        # 只能是同种数据类型，如果是不同的类型就会报错
        print("mlist[{0}] = {1}".format(l.__index__(),l))
    nlist = mlist[0:3]
    print("mlist id is {mlistid}".format(mlistid=id(mlist)))
    print("mlist id is {nlistid}".format(nlistid=id(nlist)))

