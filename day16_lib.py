"""Day 16 puzzle solutions"""

def find_aunt(ticker_tape, aunts, use_ranges):
    """
    find aunt returns the aunt who matches the ticker_tape
    """
    aunts = aunts.splitlines()
    for aunt_line in aunts:
        aunt_id, aunt = parse_aunt_line(aunt_line)
        if not use_ranges and matches(ticker_tape, aunt):
            return aunt_id
        if use_ranges and matches_with_ranges(ticker_tape, aunt):
            return aunt_id
    return -1

def matches(ticker_tape, aunt):
    """
    matches returns true if the aunt's attributes match the ones in the ticker_tape
    """
    for attribute, value in aunt.items():
        if ticker_tape[attribute] != value:
            return False
    return True

def matches_with_ranges(ticker_tape, aunt):
    """
    matches returns true if the aunt's attributes match the ones in the ticker_tape
    """
    for attribute, value in aunt.items():
        if attribute in ['cats', 'trees']:
            if value <= ticker_tape[attribute]:
                return False
        elif attribute in ['pomeranians', 'goldfish']:
            if value >= ticker_tape[attribute]:
                return False
        else:
            if value != ticker_tape[attribute]:
                return False
    return True

def parse_aunt_line(aunt_line):
    """
    parse_aunt_line parses a string and return the aunt id and its attributes
    """
    aunt_id = int(aunt_line[4:aunt_line.find(':')])
    attributes = aunt_line[aunt_line.find(':')+1:].split(',')
    aunt = {}
    for attribute in attributes:
        name = attribute[:attribute.find(':')].strip()
        value = int(attribute[attribute.find(':')+1:].strip())
        aunt[name] = value
        # print(f'Name: {name} {value}')
    return aunt_id, aunt
