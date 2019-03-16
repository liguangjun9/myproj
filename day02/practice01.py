if __name__ == '__main__':
    # find方法
    print("============find方法============")
    stri = "afuqweoirqi,tourryoirjkglvew,qgwderwafdsz,vcrrxregfd"
    # 搜索没有的字符
    val = stri.find(";")
    print(val)
    # 搜索有的字符
    val = stri.find("a")
    print(val)
    # 指定开始索引值
    val = stri.find("u",5)
    print(val)
    # 指定开始和结束的索引值
    val = stri.find("u",5,10)
    print(val)

    print("============index方法============")
    # index方法
    # 输入一个参数
    val1 = stri.index("rr")
    print(val1)
    # 输入两个参数
    val1 = stri.index("rr",15)
    print(val1)
    # 输入三个参数,在这个指定区间不会出现搜索的,指定的结束索引值不会。（会抛出异常valueError:substring not found）
    val1 = stri.index("rr",15,100)
    print(val1)
    print("============count方法============")
    mcount = stri.count("rr")
    print(mcount)
    mcount = stri.count("a",5)
    print(mcount)
    mcount = stri.count("b",1,15)
    print(mcount)
    print("============replace方法============")
    # 替换类型要相同,返回值是替换后的新字符串,第三个参数是表示替换的次数（超出最大替换次数不会报错）
    repl = stri.replace("rr",str(1),1)
    print(repl)
    print("============split方法============")
    sp = stri.split("rr")
    # 经过分割以后将分割的字符串放到list集合中，返回值是list类型
    print(sp)
    print(type(sp))
    print(sp[2])
    # 第二个表示分割此次数，当次数为负数时，不会报错（分割次数会根据所给的条件进行最大次所分割）
    sp = stri.split("q",2)
    print(sp)
    print("============capitalize方法============")
    # 字符串的首字母大写
    cap = stri.capitalize()
    print(cap)
    # 整个字符串大写
    cap1 = stri.upper()
    print(cap1)
    # 每个单词开头大写
    cap2 = stri.title()
    print(cap2)
    print("============startswith方法============")
    # 判断开头是否是指定字符
    mbool = stri.startswith("a")
    print(mbool)
    print("============endswith方法============")
    mbool = stri.endswith("u")
    print(bool)
    print("============ljust方法============")
    mast = "10"
    nstr = mast.ljust(5,"-")
    print(nstr)
    print("=============rjust方法================")
    news = mast.rjust(5,"-")
    print(news)
