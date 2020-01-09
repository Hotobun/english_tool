from xlrd import open_workbook
import json, os, random
import sqlalchemy
import config
import db 

def write_sql():
    try:
        work = open_workbook("英语口语3000高频词.xlsx")
    except:
        print("读取xlsx文件失败")
        exit()
    data = work.sheet_by_index(0) 
    for i in range(1, data.nrows):
        id = str(int(data.cell_value(i,0)))
        sentence =  data.cell_value(i,5).replace("\n", '')
        en = ''
        zh = ''
        for index in range(len(sentence)):
            if '\u4e00' <= sentence[index] <= '\u9fff':
                en = sentence[:index]
                zh = sentence[index:]
                break
        if en == '':
            en = sentence
        new =  {
            'id': id,
            'word': data.cell_value(i,1),
            'count':int(data.cell_value(i,2)),
            'symbol' : data.cell_value(i,3),
            'translate': data.cell_value(i,4).replace("\n", ''),
            'en' : en,
            'zh' : zh,
        }
        db.insert(new)

def words(age=5):
    data = []
    for _ in range(age):
        t = db.get_rand_data()
        # for i in t[1:-2]:
        #     print("{:13s}".format(i), end = '')
        data.append(t)
    return data

def main():  
    words()

if __name__ == "__main__": 
    main()