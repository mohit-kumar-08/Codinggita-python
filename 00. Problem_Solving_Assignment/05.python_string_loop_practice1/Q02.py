"""Decompress the string"""

compressed_string = input("Enter the compressed string: ")
decompressed_string = ""
for i in range(len(compressed_string)):
    if i % 2 == 0:
        decompressed_string += compressed_string[i] * int(compressed_string[i + 1])
print(decompressed_string)
