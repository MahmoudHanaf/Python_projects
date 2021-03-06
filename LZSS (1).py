
def elements_in_array(check_elements, elements):
    i = 0
    offset = 0
    for element in elements:
        if len(check_elements) <= offset:
            # All the elements in check_elements are in elements
            return i - len(check_elements)

        if check_elements[offset] == element:
            offset += 1
        else:
            offset = 0

        i += 1
    return -1

encoding = "utf-8"

def encode(text, max_sliding_window_size=4096):
    text_bytes1 = text.encode(encoding)

    search_buffer = []  # Array of integers, representing bytes
    check_characters = []  # Array of integers, representing bytes
    output1 = []  # Output array

    i = 0
    for char1 in text_bytes1:
        check_characters.append(char1)
        index = elements_in_array(check_characters, search_buffer)  # The index where the characters appear in our search buffer

        if index == -1 or i == len(text_bytes1) - 1:
            if len(check_characters) > 1:
                index = elements_in_array(check_characters[:-1], search_buffer)
                offset = i - index - len(check_characters) + 1  # Calculate the relative offset
                length = len(check_characters)  # Set the length of the token (how many character it represents)

                token = f"<{offset},{length}>"  # Build our token

                if len(token) > length:
                    # Length of token is greater than the length it represents, so output the character
                    output1.extend(check_characters)  # Output the characters
                else:
                    output1.extend(token.encode(encoding))  # Output our token
            else:
                output1.extend(check_characters)  # Output the character

            check_characters = []

        search_buffer.append(char1)  # Add the character to our search buffer

        if len(search_buffer) > max_sliding_window_size:  # Check to see if it exceeds the max_sliding_window_size
            search_buffer = search_buffer[1:]  # Remove the first element from the search_buffer

        i += 1

    return bytes(output1)

print(encode("supercalifragilisticexpialidocious supercalifragilisticexpialidocious", 1024).decode(encoding)+"\n")


def decode(text):

    text_bytes = text.encode(encoding)  # The text encoded as bytes
    output = []  # The output characters

    inside_token = False
    scanning_offset = True

    length = []  # Length number encoded as bytes
    offset = []  # Offset number encoded as bytes

    for char in text_bytes:
        if char == "<".encode(encoding)[0]:
            inside_token = True  # We're now inside a token
            scanning_offset = True  # We're now looking for the length number

        elif char == ",".encode(encoding)[0]:
            scanning_offset = False
        elif char == ">".encode(encoding)[0] and inside_token:
            inside_token = False  # We're no longer inside a token

            # Convert length and offsets to an integer
            length_num = int(bytes(length).decode(encoding))
            offset_num = int(bytes(offset).decode(encoding))

            # Get text that the token represents
            referenced_text = output[-offset_num:][:length_num]

            output.extend(
                referenced_text)  # referenced_text is a list of bytes, so we use extend to add each one to output

            # Reset length and offset
            length, offset = [], []
        elif inside_token:
            if scanning_offset:
                offset.append(char)
            else:
                length.append(char)
        else:
            output.append(char)  # Add the character to our output

    return bytes(output)

print(decode("supercalifragilisticexpialidocious <35,34>").decode(encoding)+"\n")

text1 = "supercalifragilisticexpialidocious supercalifragilisticexpialidocious"
encoded = encode(text1).decode(encoding)
decoded = decode(encoded).decode(encoding)

print(f"Original: {len(text1)}, Encoded: {len(encoded)}, Decoded: {len(decoded)}"+"\n")
print(f"Lossless: {text1 == decoded}"+"\n")
print(f"Compressed size: {(len(encoded)/len(text1)) * 100}%")
















