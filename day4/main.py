import day4.quest1.p1 as a
import day4.quest1.p2 as b
import day4.quest1.p3 as c
import day4.quest1.p4 as d
if __name__ == '__main__':
    mdict = {
        1:"输入用户姓名及性别，然后给出下列的提示",
        2:"随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4:"从键盘输入一行字符串，判断是否是回文数"
    }
    mfunction = {
        1:a.checkSex,
        2:b.sumSet,
        3:c.checkEmail,
        4:d.numberCheck
    }

    while True:
        for i in mdict.items():
            print(i)
        sel = input("请选择服务:")
        if int(sel) == 1:
            mfunction[int(sel)]()
        elif int(sel) == 2:
            mfunction[int(sel)]()
        elif int(sel) == 3:
            mfunction[int(sel)]()
        elif int(sel) == 4:
            mfunction[int(sel)]()
        print()