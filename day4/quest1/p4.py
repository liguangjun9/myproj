def numberCheck():
    num=input("输入回文数:")
    if len(num) % 2 != 0:
        if num == num[::-1]:
            print("是回文数")
        else:
            print("不是回文数")
    else:
        print("不是回文数")

def numCheck():
    while True:
        num = input("输入一个数字:(输入0退出)")
        print(num.isdigit())
        # 当输入的不是数字，捕获一个异常
        try:
            # print(len(num)%2 != 0 and num==num[::-1])
            # 判断全部是否是数字
            # 将其翻转并与输入的值相比是相等
            # 判断字符长度是奇数
            if len(num)%2 != 0 and num==num[::-1] and num.isdigit():
                print("是回文数")
            else:
                print("不是回文数")
            # 退出循环条件
            if int(num) == 0:
                print("fdfdsfds")
                break
        except ValueError :
            print("ValueError")

def numCheck2():
    while True:
        num = input("输入一个数字:(输入0退出)")
        print(num.isdigit())
        try:
            if len(num)%2 != 0 and num==num[::-1] and num.isdigit():
                print("是回文数")
            else:
                print("不是回文数")
            if int(num) == 0:
                print("fdfdsfds")
                break
        except ValueError :
            print("ValueError")

if __name__ == '__main__':
    numCheck()