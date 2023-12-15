## Overview

This Python script demonstrates a simple compiler for parsing and evaluating mathematical expressions. The compiler handles basic expressions with addition, subtraction, multiplication, and division operations. Two specific expressions are used as examples.

## Usage

1. **Expression Format**: The expressions should follow a basic format, such as `variable = expression`.

2. **Supported Operations**:
   - Addition (`+`)
   - Subtraction (`-`)
   - Multiplication (`*`)
   - Division (`/`)

3. **Example Expressions**:
   - `x = 4 / 5 * 8`
   - `y = 2.0 + 5 * 2`

## Code Structure

### Lexical Analysis

The `lexical_analysis` function tokenizes the input expression, converting it into a list of tokens.

### Parser Analysis

The `parser_analysis` function builds an Abstract Syntax Tree (AST) from the tokenized expression.

### AST Evaluation

The `evaluate_ast` function recursively traverses the AST to evaluate the mathematical expression. It supports variable assignment and basic arithmetic operations.

## Example Usage

<!-- ```python
# Example expressions
expression_a = "x = 4 / 5 * 8"
expression_b = "y = 2.0 + 5 * 2"

# Lexical Analysis
tokens_a = lexical_analysis(expression_a)
tokens_b = lexical_analysis(expression_b)

# Parser Analysis
ast_a = parser_analysis(tokens_a)
ast_b = parser_analysis(tokens_b)

# Initialize variables dictionary
variables = {}

# Evaluate expressions
evaluate_ast(ast_a)
evaluate_ast(ast_b)

# Print the result
print("\nVariable Values:")
print(variables) -->