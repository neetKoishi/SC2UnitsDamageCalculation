### 这是一个计算StarCraft2不同单位之间在不同的攻防下共需要攻击多少次才能击杀的工具
### 使用方法:
1. `git clone `
2. 此项目依赖于 panda 库,建议用anaconda创建Python环境, Python3.8以上版本
3. 诺无conda环境,`pip install panda `
4. `data/sc(P/T/Z)data.csv `是各单位的数据 `(XvX).xlsx`是计算后得出的数据
5. 由于在最开始没想用panda处理数据,想原生库随便写写就用的csv文件,所以如果版本更新了需要变动单位数据,需要注意文件保持格式得要UTF-8不然会报错  
这点以后会转成xlsx(有生之年)