import random
def sumSet():
    mset1 = {random.randint(0,50) for i in range(10)}
    mset2 = {random.randint(0,50) for i in range(15)}
    mset = mset1|mset2
    print(mset)

def sumSet():
    # 创建一个集合
    mseta = set()
    # 通过for循环向集合中添加数据
    for i in range(10):
        mseta.add(random.randint(0,50))
    print(mseta)
    msetb = set()
    for i in range(15):
        msetb.add(random.randint(0,50))
    print(msetb)
    # 计算两个集合的交集
    msetn = mseta|msetb
    print(msetn)

def sumSet1():
    # 创建一个集合
    mseta = set()
    # 通过for循环向集合中添加数据
    for i in range(10):
        mseta.add(random.randint(0,50))
    print(mseta)
    msetb = set()
    for i in range(15):
        msetb.add(random.randint(0,50))
    print(msetb)
    # 计算两个集合的交集
    msetn = mseta|msetb
    print(msetn)
if __name__ == '__main__':
    sumSet()