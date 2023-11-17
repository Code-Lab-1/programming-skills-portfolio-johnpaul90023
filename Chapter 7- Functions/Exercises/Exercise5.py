def describe_city(city, country='Philippines'):
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('\nManila')
describe_city('\nTokyo', 'Japan')
describe_city('\nNueva Vizcaya')
print("")
