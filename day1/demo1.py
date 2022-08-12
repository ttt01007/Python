mylist=['1','2','3']

def addMylist():
    addlist=input("请输入添加姓名")
    mylist.append(addlist)
    print(mylist)
def delMylist():
    dellist=input("请输入删除姓名")
    mylist.remove(dellist)
    print(mylist)
def movMylist():
    delname=input("请输入要修改得姓名")
    delindex = mylist.index(delname)
    if(delindex>=0):
        addname = input("请输入要修改为姓名")
        mylist[delindex] = addname
        print(mylist)
    else:
        print("不存在这个人")

def selMylist():
    pass

def caozuo(num):
    num=int(num)
    if num == 1:
        addMylist()
    elif num == 2:
        delMylist()
    elif num == 3:
        movMylist()
    elif num == 4:
        selMylist()
    elif num == 0:
        exit
    else:
        print("操作错误")
    DisplayMessage()

def DisplayMessage():
    print("1:add,2:delete,3:modify,4:select")
    return caozuo(input("请输入操作:"))

DisplayMessage()
