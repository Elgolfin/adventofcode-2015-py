"""Day 17 puzzle solutions"""

import itertools

def parse_input(input_str):
    """
    parse_iput returns a list of integers from a list of strings
    (from a from of one integer per line)
    """
    return list(map(int, input_str.splitlines()))

def get_exact_combinations(capacity, containers):
    """
    get_exact_combinations returns how many different combinations
    of containers can exactly fit the specified capacity
    """
    iter_count = len(containers)
    count = 0
    while iter_count > 0:
        combinations = itertools.combinations(containers, iter_count)
        for combination in combinations:
            if sum(combination) == capacity:
                count = count + 1
        iter_count = iter_count - 1
    return count

def get_exact_min_combinations(capacity, containers):
    """
    get_exact_min_combinations returns how many different combinations
    of containers can exactly fit the specified capacity (with the minimum containers)
    """
    iter_count = len(containers)
    count_dict = {}
    count_min_containers = 0
    while iter_count > 0:
        count = 0
        combinations = itertools.combinations(containers, iter_count)
        for combination in combinations:
            if sum(combination) == capacity:
                count = count + 1
        count_dict[iter_count] = count
        if count != 0:
            count_min_containers = count
        iter_count = iter_count - 1
    return count_min_containers
