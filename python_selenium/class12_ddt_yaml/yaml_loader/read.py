# 读取yaml中的文件内容

import yaml

if __name__ == '__main__':
    file = open('../data/data5.yaml', 'r', encoding='utf-8')
    data = yaml.load(stream=file, Loader=yaml.FullLoader)
    print(data)
