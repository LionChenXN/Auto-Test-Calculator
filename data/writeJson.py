import random
import time
import json


# 随机产生测试数据，写入json文件
def rand_data_write(n):
    path = '../data/calculation{}.json'.format(time.strftime("%Y_%m_%d_%H_%M_%S"))
    dic = {}

    for i in range(1, n + 1):

        isflage = random.randint(0, 3)
        sub_dic = {}
        sub_dic['a'] = random.randint(0, 1000)
        sub_dic['b'] = random.randint(0, 1000)

        if isflage == 0:
            sub_dic['f'] = "+"
            sub_dic["expect"] = int(sub_dic['a'] + sub_dic['b'])
        elif isflage == 1:
            sub_dic['f'] = "-"
            sub_dic["expect"] = int(sub_dic['a'] - sub_dic['b'])
        elif isflage == 2:
            sub_dic['f'] = "*"
            sub_dic["expect"] = int(sub_dic['a'] * sub_dic['b'])
        else:
            sub_dic['f'] = "/"
            sub_dic["expect"] = sub_dic['a'] / sub_dic['b']

        i = "%03d" % i
        number = "calc_{}".format(i)

        dic[number] = sub_dic

    with open(path, "w", encoding="utf-8") as f:
        json.dump(dic, f, ensure_ascii=False)

    return path

if __name__ == '__main__':
    n = 10
    rand_data_write(n)
