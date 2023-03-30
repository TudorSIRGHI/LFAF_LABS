class Lexer:
    def init(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

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