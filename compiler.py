from translations import translations
import os
import sys


def syntax(code):
    for brainrot_word, python_word in translations.items():
        code = code.replace(brainrot_word, python_word)

    lines = code.splitlines()

    def balance_parentheses(line):
        stack = []
        for char in line:
            if char == "(":
                stack.append(char)
            elif char == ")" and stack:
                stack.pop()
        # Add missing closing parentheses
        return line + ")" * len(stack)

    for i in range(len(lines)):
        if lines[i].strip().startswith("print(") or lines[i].strip().startswith(
            "input("
        ):
            lines[i] = balance_parentheses(lines[i])

    return "\n".join(lines)


def validate_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    valid_extensions = [".rizz", ".rizzscript"]
    if ext.lower() not in valid_extensions:
        raise ValueError(
            f"Invalid file extension. Expected {' or '.join(valid_extensions)}, got {ext}"
        )
    return True


def main():
    file_path = input("Enter the path of your RizzScript file: ")

    try:
        # Validate file extension
        validate_file_extension(file_path)

        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read and process file
        with open(file_path, "r") as file:
            brainrot_code = file.read()
            python_code = syntax(brainrot_code)
            exec(python_code)

    except ValueError as e:
        print("Error:", str(e))
        sys.exit(1)
    except FileNotFoundError as e:
        print("Error:", str(e))
        sys.exit(1)
    except Exception as e:
        print("Error:", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
