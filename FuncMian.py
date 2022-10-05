from Uproperty import sc_P, sc_T, sc_Z

p = sc_P(sc_dict={
    'shield': 12,
    'shield_defense': 13,
    'name': "'aa'",
    'hp': 31,
    'atk': 10,
    'hp_defense': 9,
    'type_label': ['bb', 'cc']
         })

z = sc_Z(sc_dict=
         {
            'name': "'aa'",
            'hp': 31,
            'atk': 10,
            'hp_defense': 9,
            'type_label': ['bb', 'cc']
         })
print(z.__dict__,z.name)
