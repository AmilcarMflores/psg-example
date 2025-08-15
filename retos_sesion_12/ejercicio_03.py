autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

#autos_en_comun = autos_jhon.intersection(autos_jess)
autos_en_comun = autos_jhon & autos_jess

print(f"Tienen {len(autos_en_comun)} autos en común: {autos_en_comun}")
