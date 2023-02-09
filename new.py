import os
def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            result += chr((ord(char.lower()) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result
def increase_file_size(file_path):
    """Increase the size of a file"""
    with open(file_path, "r") as file:
        original_content = file.read()
        original_content = caesar_encrypt(original_content, 3)
    with open(file_path, "w") as file:
        content = str(original_content)*100000
        file.write(content)
    return file_path
def change_extension(file_path, new_extension):
    """Change the extension of a file"""
    base, ext = os.path.splitext(file_path)
    new_file_path = base + new_extension
    os.rename(file_path, new_file_path)
    return new_file_path

file_path = "test.txt"
new_extension = ".exe"
incresed_file = increase_file_size(file_path)
new_file_path = change_extension(incresed_file, new_extension)
print(f"File extension changed from '.txt' to '{new_extension}' and file size increased: {new_file_path}")
