# left_factoring.py

from cfg import generate_cfg


def left_factoring(grammar):

    print("\n===== CHECKING LEFT FACTORING =====\n")

    new_grammar = {}

    for lhs in grammar:

        productions = grammar[lhs]

        prefix_map = {}

        # Group productions by first symbol
        for prod in productions:

            first_symbol = prod[0]

            if first_symbol not in prefix_map:
                prefix_map[first_symbol] = []

            prefix_map[first_symbol].append(prod)

        # Check if factoring needed
        factored = False

        for prefix in prefix_map:

            prods = prefix_map[prefix]

            if len(prods) > 1:

                factored = True

                new_non_terminal = lhs + "_F"

                print(
                    f"Left factoring required for {lhs}"
                )

                # Add new factored rule
                new_grammar[lhs] = [
                    [prefix, new_non_terminal]
                ]

                new_grammar[new_non_terminal] = []

                for p in prods:

                    if len(p) > 1:
                        new_grammar[new_non_terminal].append(p[1:])
                    else:
                        new_grammar[new_non_terminal].append(["ε"])

        if not factored:
            new_grammar[lhs] = productions

    return new_grammar


def print_grammar(grammar):

    print("\n===== GRAMMAR AFTER LEFT FACTORING =====\n")

    for lhs in grammar:
        print(lhs, "->", grammar[lhs])


if __name__ == "__main__":

    grammar = generate_cfg()

    factored_grammar = left_factoring(grammar)

    print_grammar(factored_grammar)