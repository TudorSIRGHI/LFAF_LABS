# Topic: Lexer
## Course: Formal Languages & Finite Automata
### Author: Sîrghi Tudor, FAF-213
## Theory 
<p>
The process of converting a string of characters that represents source code in a programming language into a collection of useful tokens or lexemes is known as lexical analysis. The code can then be executed using these tokens once they have undergone additional processing such as parsing and interpretation.

A software called a lexer, also known as a tokenizer, does lexical analysis and produces a list of tokens based on pre-established rules or patterns. The lexer creates a token for each of the various language components, including keywords, identifiers, operators, and literals. The parser is then given access to these tokens to continue processing them.

Building a lexer is a crucial component of developing a compiler, interpreter, or any other tool that needs to examine and work with source code for programming languages.

A lexer is created by first specifying the various tokens, then the patterns that match those tokens, and finally by putting the lexer into use to produce those tokens. Object-oriented programming techniques can be used to create the system, for as by developing a Lexer class that specifies the methods for identifying and producing tokens. It is also possible to implement the lexer using functional programming methods.

Overall, building a lexer is a crucial component of developing a language processing tool, and Python offers a variety of tools and packages that make the process reasonably simple.

</p>

### How does the Lexer work?
The lexer generates tokens, which are then forwarded to the parser to be processed further. After examining the program's structure using the programming language's grammar, the parser generates a parse tree that represents the program's structure.

## Objectives:
1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation description
This Python code describes a class called Lexer that has an init method. The text input is used by the init method to initialize the object's state. The "text" attribute is changed to the input text, while the "pos" attribute is changed to 0. The first character of the input text at index 0 is used as the value for the 'current char' attribute. The input text is divided into smaller parts called tokens in order to perform lexical analysis using this class and its methods.

    
  class Lexer:
    def init(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
The following code shows several functions for tokenizing input text that is defined as part of the implementation of the Lexer class. An invalid character will cause an exception to be raised via the "error" method. When the input text reaches the end, the "advance" method updates the location of the current character and changes it to None.

Any white space characters are skipped by the 'skip whitespace' function. The "integer" method determines whether a value is an integer and returns it. The "tokenize" procedure, which comes last, creates tokens based on the recognized character patterns. Using the methods mentioned above, it detects various operators and numbers and then returns a generator object that generates tokens one at a time.

The 'error' method is called when an unrecognized character is found, which throws an exception. The basic functionality of a Lexer object, which may tokenize input text into a series of meaningful tokens, is generally implemented in this code.
 
def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                yield self.integer()
            elif self.current_char == '+':
                self.advance()
                yield '+'
            elif self.current_char == '-':
                self.advance()
                yield '-'
            elif self.current_char == '*':
                self.advance()
                yield '*'
            elif self.current_char == '/':
                self.advance()
                yield '/'
            else:
                self.error()

The 'Lexer' module is imported, an input text string is defined, and an object called 'lexer' is created. Then, it prints each token individually by iterating through the tokens produced by the "tokenize" method of the "lexer" object. The "main" class primarily serves as an example of how to tokenize an input string and output its tokens using the "Lexer" module.
```
import Lexer
text = "12 + 3 * 4 - 5 / 2"
lexer = Lexer
for token in lexer.tokenize():
    print(token)
```

## Conclusion
Finally, lexical analysis, which comprises breaking down the source code into smaller tokens and classifying them, is an essential part of programming language processing. Lexical analysis is performed by a software called a lexer or tokenizer, which generates a list of tokens that can be utilized in further processing.

By creating a lexer in Python, developers may quickly do lexical analysis on their code and get a list of tokens that can be used for further processing such as parsing, interpretation, and execution of the code. Overall, designing tools and programs that employ programming languages can be made much simpler by creating a lexer in Python.
____
