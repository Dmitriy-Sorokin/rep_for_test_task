def write_to_file(text):
    with open("results.text", 'a', encoding="utf-8") as file:
        file.write(text + '\n')
