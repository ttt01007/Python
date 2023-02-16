# 读取yaml中的文件内容
# data:字典 data2:list data3:复合
import yaml

if __name__ == '__main__':
    file = open('../data/data2.yaml', 'r', encoding='utf-8')
    data = yaml.load(stream=file, Loader=yaml.FullLoader)
    print(data)
