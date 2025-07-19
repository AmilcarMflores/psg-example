autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

autos_en_comun = set()

if 'Ferrari' in autos_jhon and 'Ferrari' in autos_jess:
    autos_en_comun.add('Ferrari')

if 'Lamborghini' in autos_jhon and 'Lamborghini' in autos_jess:
    autos_en_comun.add('Lamborghini')

if 'Porsche' in autos_jhon and 'Porsche' in autos_jess:
    autos_en_comun.add('Porsche')

if 'Bugatti' in autos_jhon and 'Bugatti' in autos_jess:
    autos_en_comun.add('Bugatti')

if 'McLaren' in autos_jhon and 'McLaren' in autos_jess:
    autos_en_comun.add('McLaren')

if 'Tesla' in autos_jhon and 'Tesla' in autos_jess:
    autos_en_comun.add('Tesla')

if 'Ford' in autos_jhon and 'Ford' in autos_jess:
    autos_en_comun.add('Ford')

if 'Chevrolet' in autos_jhon and 'Chevrolet' in autos_jess:
    autos_en_comun.add('Chevrolet')

print(f"Tienen {len(autos_en_comun)} autos en común: {autos_en_comun}")
