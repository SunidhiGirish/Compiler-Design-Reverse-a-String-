# tokenizer.py

import re


# Token patterns
token_specification = [

    ("DATATYPE", r"\bint\b"),
    ("MAIN", r"\bmain\b"),
    ("WHILE", r"\bwhile\b"),
    ("BEGIN", r"\bbegin\b"),
    ("END", r"\bend\b"),

    ("LPAR", r"\("),
    ("RPAR", r"\)"),

    ("COMMA", r","),
    ("SEMI", r";"),

    ("PLUS", r"\+"),
    ("EQ", r"="),

    ("NUMBER", r"\b\d+\b"),

    ("VAR", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),

    ("SKIP", r"[ \t\n]+"),

    ("MISMATCH", r".")
]


# Combine regex
tok_regex = "|".join(
    f"(?P<{name}>{pattern})"
    for name, pattern in token_specification
)


def tokenize(code):

    tokens = []

    for match in re.finditer(tok_regex, code):

        kind = match.lastgroup
        value = match.group()

        if kind == "SKIP":
            continue

        elif kind == "MISMATCH":
            raise RuntimeError(
                f"Unexpected character: {value}"
            )

        else:
            tokens.append(kind)

    tokens.append("$")

    return tokens


if __name__ == "__main__":

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

    print("\n===== TOKENS =====\n")

    print(tokens)