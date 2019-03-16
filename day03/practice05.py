# 编写Python程序判断字符串是否重复。（50分）
# 编写Python程序打印输出字符串中重复的所有字符。（50分）
# 把下面的klist作为字典的键
# 同时作为字典的值
# 把下面的klist作为字典的键
# 并统计每个单词的词频
if __name__ == '__main__':

    klist = [
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
        " day ","day"," up",
             ]
    mlist = [i.strip() for i in klist]
    mset = {i for i in mlist}
    mlist1=[i for i in mset]
    if len(mlist)!=mset:
        print("有重复")
    else:
        print("无重复")
    print("重复词",mset)
    mdict = {k: k for k in mset}
    print("mdic = {mdictkey}".format(mdictkey=mdict))
    mdict1 = {k: mlist1.count(k) for k in mset}
    print("mdic = {mdict1key}".format(mdict1key=mdict1))

    mlist = [i.strip() for i in klist]
    mset = {i for i in mlist}
    mlist1 = [i for i in mset]
    if len(mlist) != len(mset):
        print("有重复")
    else:
        print("无重复")
    print("重复词:",mset)
    mdict = {i:i for i in mset}
    print("mdict = {mdictkey}".format(mdictkey = mdict))
    mdict1 = {i:mlist.count(i) for i in mset}
    print("mdict1 = {mdict1key}".format(mdict1key=mdict1))
    print("mdic = {mdictkey}".format(mdictkey=mdict))
    mdict1 = {k: mlist1.count(k) for k in mset}
    print("mdic = {mdict1key}".format(mdict1key=mdict1))




    mset = {i.strip() for i in klist}
    mlist1 = [i.strip() for i in klist]
    mlist = [i.strip() for i in mset]
    if len(mset)!=len(mlist1):
        print("有重复")
    else:
        print("无重复")
    print("重复词：",mset)
    mdict = {k:k for k in mset}
    print("mdic = {mdictkey}".format(mdictkey = mdict))
    mdict1 = {k:mlist1.count(k) for k in mset}
    print("mdic = {mdict1key}".format(mdict1key = mdict1))

    mset = {i.strip() for i in klist}
    mlist = [i for i in mset]
    mlist1 = [i.strip() for i in klist]
    if len(mset) !=len(klist):
        print("有重复")
    else:
        print("没有重复")
    print(mset)
    mdict = {k:k for k in mset}
    print("mdict = {mdictKey}".format(mdictKey = mdict))
    mdict1 = {}
    for k in mset:
        mdict1[k]=mlist1.count(k)
    print("mdict1 = {mdictKey}".format(mdictKey=mdict1))

    mdict2 ={k:mlist1.count(k) for k in mset}
    print(mdict2)