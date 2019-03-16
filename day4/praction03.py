    # 自定义一个异常
    # 给自定义异常类是ValueError的子类
    # 注意类中没有任何有效代码，仅有一个站位用的
class MyException(ValueError):
    pass
try:
    print("before raise excepion")
    # 手动抛出异常
    # 注意抛出的是自定义异常
    raise Exception
    print("after raise exception")
    
# 捕获自定义异常
except MyException as me:
    print("catch MyException")

#捕获自定义异常的父类
except ValueError as ve :
    print("cath ValueError")

# 捕获所有异常的父亲
except Exception as e:
    print("exception")
    print(e)
if __name__ == '__main__':
    pass
