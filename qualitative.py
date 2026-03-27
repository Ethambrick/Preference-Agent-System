from src.solver import eval_clause


def satisfies(formula, obj, attributes):
    if formula.strip() == "":
        return True
    clauses = formula.split("AND")
    return all(eval_clause(c.strip(), obj, attributes) for c in clauses)


def parse_rule(rule):
    parts = rule.split("IF")
    left = parts[0].strip()
    condition = parts[1].strip() if len(parts) > 1 else ""

    options = [x.strip() for x in left.split("BT")]
    return options, condition


def compare_objects(o1, o2, rules, attributes):
    d1 = dominates(o1, o2, rules, attributes)
    d2 = dominates(o2, o1, rules, attributes)

    print(f"Comparing {o1} and {o2}")

    if d1 and not d2:
        print("First is strictly preferred over second")
    elif d2 and not d1:
        print("Second is strictly preferred over first")
    elif not d1 and not d2:
        print("Objects are incomparable")
    else:
        print("Objects are equivalent")


def dominates(o1, o2, rules, attributes):
    strictly_better = False

    for rule in rules:
        options, condition = parse_rule(rule)

        cond1 = satisfies(condition, o1, attributes)
        cond2 = satisfies(condition, o2, attributes)

        if not cond1 and not cond2:
            continue

        rank1 = None
        rank2 = None

        if cond1:
            for i, opt in enumerate(options):
                if satisfies(opt, o1, attributes):
                    rank1 = i
                    break

        if cond2:
            for i, opt in enumerate(options):
                if satisfies(opt, o2, attributes):
                    rank2 = i
                    break

        if cond1 and not cond2 and rank1 is not None:
            strictly_better = True
            continue

        if cond2 and not cond1 and rank2 is not None:
            return False

        if rank1 is not None and rank2 is not None:
            if rank1 < rank2:
                strictly_better = True
            elif rank2 < rank1:
                return False

    return strictly_better


def find_optimal_qualitative(objects, rules, attributes):
    optimal = []

    for i, o in objects:
        dominated = False
        for j, other in objects:
            if i != j and dominates(other, o, rules, attributes):
                dominated = True
                break
        if not dominated:
            optimal.append(i)

    labels = [f"o{i}" for i in optimal]
    print("All optimal objects:", ", ".join(labels))

def show_qualitative_table(objects, rules, attributes):
    headers = ["encoding"] + rules
    col_width = 20

    def line():
        return "+" + "+".join(["-" * col_width for _ in headers]) + "+"

    print(line())
    print("|" + "|".join(f"{h[:col_width]:^{col_width}}" for h in headers) + "|")
    print(line())

    for i, obj in objects:
        row = [f"o{i}"]

        for rule in rules:
            options, condition = parse_rule(rule)

            if not satisfies(condition, obj, attributes):
                row.append("-")
                continue

            rank = "-"
            for idx, opt in enumerate(options):
                if satisfies(opt, obj, attributes):
                    rank = str(idx + 1)  # 1-based rank
                    break

            row.append(rank)

        print("|" + "|".join(f"{val:^{col_width}}" for val in row) + "|")

    print(line())