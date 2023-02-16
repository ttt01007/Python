from xml.dom import minidom

# 加载xml
dom = minidom.parse('1.xml')
# 文件数据
root = dom.documentElement
# 获取根节点
print(root.nodeName)
# 获取根节点行
print(root.nodeType)

# 获取标签名 一个 getElementByTagName和 多个 getElementsByTagName
name1 = root.getElementsByTagName('name')
print(name1[0].nodeName)
age1 = root.getElementsByTagName('age')
print(age1[0].nodeName)
# 获取值
print(name1[0].firstChild.data)

# 获取属性值
student = root.getElementsByTagName('student')
ID = student[0].getAttribute('ID')
print(ID)

# 获取所有学生的信息
student = root.getElementsByTagName('student')
for i in student:
    name = i.getElementsByTagName('name')
    age = i.getElementsByTagName('age')
    name_value = name[0].firstChild.data
    age_value = age[0].firstChild.data
    print(name_value)
    print(age_value)
