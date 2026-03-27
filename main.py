from src.parser import *
from src.model import *
from src.solver import *
from src.penalty import *
from src.qualitative import *
import random

def main():
    print("Welcome to PrefAgent!")

    attr_file = input("Enter Attributes File Name: ")
    attributes = parse_attributes(attr_file)

    cons_file = input("Enter Hard Constraints File Name: ")
    constraints = parse_constraints(cons_file)

    while True:
        print("\nChoose the preference logic to use:")
        print("1. Penalty Logic")
        print("2. Qualitative Choice Logic")
        print("3. Exit")

        choice = input("Your Choice: ")

        if choice == "1":
            print("You picked Penalty Logic")
            pref_file = input("Enter Preferences File Name: ")
            rules = parse_penalty(pref_file)

            run_tasks(attributes, constraints, rules, logic="penalty")

        elif choice == "2":
            print("You picked Qualitative Choice Logic")
            pref_file = input("Enter Preferences File Name: ")
            rules = parse_qualitative(pref_file)

            run_tasks(attributes, constraints, rules, logic="qualitative")

        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Wrong Choice!")

def run_tasks(attributes, constraints, rules, logic):
    objects = generate_objects(attributes)
    feasible = [(i, o) for i, o in enumerate(objects)
                if is_feasible(o, constraints, attributes)]

    while True:
        print("\nChoose the reasoning task to perform:")
        print("1. Encoding")
        print("2. Feasibility Checking")
        print("3. Show the Table")
        print("4. Exemplification")
        print("5. Omni-optimization")
        print("6. Back to previous menu")

        choice = input("Your Choice: ")

        if choice == "1":
            for i, obj in enumerate(objects):
                print(f"o{i} – {decode_object(obj, attributes)}")

        elif choice == "2":
            print(f"Yes, there are {len(feasible)} feasible objects.")

        elif choice == "3":
            if logic == "penalty":
                show_penalty_table(feasible, rules, attributes)
            else:
                show_qualitative_table(feasible, rules, attributes)

        elif choice == "4":
            (i1, o1), (i2, o2) = random.sample(feasible, 2)

            print(f"Two randomly selected feasible objects are o{i1} and o{i2},")

            if logic == "penalty":
                from src.penalty import compute_penalty

                p1 = compute_penalty(o1, rules, attributes)[1]
                p2 = compute_penalty(o2, rules, attributes)[1]

                if p1 < p2:
                    print(f"and o{i1} is strictly preferred over o{i2}.")
                elif p2 < p1:
                    print(f"and o{i2} is strictly preferred over o{i1}.")
                else:
                    print(f"and o{i1} and o{i2} are equivalent.")

            else:
                from src.qualitative import dominates

                if dominates(o1, o2, rules, attributes) and not dominates(o2, o1, rules, attributes):
                    print(f"and o{i1} is strictly preferred over o{i2}.")
                elif dominates(o2, o1, rules, attributes) and not dominates(o1, o2, rules, attributes):
                    print(f"and o{i2} is strictly preferred over o{i1}.")
                elif not dominates(o1, o2, rules, attributes) and not dominates(o2, o1, rules, attributes):
                    print(f"and o{i1} and o{i2} are incomparable.")
                else:
                    print(f"and o{i1} and o{i2} are equivalent.")

        elif choice == "5":
            if logic == "penalty":
                find_optimal_penalty(feasible, rules, attributes)
            else:
                find_optimal_qualitative(feasible, rules, attributes)

        elif choice == "6":
            break
        else:
            print("Wrong Choice!")

if __name__ == "__main__":
    main()