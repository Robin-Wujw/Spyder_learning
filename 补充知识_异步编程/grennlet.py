from greenlet import greenlet

def func1():
    print(1)    #1: 输出1 
    gr2.switch()#3: 切换到func2
    print(2)    #6: 输出2
    gr2.switch()#7: 切换到func2,从上次执行的位置继续向后执行

def func2():
    print(3)    #4: 输出3
    gr1.switch()#5: 切换到func1，从上次执行的位置继续向后执行
    print(4)    #8: 输出4

gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch() #1: 去执行func1