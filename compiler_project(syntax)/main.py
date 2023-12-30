

class Tokenizer:
    position = 0
    def __init__(self, input_string):
        self.input_string = input_string


    def get_next_token(self):
        while self.position < len(self.input_string):
            current_char = self.input_string[self.position]
            if current_char.isspace():
                self.position += 1

            if current_char.isdigit():
                self.position += 1
                return ("NUMBER", int(current_char))
            elif current_char in "+*-/":
                self.position += 1
                return ("OPERATOR", current_char)

            else:
                raise SyntaxError(f"Unexpected character: {current_char}")


class Parser:
    current_token = None
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer


    def parse(self):
        self.current_token = self.tokenizer.get_next_token()
        result = self.expr()
        if self.current_token[0] != "EOF":
            raise SyntaxError("Unexpected tokens after parsing.")
        return result

    def expr(self):
        term_result = self.term()
        while self.current_token[0] == "OPERATOR" and self.current_token[1] in ("+", "*"):
            operator = self.current_token[1]
            self.current_token = self.tokenizer.get_next_token()
            term_result = (operator, term_result, self.term())
        return term_result

    def term(self):
        if self.current_token[0] == "NUMBER":
            value = self.current_token[1]
            self.current_token = self.tokenizer.get_next_token()
            return value
        else:
            raise SyntaxError("Expected NUMBER.")




if __name__ == "__main__":
    input_string = "2 + 3 * 4"
    tokenizer = Tokenizer(input_string)
    parser = Parser(tokenizer)

    try:
        result = parser.parse()
        print(f"Parse result: {result}")
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
