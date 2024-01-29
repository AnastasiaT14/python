ages = {
    "anna" : 19,
    "dato" : 15,
    "lika" : 24
}
min_value = min(ages.values())
min_keys = [key for key in ages if ages[key]==min_value]
print(min_keys)
