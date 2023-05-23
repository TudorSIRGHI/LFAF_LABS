# Parser & Building an Abstract Syntax Tree

## Course: Formal Languages & Finite Automata  
## Author: Sirghi Tudor




## Theory


In the context of creating formal languages, a parser is a fundamental component that plays a crucial role in analyzing and processing the syntax of a given language. It takes input in the form of a sequence of symbols and determines whether that sequence conforms to the grammar rules of the language.
## Objectives

1. Get familiar with parsing, what it is and how it can be programmed [^1].
2. Get familiar with the concept of AST [^2].
3. In addition to what has been done in the 3rd lab work, do the following:
    1. In case you didn't have a type that denotes the possible types of tokens, you need to:
        1. Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
        2. Please use regular expressions to identify the type of the token.
    2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3. Implement a simple parser program that could extract the syntactic information from the input text.


## Implementation description

### Parser Class

This constructor method sets up the initial state of the class by assigning the token generator, initializing the list for tokens, and setting the current index to 0.
```python
    def __init__(self, token_generator):
        self.token_generator = token_generator
        self.tokens_list = []
        self.current_index = 0
```

### Parsing
The `process_statement` method checks the category of the current token. If it is a variable declaration ('VAR'), it processes the variable declaration statement. Otherwise, it raises a ValueError with an appropriate error message for unexpected tokens.

### Processing the variable names and values

Both methods follow a similar pattern. They retrieve the current token, perform a check based on the token's category, consume the token if it matches the expected category, and return the processed result. If the token's category does not match the expected value, they raise a `ValueError` with an appropriate error message indicating the unexpected token.


### Processing a token sequence that represents a value expression
The method essentially processes the token sequence representing a value expression and constructs an appropriate AST node for the value expression based on its type (numeric literal, identifier, or binary expression).

### Interpreter 
The Interpreter class provides a way to interpret and evaluate the AST generated from the parsed code. It supports variable declaration, numeric literals, identifier references, and basic binary expressions.


# Conclusion
In general, parsers are fundamental components in the field of computational linguistics and language theory. They are crucial for analyzing and processing the syntax of formal languages, including programming languages, markup languages, natural languages, and more.

The main purpose of a parser is to take a sequence of symbols as input and determine whether it conforms to the grammar rules of the language. By analyzing the structure and syntax of the input, parsers enable various applications such as compilers, interpreters, syntax checkers, code editors, natural language processing systems, and more.

Parsers can be categorized into two broad types: top-down and bottom-up parsers. Top-down parsers start from the input's beginning and recursively apply production rules to match the grammar. Bottom-up parsers, on the other hand, start from the input's end and work their way up to the start symbol, using shifting and reducing operations to construct parse trees.

There are different parsing techniques and algorithms available, each with its advantages and trade-offs. Some commonly used techniques include LL parsing, LR parsing, LALR parsing, recursive descent parsing, CYK parsing, and PEG parsing. The choice of a specific parsing technique depends on factors such as the complexity of the language's grammar, the efficiency requirements, and the presence of ambiguities or left recursion.

Parsers are not limited to formal languages used in computing. They are also utilized in natural language processing tasks, such as syntactic analysis, part-of-speech tagging, named entity recognition, and dependency parsing. Parsers enable the extraction of meaning and structure from natural language texts, facilitating tasks like information retrieval, machine translation, sentiment analysis, and question-answering systems.

In summary, parsers are essential tools for analyzing the syntax of formal languages and natural languages. They enable the validation, interpretation, and transformation of input sequences, powering a wide range of applications in computing and linguistic analysis.
