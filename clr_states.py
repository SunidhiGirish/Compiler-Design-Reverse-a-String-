# clr_states.py

from augmented_grammar import augment_grammar
from cfg import generate_cfg

EPSILON = "ε"


def closure(items, grammar):

    closure_set = list(items)

    changed = True

    while changed:

        changed = False

        new_items = []

        for lhs, rhs, dot in closure_set:

            # If dot before symbol
            if dot < len(rhs):

                symbol = rhs[dot]

                # If non-terminal
                if symbol in grammar:

                    for production in grammar[symbol]:

                        item = (
                            symbol,
                            tuple(production),
                            0
                        )

                        if item not in closure_set:
                            new_items.append(item)

        if new_items:

            closure_set.extend(new_items)
            changed = True

    return closure_set


def goto(items, symbol, grammar):

    goto_set = []

    for lhs, rhs, dot in items:

        if dot < len(rhs) and rhs[dot] == symbol:

            goto_set.append(
                (lhs, rhs, dot + 1)
            )

    return closure(goto_set, grammar)


def generate_states(grammar):

    print("\n===== CLR STATES =====\n")

    start_symbol = list(grammar.keys())[0]

    first_item = (
        start_symbol,
        tuple(grammar[start_symbol][0]),
        0
    )

    states = []

    I0 = closure([first_item], grammar)

    states.append(I0)

    symbols = set()

    for lhs in grammar:
        symbols.add(lhs)

        for prod in grammar[lhs]:
            for sym in prod:
                if sym != EPSILON:
                    symbols.add(sym)

    i = 0

    while i < len(states):

        state = states[i]

        for symbol in symbols:

            new_state = goto(
                state,
                symbol,
                grammar
            )

            if new_state and new_state not in states:
                states.append(new_state)

        i += 1

    # Print states
    for i, state in enumerate(states):

        print(f"I{i}:")

        for lhs, rhs, dot in state:

            rhs = list(rhs)

            rhs.insert(dot, ".")

            print(
                f"{lhs} -> {' '.join(rhs)}"
            )

        print()

    return states


if __name__ == "__main__":

    grammar = generate_cfg()

    augmented = augment_grammar(grammar)

    generate_states(augmented)