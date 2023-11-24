import json

def write_to_file( text):
    with open("test_results.text", 'a', encoding="utf-8") as file:
        file.write(text + '\n')
