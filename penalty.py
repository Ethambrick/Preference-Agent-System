from src.solver import eval_clause

def eval_formula(formula, obj, attributes):
    clauses = formula.split("AND")
    return all(eval_clause(c.strip(), obj, attributes) for c in clauses)


def compute_penalty(obj, rules, attributes):
    total = 0
    details = []
    for formula, val in rules:
        if eval_formula(formula, obj, attributes):
            details.append(0)
        else:
            details.append(val)
            total += val
    return details, total


def show_penalty_table(objects, rules, attributes):

    headers = ["encoding"] + [formula for formula, _ in rules] + ["total penalty"]

    col_widths = [max(len(h), 8) + 2 for h in headers]

    def line():
        return "+" + "+".join("-" * w for w in col_widths) + "+"

    print(line())
    print("|" + "|".join(f"{h:^{w}}" for h, w in zip(headers, col_widths)) + "|")
    print(line())

    for i, obj in objects:
        details, total = compute_penalty(obj, rules, attributes)

        row = [f"o{i}"] + [str(d) for d in details] + [str(total)]
        print("|" + "|".join(f"{val:^{w}}" for val, w in zip(row, col_widths)) + "|")

    print(line())

def compare_objects(o1, o2, rules, attributes):
    p1 = compute_penalty(o1, rules, attributes)[1]
    p2 = compute_penalty(o2, rules, attributes)[1]

    print(f"Comparing {o1} and {o2}")
    if p1 < p2:
        print("First is preferred")
    elif p2 < p1:
        print("Second is preferred")
    else:
        print("Equivalent")


def find_optimal_penalty(objects, rules, attributes):
    results = [(i, o, compute_penalty(o, rules, attributes)[1]) for i, o in objects]

    min_val = min(r[2] for r in results)

    best = [(i, o) for i, o, v in results if v == min_val]

    labels = [f"o{i}" for i, _ in best]
    print("All optimal objects:", ", ".join(labels))