# clr_parsing_table.py

from clr_states import generate_states, goto
from augmented_grammar import augment_grammar
from cfg import generate_cfg


# -----------------------------
# Collect Productions
# -----------------------------

def get_productions(grammar):

    productions = []
    prod_map = {}

    count = 1

    for lhs in grammar:
        for prod in grammar[lhs]:

            productions.append((lhs, prod))
            prod_map[(lhs, tuple(prod))] = count

            count += 1

    return productions, prod_map


# -----------------------------
# Get Terminals
# -----------------------------

def get_terminals(grammar):

    terminals = set()

    for lhs in grammar:
        for prod in grammar[lhs]:
            for sym in prod:
                if sym not in grammar and sym != "ε":
                    terminals.add(sym)

    terminals.add("$")

    return sorted(terminals)


# -----------------------------
# Get Non-terminals
# -----------------------------

def get_non_terminals(grammar):

    return sorted(grammar.keys())


# -----------------------------
# Build Table
# -----------------------------

def build_parsing_table(states, grammar):

    terminals = get_terminals(grammar)
    non_terminals = get_non_terminals(grammar)

    productions, prod_map = get_productions(grammar)

    ACTION = {}
    GOTO = {}

    # Initialize
    for i in range(len(states)):

        ACTION[i] = {t: "" for t in terminals}
        GOTO[i] = {nt: "" for nt in non_terminals}

    # SHIFT + GOTO
    for i, state in enumerate(states):

        for symbol in terminals + non_terminals:

            new_state = goto(state, symbol, grammar)

            if new_state and new_state in states:

                j = states.index(new_state)

                if symbol in terminals:
                    ACTION[i][symbol] = f"s{j}"

                elif symbol in non_terminals:
                    GOTO[i][symbol] = j

    # 🔴 FIXED REDUCE LOGIC
    for i, state in enumerate(states):

        for lhs, rhs, dot in state:

            if dot == len(rhs):

                if lhs == "S'":

                    ACTION[i]["$"] = "acc"

                else:

                    prod_no = prod_map[(lhs, tuple(rhs))]

                    # Apply reduce to ALL terminals
                    for t in terminals:

                        if ACTION[i][t] == "":
                            ACTION[i][t] = f"r{prod_no}"

    return ACTION, GOTO, productions


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    grammar = generate_cfg()

    augmented = augment_grammar(grammar)

    states = generate_states(augmented)

    ACTION, GOTO, productions = build_parsing_table(
        states,
        augmented
    )

    print("Parsing table built.")