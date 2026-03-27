from itertools import product

def generate_objects(attributes):
    return list(product([0, 1], repeat=len(attributes)))


def decode_object(obj, attributes):
    values = []
    for i, bit in enumerate(obj):
        attr = attributes[i]
        values.append(attr[1] if bit == 1 else attr[2])
    return ", ".join(values)