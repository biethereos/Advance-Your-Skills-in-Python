countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
population = [17_500_000, 198_000_000, 10_000_000,
              30_000_000, 24_000_000, 128_000_000]

print(max(population))

print(min(countries))

print(min(zip(countries, population)))


def get_population(pair):
    country, population = pair
    return population

print(min(zip(countries, population), key=get_population))

print(min(zip(countries, population), key=lambda x: x[1]))

print(min(zip(population, countries)))