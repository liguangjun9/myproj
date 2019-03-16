if __name__ == '__main__':
    mlsit = list()
    for i in range(1,11):
        mlsit.append(i*i)
    print(mlsit)
    # 列表生成式
    # 最简单的列表生成式
    mlist1 = [i*i for i in range(1,11)]
    # 复合列表生成式
    mlist1 = [i**2 for i in range(1,11)]
    print("mlist1 = {mlist1}".format(mlist1 = mlist1))

    mlsit = list()
    for i in range(1,11):
        if i % 2 == 0:
            mlsit.append(i)
    print(mlsit)

    mlist = [i for i in range(1,11) if i % 2 == 0]
    print("mlist = {mlist}".format(mlist = mlist))

    mlist = [1,2,3]
    nlist = ["a","b","c"]
    qlist = []
    for m in mlist:
        for n in nlist:
            qlist.append(str(m)+n)
    print("qlist = {qlist}".format(qlist = qlist))

    qlist = [str(m)+n  for m in mlist  for n in nlist]
    print("qlist  = {qlist}".format(qlist = qlist))

    qlist = [str(m) + n for m in mlist \
                if m % 2 !=0 \
             for n in nlist]
    print("qlist  = {qlist}".format(qlist=qlist))