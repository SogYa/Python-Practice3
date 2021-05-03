def find_farthest_orbit(list_of_orbits):
    max_orbit_area = sorted([3.1412926 * semiaxis[0] * semiaxis[1] for semiaxis in list_of_orbits])[-1]
    return [x for x in list_of_orbits if 3.1412926 * x[1] * x[0] == max_orbit_area][0]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]          # В здадинии решено неправильно 10 * 2,5 < 6 * 6
print(*find_farthest_orbit(orbits))
