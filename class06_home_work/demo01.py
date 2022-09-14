student_list = [{'id': '123', 'name': '234', 'age': '18'}]


def DisplayMessage():
    print("1:add,2:delete,3:modify,4:select,0:exit")


def addMylist():
    s_id = input("请输入添加id\n")
    if s_id is None or s_id == '':
        print('不能为空。')
        return
    name = input("请输入添加name\n")
    if name is None or name == '':
        print('不能为空。')
        return
    age = input("请输入添加age\n")
    for i in student_list:
        if i['id'] == s_id or i['name'] == name:
            print('重复')
            return
    student_dict = {'id': s_id, 'name': name, 'age': age}
    student_list.append(student_dict)
    print(student_list)


def delMylist():
    s_id = input("请输入删除id或者name\n")
    for i in student_list:
        if i['id'] == s_id or i['name'] == s_id:
            del student_list[student_list.index(i, 0, len(student_list))]
            break
    print(student_list)


def movMylist():
    s_id = input("请输入修改的id\n")
    for i in student_list:
        if i['id'] == s_id:
            i['name'] = input('name修改为')
            i['age'] = input('age修改为')
            break
    print(student_list)


def selMylist():
    s_id = input("请输入查询id或者name\n")
    for i in student_list:
        if i['id'] == s_id or i['name'] == s_id:
            print(i)
            break
    print(student_list)


while True:
    DisplayMessage()
    num = int(input('请输入操作:'))
    if num == 1:
        addMylist()
    elif num == 2:
        delMylist()
    elif num == 3:
        movMylist()
    elif num == 4:
        selMylist()
    elif num == 0:
        break
    else:
        print("操作错误")
