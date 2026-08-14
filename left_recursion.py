# left_recursion.py

from cfg import generate_cfg


def check_left_recursion(grammar):

    print("\n===== CHECKING LEFT RECURSION =====\n")

    left_recursive = False

    for lhs in grammar:

        for production in grammar[lhs]:

            # Skip epsilon
            if production[0] == "ε":
                continue

            # Check A → A α
            if production[0] == lhs:

                left_recursive = True

                print(
                    f"Left recursion found in rule: "
                    f"{lhs} -> {' '.join(production)}"
                )

    if not left_recursive:
        print("No Left Recursion Found.")


def print_grammar(grammar):

    print("\n===== GRAMMAR AFTER LEFT RECURSION CHECK =====\n")

    for lhs in grammar:
        print(lhs, "->", grammar[lhs])


if __name__ == "__main__":

    grammar = generate_cfg()

    check_left_recursion(grammar)

    print_grammar(grammar)