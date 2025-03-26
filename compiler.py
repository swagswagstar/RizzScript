from translations import translations
import os


def syntax(code):
    for brainrot_word, python_word in translations.items():
        code = code.replace(brainrot_word, python_word)

    lines = code.splitlines()
    for i in range(len(lines)):
        if lines[i].strip().startswith("print("):
            if lines[i].count("(") > lines[i].count(")"):
                lines[i] += ")"
        elif lines[i].strip().startswith("input("):
            if lines[i].count("(") > lines[i].count(")"):
                lines[i] += ")"

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
    except FileNotFoundError as e:
        print("Error:", str(e))
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
