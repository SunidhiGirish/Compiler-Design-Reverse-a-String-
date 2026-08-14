# Grammar stored as dictionary: Non-terminal -> list of productions
grammar = {
    'P': [['int', 'main', 'begin', 'D', 'S', 'end']],
    'D': [['int', 'IDLIST', ';']],
    'IDLIST': [['ID'], ['ID', ',', 'IDLIST'], ['ID', '=', 'NUM', ',', 'IDLIST']],
    'S': [['WHILE'], ['ASSIGN']],
    'WHILE': [['while', '(', 'E', ')', 'begin', 'S', 'end']],
    'ASSIGN': [['ID', '=', 'E', ';']],
    'E': [['E', '+', 'T'], ['T']],   # left recursion
    'T': [['T', '*', 'F'], ['F']],   # left recursion
    'F': [['ID'], ['NUM'], ['(', 'E', ')']]
}

# Print the grammar nicely
for nt, productions in grammar.items():
    print(f"{nt} -> " + " | ".join(" ".join(prod) for prod in productions))
