# augmented_grammar.py

from cfg import generate_cfg


def augment_grammar(grammar):

    print("\n===== AUGMENTED GRAMMAR =====\n")

    start_symbol = list(grammar.keys())[0]

    augmented_start = start_symbol + "'"

    augmented_grammar = {}

    # Add new start rule
    augmented_grammar[augmented_start] = [[start_symbol]]

    # Copy old grammar
    for nt in grammar:
        augmented_grammar[nt] = grammar[nt]

    # Print grammar
    for lhs in augmented_grammar:
        print(lhs, "->", augmented_grammar[lhs])

    return augmented_grammar


if __name__ == "__main__":

    grammar = generate_cfg()

    augment_grammar(grammar)