# a = {'aa':1}
# b = {'bb':2}
# print(a.update({'bb':2}))
# print(a)
a = """
攻速-reload，500分，+15%攻速
移速-speed，500分，+10%移速
回血-regen，800分，5分钟前生产的单位获得1/s的回血，5分钟后生产的获得2/s
赏金-bounty，500分，击杀对面单位获得造价1/4的资源
雷达-scan，300分，每30秒给你扫雷达
星空加速-chrono，500分，建筑获得10%星空加速
反甲-counter，500分，受到平A反弹15%伤害，技能和溅射反弹5%
挨打隐身-cloak，300分，被打了隐身1.5秒，2分钟cd
爱司令（仅t）-icelin，1500分，感谢爱司令在上一届比赛中的解说，拥有此buff的t玩家导弹车锁定后发射寡妇雷,红眼科技不增加伤害，可以锁定建筑造成伤害但不会对周围建筑造成溅射伤害。
奇想大帝-canaan，300分，对面对兵下指令的时候有10%概率乱跑。
卡拉ok-karaoke，800分，每分钟随机播放歌曲，对手会出现一个选择题界面，如果选错了歌名那么所有单位不受控制并跳舞4秒
""".split('\n')
arr = []
for i in range(1, len(a) - 1):
    new_arr = a[i].split('，')
    # print(new_arr)
    arr.append(new_arr)
print(arr)
arr = sorted(arr, key=lambda x: int(x[1][:-1]))
print(arr)
for i in arr:
    print('\t\t\t'.join(i))
