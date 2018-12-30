d = {
    "Berlin": 200000,
    "München": 300000

}

population = d.get("Köln")
if population == None:
    population = 0


print(population)
print(d)