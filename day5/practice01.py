if __name__ == '__main__':
    # 创建一个非空元组
    # 元组一旦创建成功，其中的元素都不能被修改
    mytuple = (1,2,3,4,5)
    # 元组的索引操作
    print("mytuple[{0}]".format(mytuple[0],0))
    # 元组的遍历操作
    for t in mytuple:
        print("mytuple->",t)
    #元组的分片操作
    ntuple = mytuple[0:3:1]
    print("ntuple = ",ntuple)