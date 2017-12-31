"""Day 13 puzzle solutions"""

import helper

def parse_input(input_data, include_myself):
    """
    Returns an array of unique people and a dictionary of the happiness between them
    Each line of the input data must be in the format:
    Alice would gain 54 happiness units by sitting next to Bob.
    """
    lines = input_data.splitlines()
    people_arr = []
    people_dict = {}
    happiness_dict = {}
    for line in lines:
        data = line.split()
        person1, person2, happiness = data[0], data[10][:-1], int(data[3])
        if data[2] == "gain":
            happiness_dict[person1 + person2] = happiness
        else:
            happiness_dict[person1 + person2] = happiness * -1
        if not people_dict.has_key(person1):
            people_dict[person1] = True
            people_arr.append(person1)
    if include_myself is True:
        for person in people_arr:
            happiness_dict['me' + person] = 0
            happiness_dict[person + 'me'] = 0
        people_arr.append("me")
    return people_arr, happiness_dict

def get_best_seating_arrangement(people, happiness):
    """Returns the shortest and the longest runs"""
    max_happiness = 0
    for seating_arrangement in helper.permute(people):
        previous_person = ""
        current_happiness = 0
        count = 0
        for person in seating_arrangement:
            if previous_person != "":
                current_happiness += happiness[previous_person + person]
                current_happiness += happiness[person + previous_person]
            previous_person = person
            count += 1
            if count == len(seating_arrangement):
                current_happiness += happiness[seating_arrangement[0] + person]
                current_happiness += happiness[person + seating_arrangement[0]]
        if current_happiness > max_happiness:
            max_happiness = current_happiness
    return max_happiness
