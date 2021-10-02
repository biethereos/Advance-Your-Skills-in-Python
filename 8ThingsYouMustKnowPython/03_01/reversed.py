countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
print(countries)
countries.reverse()
print(countries)
print(countries[::-1])
for country in reversed(countries):
    print(country)

print(countries)
reversed_countries = list(reversed(countries))
print(reversed_countries)

for country in reversed(tuple(countries)):
    print(country)
