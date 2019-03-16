def checkEmail():
    emails = input("输入Email")
    if emails.find("@")>-1:
        strs = emails.split("@")
        if len(strs[0])>=6:
            print("邮箱合法")
        else:
            print("邮箱格式不合法")
    else:
        print("邮箱格式不合法")

def checkEmail1():
    email = input("输入邮箱")
    if email.find("@")!=-1:
        ema = email.split("@")
        if len(ema[0])>=6:
            print("邮箱格式合理")
        else:
            print("邮箱格式不合理")
    else:
        print("邮箱格式不合理")

def checkEmail2():
    email = input("输入邮箱")
    if email.find("@")!=-1:
        ema = email.split("@")
        if len(ema[0])>=6:
            print("邮箱格式合理")
        else:
            print("邮箱格式不合理")
    else:
        print("邮箱格式不合理")

if __name__ == '__main__':
    checkEmail1()