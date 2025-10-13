travel_log = [
    {
        "Country": "France",
        "Visits": 12,
        "Cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "Visits": 5,
        "Cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, number, cities):
    new_entry = {}
    
    for x in range(3):
        new_entry
    
    new_entry["Country"] = country
    new_entry["Visits"] = number
    new_entry["Cities"] = cities
    travel_log.append(new_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log, sep="\n") 