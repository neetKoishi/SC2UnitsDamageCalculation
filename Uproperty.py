class sc_A:

    def __init__(
            self,
            name: str,
            hp: int,
            atk: dict,
            hp_defense: int,
            type_label: list,
            upgrade_hp: int,
            upgrade_atk: dict,
            sc_dict: dict,
    ) -> None:
        if sc_dict:
            for k, v in sc_dict.items():
                exec(f'self._{k}={v}')
        else:
            self._name: str = name
            self._type_label: list = type_label  # 标签
            self._hp: int = hp  # 血量
            self._atk: dict = atk  # 攻击力
            self._hp_defense: int = hp_defense  # 血防
            self._upgrade_hp: int = upgrade_hp  # 防御升级
            self._upgrade_atk: dict = upgrade_atk  # 攻击升级

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def hp_defense(self):
        return self._hp_defense

    @property
    def type_label(self):
        return self._type_label


class sc_P(sc_A):
    def __init__(
            self,
            shield=0,
            shield_defense=0,
            name: str = '',
            hp: int = 0,
            atk: dict = None,
            hp_defense: int = 0,
            type_label: list = None,
            upgrade_hp: int = 0,
            upgrade_atk: dict = None,
            upgrade_shield: int = 0,
            sc_dict: dict = None,
    ):
        super(sc_P, self).__init__(name, hp, atk, hp_defense, type_label, upgrade_hp, upgrade_atk, sc_dict, )
        if not sc_dict:
            self._shield: int = shield  # 护盾
            self._shield_defense: int = shield_defense  # 盾防
            self._upgrade_shield: int = upgrade_shield  # 盾升级

    @property
    def shield(self):
        return self._shield

    @property
    def shield_defense(self):
        return self._shield_defense



class sc_Z(sc_A):
    def __init__(
            self,
            name: str = '',
            hp: int = 0,
            atk: dict = None,
            hp_defense: int = 0,
            type_label: list = None,
            upgrade_hp: int = 0,
            upgrade_atk: dict = None,
            sc_dict: dict = None,
    ):
        super().__init__(name, hp, atk, hp_defense, type_label, upgrade_hp, upgrade_atk, sc_dict)


class sc_T(sc_A):
    def __init__(
            self,
            name: str = '',
            hp: int = 0,
            atk: dict = 0,
            hp_defense: int = 0,
            type_label: list = None,
            upgrade_hp: int = 0,
            upgrade_atk: dict = None,
            sc_dict: dict = None,
    ):
        super().__init__(name, hp, atk, hp_defense, type_label, upgrade_hp, upgrade_atk, sc_dict)
