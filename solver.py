def eval_literal(lit, obj, attributes):
    neg = False
    if lit.startswith("NOT"):
        neg = True
        lit = lit[4:]

    for i, attr in enumerate(attributes):
        if lit.strip() in attr:
            val = obj[i] == 1 if lit == attr[1] else obj[i] == 0
            return not val if neg else val

    return False


def eval_clause(clause, obj, attributes):
    parts = clause.split("OR")
    return any(eval_literal(p.strip(), obj, attributes) for p in parts)


def is_feasible(obj, constraints, attributes):
    return all(eval_clause(c, obj, attributes) for c in constraints)


def filter_feasible(objects, constraints, attributes):
    return [o for o in objects if is_feasible(o, constraints, attributes)]