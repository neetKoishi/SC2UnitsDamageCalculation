from copy import copy
import pandas as pd
from ast import literal_eval
from Uproperty import *
from itertools import combinations_with_replacement, product
from FuncMian import *


def createSc_obj(file_path: str) -> list:
    csv = pd.read_csv(file_path, )
    # print(csv)
    csv_dict = csv.to_dict(orient='list')
    name_list = copy(csv_dict['name'])

    temp_arr = []
    for p in range(len(name_list)):
        sc_dict_temp = {}
        for k in csv_dict:
            sc_dict_temp[k] = csv_dict[k][p]
            if k in ('atk', 'upgrade_atk', 'type_label'):
                sc_dict_temp[k] = literal_eval(csv_dict[k][p])
        temp_arr.append(sc_dict_temp)
    return temp_arr


p_arr = createSc_obj('scPdata.csv')
# for i in p_arr:
#     print(i)
p = [sc_P(sc_dict=i) for i in p_arr]


def itermAll(*sc_list):
    if len(sc_list) == 1 or type(sc_list[0]) == type(sc_list[1]):
        '''内战'''
        # print(1)
        sc_list = sc_list[0]
        for sc_obj in product(sc_list, repeat=2):
            sc_obj_0: sc_A
            sc_obj_1: sc_A
            sc_obj_0, sc_obj_1 = sc_obj[0], sc_obj[1]
            print(sc_obj_0.name, sc_obj_1.name)
            OD_calculate(sc_obj_0, sc_obj_1)


    elif len(sc_list) == 2:
        '''外战'''
        # print(2)
        sc_list1, sc_list2 = sc_list[0], sc_list[1]
        for sc_obj in product(sc_list1, sc_list2):
            print(sc_obj[0].name, sc_obj[1].name)
            OD_calculate(sc_obj[0], sc_obj[1])
    else:
        raise print('超2个参数')


def OD_calculate(sc_obj_0, sc_obj_1):
    for atk_num in range(3 + 1):
        sc_obj_g = copy(sc_obj_0)
        a = merge_dict(sc_obj_0.atk, mul_dict(sc_obj_0.upgrade_atk, atk_num))
        sc_obj_g.atk = a
        print('-----------')
        # print(sc_obj_g.atk)
        for df in range(3 + 1):
            sc_obj_f = copy(sc_obj_1)
            sc_obj_f.hp_defense += sc_obj_f.upgrade_hp * df
            # print(sc_obj_f.hp_defense)
            print(f'攻击等级:{atk_num} 防御等级:{df} 次数:{func_SC(sc_obj_g, sc_obj_f)}')


def merge_dict(x, y) -> dict:
    """将2字典想通的key对应的值相加"""
    dic: dict = copy(x)
    for k, v in y.items():
        if k in x.keys():
            dic[k] += v
    return dic


def mul_dict(x, y) -> dict:
    dic = copy(x)

    for k, v in dic.items():
        dic[k] *= y
    return dic


itermAll(p, p)

# 用literal_eval 转里面的字符串为字典
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ...

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
