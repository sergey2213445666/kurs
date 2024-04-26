def process_string(input_str):
    if input_str.startswith("!"):
        processed_str = input_str[1:].upper()
    else:
        processed_str = input_str.lower()
    
    processed_str = processed_str.replace("!", "").replace("@", "").replace("#", "").replace("%", "")
    
    return processed_str

while True:
    input_str = input()
    if input_str == "":
        break
    print(process_string(input_str))