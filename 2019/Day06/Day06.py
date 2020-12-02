from collections import defaultdict

with open('input.txt') as file:
    orbits = [orbit.split(")") for orbit in file.read().splitlines()]

print(orbits)

orbiting = defaultdict(list)
planets = []

for planet in orbits:
    orbiting[planet[0]].append(planet[1])
    planets.append(planet[0]).append([1])

planets = set(planets)

for planet in planets:
    direct_orbits = len(planets)
    indirect_orbits = len()
    for moon in planet:







