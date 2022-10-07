from Uproperty import sc_P, sc_T, sc_Z, sc_A
from math import ceil


def func_SC(type_object_A: sc_A, type_object_B: sc_A) -> int:
    """计算A打B需要的次数,A进攻,B防守"""
    atk_A, flag = sc_MatchTag(type_object_A.atk, type_object_B.type_label)  # A对B的攻击力
    num = 0
    if atk_A != 0 and flag == 0:
        if type(type_object_B) == sc_T:
            atk_A = max(atk_A - type_object_B.hp_defense, 0.5)
            num = ceil(type_object_B.hp / atk_A)
        elif type(type_object_B) == sc_Z:
            atk_A = max(atk_A - type_object_B.hp_defense, 0.5)
            num = ceil(type_object_B.hp / atk_A)
            if type_object_B.hp % atk_A == 0 and num != 1:
                """整除且没有一击必杀时"""
                num += 1
        elif type(type_object_B) == sc_P:
            type_object_B: sc_P
            atk_A_shield = max(atk_A - type_object_B.shield_defense, 0.5)  # 攻击-盾防后的伤害
            num_shield = ceil(type_object_B.shield / atk_A_shield)  # 打盾需要的次数(向上取整)
            middle = atk_A_shield - type_object_B.shield % atk_A_shield  # 溢出的攻击力
            b_hp = type_object_B.hp  # 剩下的hp
            if type_object_B.shield % atk_A_shield != 0:
                b_hp = type_object_B.hp - max(middle - type_object_B.hp_defense, 0.5)  # 通过溢出攻击力-血防 计算剩下hp
            num_hp = ceil(b_hp / max(atk_A - type_object_B.hp_defense, 0.5))  # 向上取整对剩下hp的攻击次数
            num += num_hp + num_shield
    elif atk_A != 0 and flag == 1:
        """当攻击类型为对护盾加成的技能伤害时"""
        if type(type_object_B) == sc_T:
            num += ceil(type_object_B.hp / atk_A)
        elif type(type_object_B) == sc_Z:
            num += ceil(type_object_B.hp / atk_A)
            if type_object_B.hp % atk_A == 0 and num != 1:
                num += 1
        elif type(type_object_B) == sc_P:
            """有护盾先算护盾加成, 护盾打完了溢出护盾伤害不算,直接算基础伤害"""
            type_object_B: sc_P
            atk_A_shield = type_object_A.atk['shield']
            b_shield = type_object_B.shield
            b_hp = type_object_B.hp
            num_shield = int(b_shield / (atk_A + atk_A_shield))
            middle_shield = b_shield - ((atk_A + atk_A_shield) * num_shield)
            if middle_shield > atk_A_shield:
                b_hp -= atk_A - (middle_shield - atk_A_shield)
                b_hp = max(b_hp, 0)
                num += 1
                num_hp = ceil(b_hp / atk_A)
            else:
                num_hp = ceil(b_hp / atk_A)
            num += num_shield + num_hp

    return num


def sc_MatchTag(a: dict, b: list):
    """从B的第一个字符串匹配到a上"""
    if 'shield' not in a.keys():
        c = a['']
        for string in b:
            try:
                c = a[string]
                break
            except KeyError as e:
                pass
        return c, 0
    else:
        """当他是对护盾伤害时,(默认为技能)"""
        return a[''], 1


if __name__ == '__main__':
    p = sc_P(sc_dict={
        'shield': 350,
        'shield_defense': 2,
        'name': '使徒',
        'hp': 10,
        'atk': {'': 10, '重甲': 22},
        'hp_defense': 2,
        'type_label': ['重甲', '机械单位']
    })
    p2 = sc_P(sc_dict={
        'shield': 50,
        'shield_defense': 2,
        'name': '探鸡',
        'hp': 100,
        'atk': {'': 10, '重甲': 22 + 3 * 2},
        'hp_defense': 0,
        'type_label': ['重甲', '机械单位']
    })
    t = sc_T(sc_dict={
        'name': "寡妇雷",
        'hp': 45,
        'atk': {'': 125, 'shield': 35},
        'hp_defense': 0,
        'type_label': ['轻甲', '生物单位']
    })
    print(p, p.__dict__)
    print(p.shield)
    print(func_SC(t, p2))
