import random
if __name__ == '__main__':
    arr =[1,2,3,4,5]
    # 打乱顺序
    # 导包random
    random.shuffle(arr)

    print(arr)
    # 升序排列，永久性排序
    arr.sort()

    print(arr)
    # 将序排列
    arr.sort(reverse=True)

    print(arr)
    # 原列表的顺序不变，它是以返回值的形式临时排序
    arr1 = sorted(arr)

    print()

    print(arr1)
    # 将列表排列翻转，永久性翻转
    arr.reverse()
    print(arr)
