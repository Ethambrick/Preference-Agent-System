def parse_attributes(file):
    attributes = []
    with open(file) as f:
        for line in f:
            name, values = line.strip().split(":")
            v1, v2 = values.strip().split(",")
            attributes.append((name.strip(), v1.strip(), v2.strip()))
    return attributes


def parse_constraints(file):
    with open(file) as f:
        return [line.strip() for line in f]


def parse_penalty(file):
    rules = []
    with open(file) as f:
        for line in f:
            formula, val = line.strip().split(",")
            rules.append((formula.strip(), int(val)))
    return rules


def parse_qualitative(file):
    return [line.strip() for line in open(file)]