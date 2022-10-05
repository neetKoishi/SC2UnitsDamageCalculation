import pandas as pd
from ast import literal_eval
csv = pd.read_csv('scPdata.csv',)
print(csv)
csv_dict = csv.to_dict(orient='list')

# 用literal_eval 转里面的字符串为字典
print(literal_eval(csv_dict['type_label'][0]))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ...

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
