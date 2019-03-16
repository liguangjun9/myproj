# 创建一个类
# 这个类是继承Exception(所有异常的父类)
# 这个类扩展了一个方法show
class MyExcept(Exception):
    pass
    def show(self):
        print("hh")
if __name__ == '__main__':
    # 创建一个对象
    me = MyExcept()
    # 调用对象方法
    me.show()
    try:
        # 手动抛出自定义异常
        raise MyExcept

    except MyExcept as e:
        print("raise MyExcept")
        # 调用了自定义异常的扩展的方法
        e.show