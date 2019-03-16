if __name__ == '__main__':
    try:
        mfile = open(r"C:\Users\lenovo\PycharmProjects\myproj\day4\a.c","r")

        val = mfile.read()
        print(val)
        mlist = mfile.readlines()

        mline = mfile.readline()

        mbool = mfile.readable()

    except OSError :

        print("OSError")
    except Exception :
        print("Exception")
    else :
        mfile.close()

    mlist = ["dun","dan","u","up"]

    mfile = open(r"C:\Users\lenovo\PycharmProjects\myproj\day4\a.c", "w")

    mwr = mfile.write("zhong")

    print("mwr = {mwrKey}".format(mwrKey = mwr))
    mfile.close()