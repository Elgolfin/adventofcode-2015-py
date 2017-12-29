"""Day 02 puzzle solutions"""

DISTANCES = {
    'Faerun to Norrath': 129,
    'Faerun to Tristram': 58,
    'Faerun to AlphaCentauri': 13,
    'Faerun to Arbre': 24,
    'Faerun to Snowdin': 60,
    'Faerun to Tambi': 71,
    'Faerun to Straylight': 67,
    'Norrath to Tristram': 142,
    'Norrath to AlphaCentauri': 15,
    'Norrath to Arbre': 135,
    'Norrath to Snowdin': 75,
    'Norrath to Tambi': 82,
    'Norrath to Straylight': 54,
    'Tristram to AlphaCentauri': 118,
    'Tristram to Arbre': 122,
    'Tristram to Snowdin': 103,
    'Tristram to Tambi': 49,
    'Tristram to Straylight': 97,
    'AlphaCentauri to Arbre': 116,
    'AlphaCentauri to Snowdin': 12,
    'AlphaCentauri to Tambi': 18,
    'AlphaCentauri to Straylight': 91,
    'Arbre to Snowdin': 129,
    'Arbre to Tambi': 53,
    'Arbre to Straylight': 40,
    'Snowdin to Tambi': 15,
    'Snowdin to Straylight': 99,
    'Tambi to Straylight': 70
}
CITIES = [
    "Faerun",
    "Norrath",
    "Tristram",
    "AlphaCentauri",
    "Arbre",
    "Snowdin",
    "Tambi",
    "Straylight"
]

def permute(items, low=0):
    """Returns all permutations of a list of items"""
    if low + 1 >= len(items):
        yield items
    else:
        for perm in permute(items, low + 1):
            yield perm
        for k in range(low + 1, len(items)):
            items[low], items[k] = items[k], items[low]
            for perm in permute(items, low + 1):
                yield perm
            items[low], items[k] = items[k], items[low]

def get_distances():
    """Returns the shortest and the longest distances"""
    shortest_distance = 0
    longest_distance = 0
    for i in permute(CITIES):
        previous = ""
        dist = 0
        for j in i:
            if previous != "":
                if DISTANCES.has_key("{0} to {1}".format(previous, j)):
                    dist += DISTANCES["{0} to {1}".format(previous, j)]
                else:
                    dist += DISTANCES["{1} to {0}".format(previous, j)]
            previous = j
        if shortest_distance == 0 or dist < shortest_distance:
            shortest_distance = dist
        if dist > longest_distance:
            longest_distance = dist
    return shortest_distance, longest_distance

SHORT_DIST, LONG_DIST = get_distances()

print "Day09 --- Part One --- result is: {0}".format(SHORT_DIST)
print "Day09 --- Part Two --- result is: {0}".format(LONG_DIST)
