# 打开文件
import os
import shutil

file = open('1.txt', 'r+', encoding='utf-8')
# 按行读取
print(file.readline())
# 移动光标
file.seek(1, 0)
print(file.readline())
file.close()

with open('2.txt', 'r+') as file:
    print(file.readline())
# 创建文件
# os.mkdir(r'.\abc')
# 删除文件
# os.rmdir(r'.\abc')
# 删除文件树
# shutil.rmtree(r'.\abc')
# 修改文件名
# os.rename(r'.\abc', r'.\dce')
# 获取文件当前路径
print(os.getcwd())
