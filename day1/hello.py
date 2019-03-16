if __name__ == '__main__':
    array = [[1,2,3,4,5,2,3],[1,2,3]]
    arr = [65,11,33,13]
    for i in array :
        print(i)
        for j in i :
            print(j)
    print("         ")
    arr.sort()
    print(arr)

    A = "name"
    B = "age"
    C = "sex"
    # 行位不换行，以“-”连接两个参数
    print(A,B,C,sep="-",end="")

    arr1 = [1,2,3,4,5,6,7,8,9]
    arr2 = [1,2,3,4,5,6,7,8,9]
    for i in arr1:
        for j in arr2:
            print(str(j)+"*"+str(i)+"="+str(i*j),end="")
            print(" ",end="")
            if i==j:
                print("")

    k = 5
    m = 1
    i = 1
    j = 1
    while k>=1:
        k -= 1
        m = 1
        while m < k:
            m += 1
            print("=", end="")

        while i <= k:
            i = i + 1
            j = 1
            while j < i:
                j += 1
                print("*", end="")
                if i == j:
                    print("")

    i=1
    while i<=5:
        j=0
        #控制上半个三角每行空格数量
        while j<5-i:
            #控制输出=
            print(" ",end="")
            j+=1
        j=0
        while j<2*i-1:
            print("*",end="")
            j+=1
        i+=1
        print()
    i = 5 - 1
    while i>=1:
        j=5-i
        while j>0:
            print(" ",end ="")
            j-=1
        j=2*i-1
        while j>0:
            print("*",end="")
            j-=1
        print()
        i-=1

    length = int(input("请输入:"))
    i = 1
    while i<=length:
        j = 1
        while j<=length-i:
            print(" ",end="")
            j+=1
        j = 1
        while j <=2*i-1:
            print("*",end="")
            j+=1
        print()
        i+=1
    i = length - 1
    while i>0:
        j =1
        while j <=length-i:
            print(" ",end="")
            j+=1
        j = 0
        while j < 2*i - 1:
            print("*",end="")
            j+=1
        print()
        i-=1
    # 提示用户数如一个值菱形的行数为2*行-1
    h=int(input("行数"))
    i=1
    while i<=h:
        j=1
        while j<=h-i:
            print("=",end="")
            j+=1
        j=1
        while j <=2*i-1:
            print("*",end="")
            j+=1
        print()
        i+=1
    i=h-1
    while i>0:
        j = 1
        while j<=h-i:
            print("=",end="")
            j+=1
        j=1
        while j<=2*i-1:
            print("*",end="")
            j+=1
        print()
        i-=1

