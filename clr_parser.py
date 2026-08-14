# clr_parser.py

from tokenizer import tokenize
from clr_parsing_table import build_parsing_table
from clr_states import generate_states
from augmented_grammar import augment_grammar
from cfg import generate_cfg


def clr_parse(tokens, ACTION, GOTO, productions):

    print("\n===== CLR STRING PARSING =====\n")

    stack = [0]
    index = 0

    print("{:<30}{:<45}{:<10}".format(
        "STACK",
        "INPUT",
        "ACTION"
    ))

    print("-" * 95)

    while True:

        state = stack[-1]
        symbol = tokens[index]

        action = ACTION[state].get(symbol, "")

        print("{:<30}{:<45}{:<10}".format(
            str(stack),
            str(tokens[index:]),
            action
        ))

        # ACCEPT
        if action == "acc":

            print("\n✅ STRING ACCEPTED\n")
            return

        # SHIFT
        elif action.startswith("s"):

            next_state = int(action[1:])

            stack.append(symbol)
            stack.append(next_state)

            index += 1

        # REDUCE (LOOP FIX)
        elif action.startswith("r"):

            while action.startswith("r"):

                prod_no = int(action[1:]) - 1

                lhs, rhs = productions[prod_no]

                # epsilon safe
                if rhs != ["ε"]:

                    for _ in range(2 * len(rhs)):
                        stack.pop()

                state = stack[-1]

                stack.append(lhs)

                goto_state = GOTO[state][lhs]

                stack.append(goto_state)

                state = stack[-1]

                symbol = tokens[index]

                action = ACTION[state].get(symbol, "")

        else:

            print("\n❌ STRING REJECTED\n")
            return


# -------------------------
# MAIN
# -------------------------

if __name__ == "__main__":

    grammar = generate_cfg()

    augmented = augment_grammar(grammar)

    states = generate_states(augmented)

    ACTION, GOTO, productions = build_parsing_table(
        states,
        augmented
    )

    code = """
    int main()
    begin
        int n, re = 0, rem;
        while(expr)
        begin
            expr = expr + expr;
        end
    end
    """

    tokens = tokenize(code)

    clr_parse(tokens, ACTION, GOTO, productions)