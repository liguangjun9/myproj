# from datetime import *
# if __name__ == '__main__':
#     datea = input("输如年月日")
#     year = datea[:4]
#     d1 = datetime.strptime(year+'0101','%Y%m%d')
#     d2 = datetime.strptime(datea,'%Y%m%d')
#     print((d2-d1).days+1)
# from datetime import *
# if __name__ == '__main__':
#     day=input("输入年月日")
#     day1 = datetime.strptime(day[:4]+"0101","%Y%m%d")
#     day2 = datetime.strptime(day,"%Y%m%d")
#     print((day2-day1).days+1)
# from datetime import *
# if __name__ == '__main__':
#     day = input("输入年月日")
#     day1 = datetime.strptime(day[:4]+"0101","%Y%m%d")
#     day2 = datetime.strptime(day,"%Y%m%d")
#     print((day2-day1).days+1)
#
# import time
# if __name__ == '__main__':
#     day= input("输入")
#     day1 = time.strptime(day,"%Y%m%d")
#     print(day1.tm_yday)
# import time
# if __name__ == '__main__':
#     day= input("输入")
#     day1 = time.strptime(day,"%Y%m%d")
#     print(day1.tm_yday)
# from datetime import *
# if __name__ == '__main__':
#     day = input("输入年月日")
#     day1 = datetime.strptime(day[:4]+"0101","%Y%m%d")
#     day2= datetime.strptime(day,"%Y%m%d")
#     print((day2-day1).days+1)
# import time
# if __name__ == '__main__':
#     day = input("输入年月日")
#     day1 = time.strptime(day,"%Y%m%d")
#     print(day1.tm_yday)
import random
if __name__ == '__main__':
    mlist = []
    for i in range(5):
        random.randint(10)

