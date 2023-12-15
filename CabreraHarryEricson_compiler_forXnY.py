import tokenize
from io import BytesIO

# function for lexical analysis
def lexical_analysis(expression):
    tokens = []
    # tokenize the expression using the importedtokenize module
    for tok in tokenize.tokenize(BytesIO(expression.encode('utf-8')).readline):
        # appending each token as a tuple to the tokens list
        tokens.append((tokenize.tok_name[tok.type], tok.string))
    return tokens

# function for parser analysis
def parser_analysis(tokens):
    # initialize an abstract syntax tree
    ast = {'operator': None, 'left': None, 'right': None}
    current_node = ast

    for token_type, token_value in tokens:
        if token_type == 'NAME':
            # in variable assignment, left side of the AST node is set
            current_node['left'] = token_value
        elif token_type == 'OP':
            if token_value == '=':
                # in assignment operator, the operator and create a new ast node on the right is set
                current_node['operator'] = token_value
                current_node['right'] = {'operator': None, 'left': None, 'right': None}
                current_node = current_node['right']
            elif token_value in {'+', '-', '*', '/'}:
                # in arithmetic operators, the operator and create a new ast node on the right is set
                current_node['operator'] = token_value
                current_node['right'] = {'operator': None, 'left': None, 'right': None}
                current_node = current_node['right']
        elif token_type == 'NUMBER':
            # for numeric values, ast is set a floatt
            current_node['left'] = float(token_value)

    return ast

# function to recursively evaluate the ast
def evaluate_ast(ast):
    if isinstance(ast, dict):
        # checks if the node is a dictionary
        if ast.get('operator') is None:
            # if it's a leaf node, return the left side
            return ast.get('left')
        elif ast['operator'] == '=':
            # if it's an assignment, evaluate the right side and store the result in variables dictionary
            variables[ast['left']] = evaluate_ast(ast['right'])
        elif ast['operator'] in {'+', '-', '*', '/'}:
            # recursively evaluate left and right sides
            left_result = evaluate_ast(ast['left'])
            right_result = evaluate_ast(ast['right'])
            
            # this performs the arithmetic operation
            if ast['operator'] == '+':
                return left_result + right_result
            elif ast['operator'] == '-':
                return left_result - right_result
            elif ast['operator'] == '*':
                return left_result * right_result
            elif ast['operator'] == '/':
                return left_result / right_result
    else:
        # if the node is not a dictionary, return the value
        return ast


expression_a = "x = 4 / 5 * 8"
expression_b = "y = 2.0 + 5 * 2"

tokens_a = lexical_analysis(expression_a)
tokens_b = lexical_analysis(expression_b)

print("Lexical Analysis Result for expression_a:")
print(tokens_a)
print("\nLexical Analysis Result for expression_b:")
print(tokens_b)

ast_a = parser_analysis(tokens_a)
ast_b = parser_analysis(tokens_b)

print("\nParser Analysis Result (Abstract Syntax Tree) for expression_a:")
print(ast_a)
print("\nParser Analysis Result (Abstract Syntax Tree) for expression_b:")
print(ast_b)

# vriables dictionary to store evaluated values
variables = {}

evaluate_ast(ast_a)
evaluate_ast(ast_b)

print("\nVariable Values:")
print(variables)
