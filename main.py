from copy import copy

import numpy as np
import pandas as pd
from ast import literal_eval

from openpyxl.utils import get_column_letter

from Uproperty import *
from itertools import combinations_with_replacement, product
from FuncMian import *
from memory_profiler import profile


# @profile
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


sc_dic = {}


# @profile
def itermAll(*sc_list):
    if len(sc_list) == 1 or type(sc_list[0]) == type(sc_list[1]):
        '''内战'''
        # print(1)
        sc_list = sc_list[0]
        for sc_obj in product(sc_list, repeat=2):
            sc_obj_0: sc_A
            sc_obj_1: sc_A
            sc_obj_0, sc_obj_1 = sc_obj[0], sc_obj[1]
            OD_calculate(sc_obj_0, sc_obj_1)

    elif len(sc_list) == 2:
        '''外战'''
        # print(2)
        sc_list1, sc_list2 = sc_list[0], sc_list[1]
        for sc_obj in product(sc_list1, sc_list2):
            # print(sc_obj[0].name, sc_obj[1].name)
            OD_calculate(sc_obj[0], sc_obj[1])
    else:
        raise print('超2个参数')


def OD_calculate(sc_obj_0, sc_obj_1):
    global sc_dic
    arr1 = []
    for atk_num in range(3 + 1):
        sc_obj_g = copy(sc_obj_0)
        a = merge_dict(sc_obj_0.atk, mul_dict(sc_obj_0.upgrade_atk, atk_num))
        sc_obj_g.atk = a
        # print('-----------')
        for df_num in range(3 + 1):
            sc_obj_f = copy(sc_obj_1)
            sc_obj_f.hp_defense += sc_obj_f.upgrade_hp * df_num
            if type(sc_obj_0) == sc_P or type(sc_obj_1) == sc_P:
                """当有P时,添加护盾类型"""
                for sh_num in range(3 + 1):
                    sc_obj_s = copy(sc_obj_f)
                    sc_obj_s.shield_defense += sc_obj_s.upgrade_shield * sh_num
                    arr1.append(func_SC(sc_obj_g, sc_obj_s))
            else:
                arr1.append(func_SC(sc_obj_g, sc_obj_f))

    sc_name = sc_obj_0.name + ' ' + sc_obj_1.name
    sc_dic[sc_name] = arr1


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


def to_xlsx(f: pd.DataFrame, filePath: str):
    """对表格进行分类处理并写入Excel"""
    excel_dic1 = {}
    excel_dic2 = {}

    for column in f.columns:
        unit_str = column.split(' ')[0]
        unit_str_f = column.split(' ')[1]
        # print(unit_str)

        if unit_str not in excel_dic1:
            temp_arr1 = [column]
            # temp_arr2 = [unit_str_f]

            excel_dic1[unit_str] = None
            excel_dic2[unit_str] = {column: unit_str_f}
        else:
            temp_arr1.append(column)
            # temp_arr2.append(unit_str_f)
            excel_dic1[unit_str] = temp_arr1
            excel_dic2[unit_str][column] = unit_str_f
            # excel_dic2[colums] = temp_arr2
    # excel_path = 'output.xlsx'
    with pd.ExcelWriter(filePath) as writer:
        for i in excel_dic1:
            # print(i)
            unit_df = f[excel_dic1[i]]
            unit_df = unit_df.rename(columns=excel_dic2[i])
            # unit_df.to_excel(writer, sheet_name=i)
            to_excel_auto_column_weight(unit_df, writer, i)


def to_excel_auto_column_weight(df: pd.DataFrame, writer: pd.ExcelWriter, sheet_name):
    """DataFrame保存为excel并设置A列列宽"""
    # 数据 to 写入器，并指定sheet名称
    df.to_excel(writer, sheet_name=sheet_name)
    worksheet = writer.sheets[sheet_name]
    worksheet.column_dimensions['A'].width = 30
    for i in [chr(k) for k in range(ord("B"), ord("V")+1)]:
        worksheet.column_dimensions[i].width = 10


# 用literal_eval 转里面的字符串为字典
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    p_arr = createSc_obj('scPdata.csv')
    p = [sc_P(sc_dict=i) for i in p_arr]
    t = []
    z = []
    itermAll(p, p)
    index_arr_p = [f'攻击等级{i},防御等级{j},盾等级{k}' for i in range(4) for j in range(4) for k in range(4)]
    pdDf = pd.DataFrame(sc_dic, index=index_arr_p)

    excel_path = 'output.xlsx'
    to_xlsx(pdDf, excel_path)
    # pddf.to_csv('2.csv', encoding='gbk')
