"""Day 09 puzzle solutions"""

import sys
import helper

def parse_input(input_data):
    """
    Returns an array of unique cities and a dictionary of the distances between them
    Each line of the input data must be in the format: City1 to City2 = 123
    """
    lines = input_data.splitlines()
    cities_arr = []
    cities_dict = {}
    distances = {}
    for line in lines:
        data = line.split()
        city1, city2, dist = data[0], data[2], int(data[4])
        distances[city1 + city2] = dist
        distances[city2 + city1] = dist
        if not cities_dict.has_key(city1):
            cities_dict[city1] = True
            cities_arr.append(city1)
        if not cities_dict.has_key(city2):
            cities_dict[city2] = True
            cities_arr.append(city2)
    return cities_arr, distances

def get_distances(cities, distances):
    """Returns the shortest and the longest runs"""
    shortest_distance = 0
    longest_distance = 0
    for run in helper.permute(cities):
        previous_city = ""
        dist = 0
        for city in run:
            if previous_city != "":
                dist += distances[previous_city + city]
            previous_city = city
        if shortest_distance == 0 or dist < shortest_distance:
            shortest_distance = dist
        if dist > longest_distance:
            longest_distance = dist
    return shortest_distance, longest_distance

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.read()

CITIES, DISTANCES = parse_input(INPUT)
SHORTEST_DIST, LONGEST_DIST = get_distances(CITIES, DISTANCES)

print "Day09 --- Part One --- result is: {0}".format(SHORTEST_DIST)
print "Day09 --- Part Two --- result is: {0}".format(LONGEST_DIST)
