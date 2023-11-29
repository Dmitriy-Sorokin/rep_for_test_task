import os


def write_to_file(text):
    file_path = os.path.abspath(os.path.join(os.getcwd(), "artifacts/results.txt"))
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write(text + '\n')
