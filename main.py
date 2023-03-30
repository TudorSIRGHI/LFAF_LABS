import Lexer

text = "12 + 3 * 4 - 5 / 2"
lexer = Lexer(text)
for token in lexer.tokenize():
    print(token)