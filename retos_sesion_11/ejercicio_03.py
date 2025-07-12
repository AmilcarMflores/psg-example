especies = dict((
    ('canino', '🐶'),
    ('felino', '🐱'),
    ('aves', ['🐦', '🦅'])
))
print(especies)
print(type(especies))

# Obtenemos y eliminamos 'aves':
valor_aves = especies.pop('aves')
print(valor_aves, type(valor_aves))
print(especies)

# Modificamos el valor de la clave felino por 🐈
especies.update({'felino': '🐈'})
print(especies)

# Cambiamos la clave canino por caninos y su valor por ['🐶','🐕']
especies.pop('canino')
especies.update({'caninos': ['🐶','🐕']})
print(especies)