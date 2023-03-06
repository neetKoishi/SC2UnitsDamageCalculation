# coding=utf-8
from copy import copy
import os
import pandas as pd

from Uproperty import *
from itertools import combinations_with_replacement, product
from FuncMian import *


# @profile
def createSc_obj(file_path: str) -> list:
    csv = pd.read_csv(os.getcwd() + "\\" + file_path, encoding='utf-8')
    # print(csv)
    csv_dict = csv.to_dict(orient='list')
    name_list = copy(csv_dict['name'])

    temp_arr = []
    for p in range(len(name_list)):
        sc_dict_temp = {}
        for k in csv_dict:
            sc_dict_temp[k] = csv_dict[k][p]
            if k in ('atk', 'upgrade_atk', 'type_label', 'unit_type', 'atk_type'):
                """将表格中的字符串转dict或者list"""
                sc_dict_temp[k] = literal_eval(csv_dict[k][p])
        temp_arr.append(sc_dict_temp)
    return temp_arr


# @profile
def itermAll(sc_list1, sc_list2):
    """修改sc_dict, 1进攻,2防守"""

    # print(sc_list1, sc_list2)
    flag = None
    for sc_obj in product(sc_list1, sc_list2):
        # print(sc_obj[0].name, sc_obj[1].name)
        new_flag = sc_obj[1].flag
        if flag == new_flag:
            continue
        if atk_type_bool(sc_obj[0].atk_type, sc_obj[1].unit_type):
            OD_calculate(sc_obj[0], sc_obj[1])
        flag = new_flag


def OD_calculate(sc_obj_0, sc_obj_1):
    """传入2个sc_object, 并变成可以传入DataFrame的dict"""
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
            if type(sc_obj_1) == sc_P:
                """当防守为P时,添加护盾类型"""
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


def atk_type_bool(a: list, b: list) -> bool:
    if len(a) == 0:
        return False
    else:
        for i in a:
            if i in b:
                return True
        return False


def to_xlsx(f: pd.DataFrame, filePath: str):
    """对表格进行分类处理并写入Excel"""
    excel_dic1 = {}
    excel_dic2 = {}

    for column in f.columns:
        unit_str = column.split(' ')[0]
        unit_str_f = column.split(' ')[1]
        # print(unit_str)

        if unit_str not in excel_dic1:

            # temp_arr2 = [unit_str_f]

            excel_dic1[unit_str] = [column]
            excel_dic2[unit_str] = {column: unit_str_f}
        else:
            excel_dic1[unit_str].append(column)
            # temp_arr2.append(unit_str_f)
            excel_dic2[unit_str][column] = unit_str_f
            # excel_dic2[colums] = temp_arr2
    # excel_path = 'output.xlsx'

    with pd.ExcelWriter(filePath) as writer:
        for i in excel_dic1:
            # print(i)
            unit_df = f[excel_dic1[i]]
            unit_df = unit_df.rename(columns=excel_dic2[i])
            unit_df.to_excel(writer, sheet_name=i)
            to_excel_auto_column_weight(unit_df, writer, i)

    # for i in excel_dic1:
    #     unit_df = f[excel_dic1[i]]
    #     unit_df = unit_df.rename(columns=excel_dic2[i])
    #     print(i, '==========')
    #     print(unit_df)


def to_excel_auto_column_weight(df: pd.DataFrame, writer: pd.ExcelWriter, sheet_name):
    """DataFrame保存为excel并设置A列列宽"""
    # 数据 to 写入器，并指定sheet名称
    df.to_excel(writer, sheet_name=sheet_name)
    worksheet = writer.sheets[sheet_name]
    worksheet.column_dimensions['A'].width = 30
    for i in [chr(k) for k in range(ord("B"), ord("V") + 1)]:
        worksheet.column_dimensions[i].width = 10


# 用literal_eval 转里面的字符串为字典
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    p_arr = createSc_obj('data/scPdata.csv')
    t_arr = createSc_obj('data/scTdata.csv')
    z_arr = createSc_obj('data/scZdata.csv')
    p = [sc_P(sc_dict=i) for i in p_arr]
    t = [sc_T(sc_dict=i) for i in t_arr]
    z = [sc_Z(sc_dict=i) for i in z_arr]

    # print(p, t, z)
    index_arr_p = [f'攻击等级{i},防御等级{j},盾等级{k}' for i in range(4) for j in range(4) for k in range(4)]
    index_arr_unP = [f'攻击等级{i},防御等级{j}' for i in range(4) for j in range(4)]
    for item in product([p, t, z], repeat=2):
    # for item in [(t, t)]:
        #     print(item)
        sc_dic = {}

        itermAll(item[0], item[1])
        if sc_P == type(item[1][0]):
            pdDf = pd.DataFrame(sc_dic, index=index_arr_p)
        else:
            pdDf = pd.DataFrame(sc_dic, index=index_arr_unP)
        F = lambda x: str(type(x)).split("'")[-2].split('_')[-1]
        excel_path = fr'{os.getcwd()}\data\{F(item[0][0])}v{F(item[1][0])}.xlsx'
        to_xlsx(pdDf, excel_path)
    # pddf.to_csv('2.csv', encoding='gbk')
