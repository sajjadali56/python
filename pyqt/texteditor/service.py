def read(filename) -> str:
    with open(filename, "r") as file:
        text = file.read()
    return text

def write(filename, text): 
    with open(filename, "w")  as file:
        file.write(text)