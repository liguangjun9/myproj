# 导入随机数生成用到的包
import random

if __name__ == '__main__':
    # 随机从给定范围去一个整数
    val = random.randint(1,10)
    print(val)

    #从给定序列中选择一个数
    random.choice(range(3))
    print("val = {val}".format(val = val))

    # 数据源
    mstr="abcdefghijklmn"
    # 临时存储变量
    tstr=""
    # 循环3次，相当于控制循环次数，从数据源中取出3个字符
    for i in range(3):
        # 每次随机从数据源中取出1个字符
        v=random.choice(mstr)
        # 追加到临时变量中
        tstr+=v
    # 输出数据源中随机取出的字符所拼成的新的字符串
    print(tstr)

    # 从0到9随机产生一个整数
    rval = random.randrange(0,10,1)

    print("rval = {rval}".format(rval=rval))
    #打乱书序前
    mstrs=["hehe","hoho","heihei"]
    print("befor{0}".format(mstrs))
    print(mstrs)

    # 对数据源打乱顺序操作
    random.shuffle(mstrs)
    print("after{0}".format(mstrs))
    print(mstrs)

    i = random.randint9(1,10)
    print(type(i))
