def main():
    file_path = 'books/frankenstein.txt'
    output_text(file_path) #call the output_text function to see if the user wants to output the text from the book
    text = read_text(file_path) #assign the 'text' variable as the output of the read_text function
    word_count = get_word_count(text) #assign the 'word_count' variable to the output of the 'get_word_count' function
    print(f"The word count for the text is: {word_count}")
    get_char_count(file_path)

def get_word_count(text):
    words = text.split()
    return len(words)

def read_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

def output_text(file_path):
    read_text_input = input("Would you like to output the text from the book into the console? (y/n): ")
    if read_text_input in ('y', 'Y'):
        print(f'{read_text(file_path)}\n')
    elif read_text_input in ('n', 'N'):
        pass
    else:
        print("Sorry that is not a valid input, please try again.")
        return output_text(file_path)

def get_char_count(file_path):
    character_dict = {}
    words = read_text(file_path).lower()
    for char in words:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    print(character_dict)




main()

