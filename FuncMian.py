from Uproperty import sc_P, sc_T, sc_Z, sc_A
from math import ceil


def func_SC(type_object_A: sc_A, type_object_B: sc_A) -> int:
    """计算A打B需要的次数,A进攻,B防守"""
    atk_A = sc_MatchTag(type_object_A.atk, type_object_B.type_label)  # A对B的攻击力
    num = 0
    if type(type_object_B) == sc_T:
        atk_A -= max(type_object_B.hp_defense, 0.5)
        num = ceil(type_object_B.hp / atk_A)
    elif type(type_object_B) == sc_Z:

        atk_A -= max(type_object_B.hp_defense, 0.5)
        num = ceil(type_object_B.hp / atk_A)
        if type_object_B.hp % atk_A == 0 and num != 1:
            """整除且没有一击必杀时"""
            num += 1
    elif type(type_object_B) == sc_P:
        atk_A_shield = max(atk_A - type_object_B.shield_defense, 0.5)
        num_shield = ceil(type_object_B.shield / atk_A_shield)
        middle = type_object_B.shield % atk_A_shield
        b_hp = type_object_B.hp
        if middle != 0:
            b_hp = type_object_B.hp - max(middle - type_object_B.hp_defense, 0.5)
        num_hp = ceil(b_hp / max(atk_A - type_object_B.hp_defense, 0.5))
        num = num_hp + num_shield
    return num


def sc_MatchTag(a: dict, b: list):
    """从B的第一个字符串匹配到a上"""
    c = a['']
    for string in b:
        try:
            c = a[string]
            break
        except KeyError as e:
            pass
    return c


if __name__ == '__main__':
    p = sc_P(sc_dict={
            'shield': 80,
            'shield_defense': 0,
            'name': '追猎',
            'hp': 80,
            'atk': {'': 13, '重甲': 18},
            'hp_defense': 1,
            'type_label': ['重甲', '机械单位']
                 })
    t = sc_T(sc_dict={
        'name': "陆战队员",
        'hp': 45,
        'atk': {'': 6},
        'hp_defense': 0,
        'type_label': ['轻甲', '生物单位']
    })
    print(p, p.__dict__)
    print(p.shield)
    print(func_SC(p, t))