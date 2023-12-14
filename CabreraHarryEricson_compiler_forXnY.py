import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token('EOF', None)

        current_char = self.text[self.pos]

        if re.match(r'\d', current_char):
            self.pos += 1
            return Token('NUMBER', int(current_char))

        if current_char == '+':
            self.pos += 1
            return Token('PLUS', '+')

        if current_char == '-':
            self.pos += 1
            return Token('MINUS', '-')

        if current_char == '*':
            self.pos += 1
            return Token('MULTIPLY', '*')

        if current_char == '/':
            self.pos += 1
            return Token('DIVIDE', '/')

        if current_char == '=':
            self.pos += 1
            return Token('ASSIGN', '=')

        if re.match(r'[a-zA-Z]', current_char):
            self.pos += 1
            return Token('VAR', current_char)

        self.error()

    def get_tokens(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == 'EOF':
                break
        return tokens
    

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return token.value
        elif token.type == 'VAR':
            self.eat('VAR')
            return token.value
        else:
            self.error()

    def term(self):
        result = self.factor()

        while self.current_token.type in ['MULTIPLY', 'DIVIDE']:
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                result *= self.factor()
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
                result /= self.factor()

        return result

    def expr(self):
        if self.current_token.type == 'VAR':
            var_name = self.current_token.value
            self.eat('VAR')
            self.eat('ASSIGN')
            result = self.term()
            return (var_name, result)
        else:
            self.error()

    def parse(self):
        return self.expr()


class Evaluator:
    def __init__(self, parser):
        self.parser = parser
        self.variables = {}

    def evaluate(self):
        var_name, result = self.parser.parse()
        self.variables[var_name] = result
        return self.variables

# Example usage
lexer = Lexer('x = 4 / 5 * 8')
parser = Parser(lexer)
evaluator = Evaluator(parser)
print(evaluator.evaluate())  # Output: {'x': 6.4}

lexer = Lexer('y = 2.0 + 5 * 2')
parser = Parser(lexer)
evaluator = Evaluator(parser)
print(evaluator.evaluate())  # Output: {'y': 12.0}