# 导包
import json


def read_json(filename):
    filepath = "../" + filename
    # 调用 load方法
    with open(filepath, "r", encoding="utf-8")as f:
        return json.load(f)

if __name__ == '__main__':
    datas = read_json("calculation.json")
    print(datas)
    print("---" * 50)
    # 新建空列表
    arrs = []
    for data in datas.values():
        arrs.append((data['a'], data['b'], data["f"], data['expect']))
    print(arrs)