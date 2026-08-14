# first_follow.py

from cfg import generate_cfg

EPSILON = "ε"


def compute_first(grammar):

    first = {nt: set() for nt in grammar}

    changed = True

    while changed:
        changed = False

        for nt in grammar:

            for production in grammar[nt]:

                for symbol in production:

                    # Terminal
                    if symbol not in grammar:

                        if symbol not in first[nt]:
                            first[nt].add(symbol)
                            changed = True

                        break

                    # Non-terminal
                    else:

                        before = len(first[nt])

                        first[nt] |= (
                            first[symbol] - {EPSILON}
                        )

                        if EPSILON not in first[symbol]:
                            break

                        if before != len(first[nt]):
                            changed = True

                else:
                    if EPSILON not in first[nt]:
                        first[nt].add(EPSILON)
                        changed = True

    return first


def compute_follow(grammar, first):

    follow = {
        nt: set() for nt in grammar
    }

    start_symbol = list(grammar.keys())[0]

    follow[start_symbol].add("$")

    changed = True

    while changed:

        changed = False

        for nt in grammar:

            for production in grammar[nt]:

                for i, symbol in enumerate(production):

                    if symbol in grammar:

                        next_symbols = production[i+1:]

                        if next_symbols:

                            first_next = set()

                            for s in next_symbols:

                                if s in grammar:
                                    first_next |= (
                                        first[s] - {EPSILON}
                                    )

                                    if EPSILON not in first[s]:
                                        break

                                else:
                                    first_next.add(s)
                                    break

                            before = len(
                                follow[symbol]
                            )

                            follow[symbol] |= first_next

                            if before != len(
                                follow[symbol]
                            ):
                                changed = True

                        else:

                            before = len(
                                follow[symbol]
                            )

                            follow[symbol] |= follow[nt]

                            if before != len(
                                follow[symbol]
                            ):
                                changed = True

    return follow


def print_sets(first, follow):

    print("\n===== FIRST SETS =====\n")

    for nt in first:
        print(f"FIRST({nt}) = {first[nt]}")

    print("\n===== FOLLOW SETS =====\n")

    for nt in follow:
        print(f"FOLLOW({nt}) = {follow[nt]}")


if __name__ == "__main__":

    grammar = generate_cfg()

    first = compute_first(grammar)

    follow = compute_follow(grammar, first)

    print_sets(first, follow)