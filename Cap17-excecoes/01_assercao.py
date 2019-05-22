

# converter Kelvin


def kelvinToFahreinheit(Temperatura):
    assert (Temperatura >= 0), 'Colder than absolute zero'
    return ((Temperatura - 273) * 1.8) + 32

print(kelvinToFahreinheit(273))
print(kelvinToFahreinheit(505.78))
print(kelvinToFahreinheit(0))
print(kelvinToFahreinheit(-1))