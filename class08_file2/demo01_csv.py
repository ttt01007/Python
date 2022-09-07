import csv
# csv读数据，按照行读
file = open('1.csv', 'r+', encoding='utf-8')
file_csv = csv.reader(file)
for i in file_csv:
    print(i)
file.close()
# csv读数据，带标签行读成 字典
f = open('1.csv', 'a+', encoding='utf-8')
reader = csv.DictReader(f)
print(f.tell())
f.seek(0)
for row in reader:
    print(row)
#     print(row['name'])
# 写入数据
row4 = ['feifei', '22', 'man']
csv_writer = csv.writer(f)
csv_writer.writerow(row4)
f.close()
