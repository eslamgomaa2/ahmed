
class TokenType:
    Identifier = "Identifier"
    Number = "Number"
    Operator = "Operator"
    SpecialCharacter = "SpecialCharacter"
    Keyword = "Keyword"

class Token:
    def __init__(self, type, char):
        self.type = type
        self.char = char



class Lexer:
    current_position = 0
    operators = ['+', '-', '*', '/', '=']
    special_characters = ['(', ')', '{', '}', ',', ';']
    keywords = ['if', 'else', 'while', 'int', 'float']
    def __init__(self, source_code):
        self.source_code = source_code


    def analyze(self):
        tokens = []

        while self.current_position < len(self.source_code):
            current_char = self.source_code[self.current_position]

            if current_char.isspace():
                self.current_position += 1
            elif current_char.isalpha():
                identifier = self.read_while(lambda char: char.isalnum())
                type_ = TokenType.Keyword if identifier in self.keywords else TokenType.Identifier
                tokens.append(Token(type_, identifier))
            elif current_char.isdigit():
                tokens.append(Token(TokenType.Number, self.read_while(lambda char: char.isdigit())))
            elif current_char in self.operators:
                tokens.append(Token(TokenType.Operator, current_char))
                self.current_position += 1
            elif current_char in self.special_characters:
                tokens.append(Token(TokenType.SpecialCharacter, current_char))
                self.current_position += 1
            else:
                print(f"Error: Unknown character '{current_char}' at position {self.current_position}")
                self.current_position += 1

        return tokens

    def read_while(self, condition):
        start = self.current_position
        while self.current_position < len(self.source_code) and condition(self.source_code[self.current_position]):
            self.current_position += 1
        return self.source_code[start:self.current_position]


if __name__ == "__main__":
    source_code = "x+y+z=10"
    lexer = Lexer(source_code)
    tokens = lexer.analyze()

    for token in tokens:
        print(token)






