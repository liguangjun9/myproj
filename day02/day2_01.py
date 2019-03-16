if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in arr1:
        for j in arr2:
            print(str(j) + "*" + str(i) + "=" + str(i * j).rjust(2," "), end=" ")
            print(" ", end="")
            if i == j:
                print("")
                break
    i = 0
    coun = 0
    while i<=119:
        coun+=1
        print(str(i).rjust(3," "),end="  ")
        if coun%10==0:
            print()
        i+=1