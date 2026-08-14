# Reverse a String Using CLR Parser

## 📌 Overview

This project is a **Compiler Design Mini Project** that demonstrates the implementation of a simplified compiler using **Python**.

The project focuses on lexical analysis, syntax analysis, and **Canonical LR(1) (CLR(1)) parsing** to validate an input string according to a defined grammar. Once the input is successfully validated, the program reverses the string.

The project demonstrates important compiler design concepts including **tokenization, Context-Free Grammar (CFG), FIRST and FOLLOW sets, CLR(1) states, GOTO transitions, and CLR parsing tables**.

## 🎯 Objectives

* To understand the fundamental phases of compiler design.
* To implement lexical analysis using Python.
* To define and process a Context-Free Grammar.
* To calculate FIRST and FOLLOW sets.
* To construct Canonical LR(1) (CLR(1)) states.
* To generate GOTO transitions.
* To construct ACTION and GOTO parsing tables.
* To validate an input string using CLR parsing.
* To reverse the input string after successful validation.

## 🔄 Project Workflow

```text
Input String
     ↓
Lexical Analysis
     ↓
Token Generation
     ↓
Context-Free Grammar
     ↓
FIRST & FOLLOW
     ↓
CLR(1) State Generation
     ↓
GOTO Transitions
     ↓
CLR Parsing Table
     ↓
String Validation
     ↓
Reverse the String
     ↓
Output
```

## 🛠️ Technologies Used

* **Python 3.x**
* Regular Expressions (`re`)
* PrettyTable
* PLY
* Context-Free Grammar
* Canonical LR(1) / CLR(1) Parsing

The project report specifies Python 3.x and lists `re`, PrettyTable, and PLY among the software requirements.

## 📂 Project Structure

```text
Compiler-Design-Reverse-a-String-
│
├── augmented_grammar.py       # Creates the augmented grammar
├── cfg.py                     # Defines the Context-Free Grammar
├── clr_parser.py              # Performs CLR parsing
├── clr_parsing_table.py       # Generates ACTION and GOTO tables
├── clr_states.py              # Generates CLR(1) states
├── first_follow.py            # Calculates FIRST and FOLLOW sets
├── left_factoring.py          # Performs left factoring
├── left_recursion.py          # Removes left recursion
├── tokenizer.py               # Performs lexical analysis/tokenization
├── input.txt                  # Input file
└── README.md                  # Project documentation
```

## 🔍 Main Components

### 1. Lexical Analysis

The lexical analyzer reads the input and converts meaningful character sequences into tokens such as keywords, identifiers, operators, constants, and special symbols.

It removes unnecessary elements and passes the generated tokens to the syntax analyzer.

### 2. Context-Free Grammar

The `cfg.py` file defines the grammar used by the parser. The grammar specifies the valid structure of the input program.

### 3. FIRST Set

The `first_follow.py` file calculates the **FIRST sets** of the grammar symbols. FIRST sets are used during CLR(1) item and lookahead computation.

### 4. FOLLOW Set

The same module calculates the **FOLLOW sets**, which are required for determining valid lookaheads during parsing.

### 5. CLR(1) States

The `clr_states.py` file generates the collection of **Canonical LR(1) states** using closure and GOTO operations.

### 6. GOTO Transitions

The parser determines transitions between CLR states for terminals and non-terminals. These transitions are used while constructing the parsing table.

### 7. CLR Parsing Table

The `clr_parsing_table.py` file generates the **ACTION** and **GOTO** tables.

The ACTION table performs operations such as:

* Shift
* Reduce
* Accept

The GOTO table determines the next state for non-terminal symbols.

### 8. String Validation

The parser processes the token sequence using the generated CLR parsing table. If the input follows the defined grammar, it is accepted; otherwise, it is rejected.

### 9. String Reversal

After successful validation, the input string is reversed and the reversed result is displayed.

## 📋 Requirements

### Hardware

* Modern multi-core processor
* Minimum 8 GB RAM
* Sufficient storage for Python and project files

### Software

* Windows, macOS, or Linux
* Python 3.x
* Visual Studio Code / PyCharm / any Python IDE
* Command Prompt or Terminal

## 📦 Installation

Make sure Python is installed:

```bash
python --version
```

Install the required libraries:

```bash
pip install regex
pip install prettytable
pip install ply
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/SunidhiGirish/Compiler-Design-Reverse-a-String-.git
```

### 2. Navigate to the project directory

```bash
cd Compiler-Design-Reverse-a-String-
```

### 3. Run the CLR parser

```bash
python clr_parser.py
```

### 4. Provide the input

The project uses `input.txt` for file-based input where applicable. Modify the file with the required input before execution.

## 📊 Output

The project generates and displays intermediate compiler outputs such as:

* Tokens
* Grammar
* FIRST table
* FOLLOW table
* CLR(1) states
* GOTO transitions
* CLR parsing table
* String validation/parsing trace
* Reversed string

The report's Results section documents token generation, grammar, FIRST/FOLLOW tables, GOTO transitions, the CLR parsing table, and string validation.

## 🧠 Compiler Design Concepts Demonstrated

This project demonstrates:

* Lexical Analysis
* Tokenization
* Context-Free Grammar
* Left Recursion Removal
* Left Factoring
* FIRST Set
* FOLLOW Set
* LR(1) Items
* Canonical LR(1) / CLR(1) Parsing
* Closure Operation
* GOTO Operation
* ACTION Table
* GOTO Table
* Shift Operation
* Reduce Operation
* Accept Operation
* Syntax Validation
* String Reversal

## 🚧 Limitations

This is a **simplified compiler implementation** intended for educational purposes.

It does not implement all phases of a complete production compiler, such as:

* Semantic analysis
* Intermediate code generation
* Code optimization
* Advanced error recovery
* Complete language support

The report also identifies these as limitations and suggests extending the compiler with additional language features and improved error handling.

## 🚀 Future Enhancements

Possible improvements include:

* Support for more complex grammars
* Enhanced syntax error reporting
* Better error recovery
* Semantic analysis
* Intermediate code generation
* Code optimization
* Support for additional language constructs
* Improved user interaction

## 👩‍💻 Team

**Sheethal K Shetty**
**Sindhushree Shetty**
**Sunidhi Girish**

**Department of Computer Science and Engineering**
**NMAM Institute of Technology, Nitte**

**Course:** Compiler Design Lab
**Course Code:** CS3602-1
**Semester:** VI Semester – Section D

## 📚 References

1. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. *Compilers: Principles, Techniques, and Tools*, 2nd Edition.
2. Cooper, K., & Torczon, L. *Engineering a Compiler*, 2nd Edition.
3. Javatpoint – Compiler Tutorial
4. W3Schools – Python Regular Expressions
5. PLY Documentation
6. PrettyTable Documentation
