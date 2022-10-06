from copy import copy
import pandas as pd
from ast import literal_eval
from Uproperty import *

csv = pd.read_csv('scPdata.csv', )
# print(csv)
csv_dict = csv.to_dict(orient='list')
name_list = copy(csv_dict['name'])

temp_arr = []
for i in range(len(name_list)):
    sc_dict_temp = {}
    for k in csv_dict:
        sc_dict_temp[k] = csv_dict[k][i]
        if k in ('atk', 'upgrade_atk', 'type_label'):
            sc_dict_temp[k] = literal_eval(csv_dict[k][i])
    temp_arr.append(sc_dict_temp)
for i in temp_arr:
    print(i)

# 用literal_eval 转里面的字符串为字典
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ...

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
