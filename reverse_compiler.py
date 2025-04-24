from translations import translations
import re
import os

# Create reverse translation dictionary
python_to_rizz = {v: k for k, v in translations.items()}


def reverse_syntax(code):
    # For multi-character replacements, sort by length in descending order
    # to avoid partial replacements
    sorted_translations = sorted(
        python_to_rizz.items(), key=lambda x: len(x[0]), reverse=True
    )

    lines = code.splitlines()
    converted_lines = []

    for line in lines:
        # Preserve indentation
        indent = re.match(r"^\s*", line).group()
        code_part = line.lstrip()

        # Split the line into code and string parts
        parts = re.split(r"(\'[^\']*\'|\"[^\"]*\")", code_part)

        for i in range(0, len(parts), 2):
            # Even indices are code, odd indices are strings
            if i < len(parts):
                # Handle special cases with parentheses first
                for python_word, brainrot_word in sorted_translations:
                    if python_word.endswith("("):
                        pattern = re.compile(
                            r"\b" + re.escape(python_word[:-1]) + r"\s*\("
                        )
                        parts[i] = pattern.sub(brainrot_word, parts[i])

                # Handle regular keywords
                for python_word, brainrot_word in sorted_translations:
                    if not python_word.endswith("("):
                        pattern = re.compile(r"\b" + re.escape(python_word) + r"\b")
                        parts[i] = pattern.sub(brainrot_word, parts[i])

        # Reassemble the line with preserved strings
        code_part = "".join(parts)
        # Reassemble line with preserved indentation
        converted_lines.append(indent + code_part)

    return "\n".join(converted_lines)


def validate_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() != ".py":
        raise ValueError(f"Invalid file extension. Expected .py, got {ext}")
    return True


def convert_file(py_path):
    # Validate file extension
    validate_file_extension(py_path)

    # Check if file exists
    if not os.path.exists(py_path):
        raise FileNotFoundError(f"File not found: {py_path}")

    # Read Python file
    with open(py_path, "r") as file:
        python_code = file.read()

    # Convert to RizzScript
    rizz_code = reverse_syntax(python_code)

    # Create output filename
    rizz_path = py_path.rsplit(".", 1)[0] + ".rizz"

    # Save RizzScript file
    with open(rizz_path, "w") as file:
        file.write(rizz_code)

    return rizz_path


def main():
    file_path = input("Enter the path of your Python file (without extension): ")

    # Add .py extension if not provided
    if not file_path.endswith(".py"):
        file_path += ".py"

    try:
        output_path = convert_file(file_path)
        print(f"Successfully converted to: {output_path}")
    except ValueError as e:
        print("Error:", str(e))
    except FileNotFoundError as e:
        print("Error:", str(e))
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
