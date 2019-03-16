if __name__ == '__main__':
    mdict = {"name":"good","password":"123"}
    print(type(mdict))
    # 这种遍历方式取出的是键
    for k in mdict:
        # 显示的类型是str
        print("type is {0}".format(type(k)))
        print(k)
    print("======================")
    # 这种遍历方式取出的是值
    for v in mdict.values():
    # 显示的类型是str
        print("type is {0}".format(type(v)))
        print(v)
    print("======================")
    # 这种遍历方式取出来的是键值对
    for kv in mdict.items():
        print("type id {0}".format(type(kv)))
        print(kv)
