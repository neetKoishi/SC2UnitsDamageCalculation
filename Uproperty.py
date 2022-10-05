import inspect


class sc_A:

    def __init__(
            self,
            name: str,
            hp: int,
            atk: dict,
            hp_defense: int,
            type_label: list,
            sc_dict: dict,
    ) -> None:
        if sc_dict:
            # self._globals = {'self': self.__dict__}
            for k, v in sc_dict.items():
                # self._globals.update({f'{k}': f'{v}'})
                # print(self._globals)
                exec(f'self.{k}={v}')
        else:
            self.name: str = name
            self.type_label: list = type_label  # 标签
            self.hp: int = hp  # 血量
            self.atk: dict = atk  # 攻击力
            self.hp_defense: int = hp_defense  # 血防


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
            sc_dict: dict = None
    ):
        super(sc_P, self).__init__(name, hp, atk, hp_defense, type_label, sc_dict)
        if not sc_dict:
            self.shield: int = shield  # 护盾
            self.shield_defense: int = shield_defense  # 盾防


class sc_Z(sc_A):
    def __init__(
            self,
            name: str = '',
            hp: int = 0,
            atk: dict = None,
            hp_defense: int = 0,
            type_label: list = None,
            sc_dict: dict = None
    ):
        super().__init__(name, hp, atk, hp_defense, type_label, sc_dict)


class sc_T(sc_A):
    def __init__(
            self,
            name: str = '',
            hp: int = 0,
            atk: dict = 0,
            hp_defense: int = 0,
            type_label: list = None,
            sc_dict: dict = None
    ):
        super().__init__(name, hp, atk, hp_defense, type_label, sc_dict)
