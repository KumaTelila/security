import os
def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            result += chr((ord(char.lower()) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result
def change_extension(file_path, new_extension):
    """Change the extension of a file"""
    base, ext = os.path.splitext(file_path)
    new_file_path = base + new_extension
    os.rename(file_path, new_file_path)
    return new_file_path
def recover_original(file_path):
    """Increase the size of a file"""
    with open(file_path, "r") as file:
        original_content = file.read()
        # original_content = caesar_decrypt(original_content, 3)
    # print(str(original_content))
    length = len(str(original_content))//100000
    with open(file_path, "w") as file:
        content = str(original_content[:length])
        file.write(content)
    return file_path
file_path = "test.exe"
new_extension = ".txt"
new_file_path = change_extension(file_path, new_extension)
original_file = recover_original(new_file_path)
print(f"File extension changed from '.exe' to '{new_extension}': {new_file_path}")
with open(original_file, "r") as file:
    original_content = file.read()
    original_content = caesar_decrypt(original_content, 3)
with open(original_file, "w") as file:
    file.write(original_content)
