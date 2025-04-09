import re

keywords = {'int', 'return', 'if', 'else', 'while', 'for', 'void', 'char', 'float', 'double'}
operators = {'+', '-', '*', '/', '=', '>', '<', '>=', '<=', '==', '!='}
separators = {'{', '}', '(', ')', ';', ',', '[', ']'}
tokens = []


def remove_comments(code):
    print("\n=== Step 1: Removing Comments ===")
    print(f"We have {len(tokens)} tokens so far")

    # Remove single line comments
    code = re.sub(r'//.*\n', '\n', code)
    # Remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code


def tokenize(code):
    print("\n=== Step 2: Tokenizing ===")
    print(f"We have {len(keywords)} keywords available")

    code = remove_comments(code)
    lines = code.split('\n')

    for line_num, line in enumerate(lines, 1):
        if not line.strip():
            continue

        pattern = r'("[^"]*")|\b\w+\b|[{}\[\]();,]|[+\-*/<>=!]=?|>'
        lexemes = re.finditer(pattern, line)

        for lexeme in lexemes:
            token = lexeme.group()

            if token in keywords:
                tokens.append((token, "keyword"))
            elif token in operators:
                tokens.append((token, "operator"))
            elif token in separators:
                tokens.append((token, "separator"))
            elif token.startswith('"') and token.endswith('"'):
                tokens.append((token, "string"))
            elif token.isdigit():
                tokens.append((token, "integer"))
            elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
                tokens.append((token, "identifier"))

            print(f"Found {token} = {tokens[-1][1]}")


def analyze(filename):
    try:
        print(f"\n=== Starting Analysis of {filename} ===")
        with open(filename, 'r') as file:
            code = file.read()
        tokenize(code)

        print(f"\n=== Final Analysis: {len(tokens)} tokens found ===")
        for token, token_type in tokens:
            print(f'"{token}" = {token_type}')

    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    print("=== Lexical Analyzer Starting ===")
    print(f"Loaded with:")
    print(f"- {len(keywords)} keywords")
    print(f"- {len(operators)} operators")
    print(f"- {len(separators)} separators")
    analyze("input.txt")
