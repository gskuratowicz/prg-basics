countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":23000000},
{"name":"Finland", "population":3320000},
{"name":"Ireland", "population":1200000},
{"name":"Estonia", "population":5320000},
]
print("COUNTRY  POPULATION")
for country in countries:
    print(f"{country['name']} {country['population']}")