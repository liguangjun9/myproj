# 创建一个类
# 这个类是继承自Exception(所有异常的父类)
# 这个类扩展了一个show方法

class MyExcept(Exception):
    pass
    # 有一个参数self
    def show(self):
        print("hehe")

# 定义一个函数，如果参数是0，则手动抛出异常
def mfun(v):
    if v == 0:
        raise Exception("good")

if __name__ == '__main__':
    # 捕获异常，并打印异常信息
    try:
        mfun(0)
    except Exception as e :
        print("excetp->{0}".format(e))
        pass
    # 查看异常处理后时否影响后续程序的运行
    print("good")

    # 将可能发生异常的代码放到这段代码快中
    try:
        #打开一个不存在的文件
        #使用只读方式打开
        #注意这行代码会发生异常
        #如果不是用异常处理，程序就会终止
        f = open("good.text","r")
        f.close()
    #此处捕获异常使用了所有异常的父类Exception
    # 一般来说应该先处理子异常然后在处理父异常
    except Exception as e :
        print(e)
    # 如果try语句块没有异常发生，则会执行完try中代码执行else中的代码
    else:
        print("Excetion else")
    # 当处理完异常后就执行这段代码区间的程序
    # 无论是否发生异常，都会执行这段代码区间的程序
    finally:
        print("finally")

    # 创建一个只执行除法运算的简单的计算器
    while True:

        print("\t")

        fnum = input("First number")
        if fnum == "q":
            break

        snum =input("Second number")
        if snum =="q":
            break

        # 捕获异常，如果发生则进入异常分支代码块
        try:
            res = int(fnum)/int(snum)
        # 异常分支代码块
        # 在代码块中处理异常
        except ZeroDivisionError as e:

            print("division error")
        #如果没有发生异常，则实行这段代码
        else:

            print("resulr = {0}".format(res))
        finally:
            print("在这里处理一些收尾的工作，如果没有")

    # 创建一个对象
    me = MyExcept()
    # 调用对象方法
    me.show()
    # 捕获异常
    try:
        raise Exception
    except Exception :
        print("hehe")
        me.show()

    try:
        mstr = "hehe"
        mstr +=1
        print(mstr)

    except Exception :
        pass

    # 异常_除数为0
    try:
        # 两个错误同时出现只会捕获一个异常
        print(5-"s")
        print(5/0)

    # 捕获一个对应的异常，，并给该异常取别名“e”
    except ZeroDivisionError as e:
        print("division by zero")
        pass
        print("e = {eKey}".format(eKey=e))
    except Exception:
        print("Exception")
    # 如果打印下面的程序运行，说明上面的异常没有影响下面的程序

    print("程序正常运行")
    ''''
    异常名称	描述
    BaseException	所有异常的基类
    SystemExit	解释器请求退出
    KeyboardInterrupt	用户中断执行(通常是输入^C)
    Exception	常规错误的基类
    StopIteration	迭代器没有更多的值
    GeneratorExit	生成器(generator)发生异常来通知退出
    StandardError	所有的内建标准异常的基类
    ArithmeticError	所有数值计算错误的基类
    FloatingPointError	浮点计算错误
    OverflowError	数值运算超出最大限制
    ZeroDivisionError	除(或取模)零 (所有数据类型)
    AssertionError	断言语句失败
    AttributeError	对象没有这个属性
    EOFError	没有内建输入,到达EOF 标记
    EnvironmentError	操作系统错误的基类
    IOError	输入/输出操作失败
    OSError	操作系统错误
    WindowsError	系统调用失败
    ImportError	导入模块/对象失败
    LookupError	无效数据查询的基类
    IndexError	序列中没有此索引(index)
    KeyError	映射中没有这个键
    MemoryError	内存溢出错误(对于Python 解释器不是致命的)
    NameError	未声明/初始化对象 (没有属性)
    UnboundLocalError	访问未初始化的本地变量
    ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
    RuntimeError	一般的运行时错误
    NotImplementedError	尚未实现的方法
    SyntaxError	Python 语法错误
    IndentationError	缩进错误
    TabError	Tab 和空格混用
    SystemError	一般的解释器系统错误
    TypeError	对类型无效的操作
    ValueError	传入无效的参数
    UnicodeError	Unicode 相关的错误
    UnicodeDecodeError	Unicode 解码时的错误
    UnicodeEncodeError	Unicode 编码时错误
    UnicodeTranslateError	Unicode 转换时错误
    Warning	警告的基类
    DeprecationWarning	关于被弃用的特征的警告
    FutureWarning	关于构造将来语义会有改变的警告
    OverflowWarning	旧的关于自动提升为长整型(long)的警告
    PendingDeprecationWarning	关于特性将会被废弃的警告
    RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
    SyntaxWarning	可疑的语法的警告
    UserWarning	用户代码生成的警告
    
    '''