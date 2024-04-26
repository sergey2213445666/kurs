import os

def write_and_read(text):
    file_path = os.path.join('/tmp', 'my_file.txt')
    
    # Write text to file
    with open(file_path, "w") as file:
        file.write(text)
    
    # Read text from file
    with open(file_path, "r") as file:
        text_read = file.read()
    
    # Remove temp file
    os.remove(file_path)
    
    return text_read

text = input()
print(write_and_read(text))