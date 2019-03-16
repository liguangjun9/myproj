import random
if __name__ == '__main__':
    name = input("输入姓名")
    print(name)
    sex = input("输入性别")
    print(sex)
    age = input("输入年龄")
    print(age)

    val = int(input("请输入一个数字:"))

    print(val**(1/2))

    val1 = int(input("请输入一个1-100间数字:"))

    val2 = random.randint(1,100)

    if val1<val2:
        print("你输了!",val2)
    elif val1==val2:
        print("平局!")
    else :
        print("你赢了!", val2)