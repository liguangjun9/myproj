# 定义等腰三角形输出函数
def san(hi):
    # 利用for循环确定等腰三角形的
    for i in range(1,hi+1,1):
        # 利用for循环编写左边的填充三角形
        for k in range(i,hi,1):
            print(" ",end="")
        for j in range(1,2*i,1):
            print("*",end="")
        print()


def jiu():
    for i in range(1,10):
        for j in range(1,10):
            print(str(i)+"*"+str(j)+"="+str(i*j).rjust(2),end="\t")
            if i==j:
                break
        print()


def ling(h):
    for i in range(1,h+1,1):
        for j in range(h,i,-1):
            print(" ",end="")
        for k in range(1,2*i,1):
            print("*",end="")
        print()
    for i in range(1,h,1):
        for j in range(1,i+1,1):
            print(" ",end="")
        for k in range(i*2,2*h-1,1):
            print("*",end="")
        print()



def shu(num):
    coun=0
    for i in range(0,num+1):
        coun+=1
        print(str(i).rjust(3),end=" ")
        if coun%10==0:
            print()
if __name__ == '__main__':
    print(~7)
    # 等腰三角形
    hi = int(input("输入等边三角形的行数:"))
    san(hi)
    # 九九乘法表
    jiu()
    # 菱形输出
    h= int(input("输入"))
    ling(h)
    # 数字正方行输出
    num= int(input("输入一个数字"))
    shu(119)