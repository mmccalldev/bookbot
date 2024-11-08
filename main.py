def main():
    book_path = file_path()
    output_text(book_path) #call the output_text function to see if the user wants to output the text from the book
    text = read_text(book_path) #assign the 'text' variable as the output of the read_text function
    word_count = get_word_count(text) #assign the 'word_count' variable to the output of the 'get_word_count' function
    char_dict = get_char_count(book_path)
    print_report(word_count, char_dict, book_path)

def file_path():
    while True:
        try:
            book_path = input('Please input the file path or file name of a text within the "books/" directory: ')
            if 'books/' in book_path:
                with open(book_path):
                    return book_path
            appended_path = 'books/' + book_path
            with open(appended_path):
                return appended_path
        except KeyboardInterrupt:
                print("\nProgram interrupted by user.")
                exit()
        except FileNotFoundError:
            print('Sorry that is an invalid file path, please input the file path again: ')
            continue

def get_word_count(text):
    words = text.split()
    return len(words)

def read_text(book_path):
    try:
        with open(book_path) as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f'Error: could not find file {book_path}')
        exit()
    except PermissionError:
        print(f"Error: No permission to read file {book_path}")
        exit()
    except Exception as e:
        print(f'Error: {e}')
        exit()

def output_text(book_path):
    try:
        read_text_input = input("Would you like to output the text from the book into the console? (y/n): ")
        if read_text_input in ('y', 'Y', 'yes', 'Yes'):
            print(f'{read_text(book_path)}\n')
        elif read_text_input in ('n', 'N', 'no', 'No'):
            pass
        else:
            print("Sorry that is not a valid input, please try again.")
            return output_text(book_path)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        exit()


def get_char_count(book_path):
    character_dict = {}
    words = read_text(book_path).lower()
    for char in words:
        if char.isalpha():
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    return character_dict

def sort_on(char_dict):
    return char_dict['num']

def sort_dict(char_dict):
    char_dict_list = []
    for char, num in char_dict.items():
        char_dict_list.append({'char': char, 'num': num })
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

def print_report(word_count, char_dict, book_path):
    #print header
    print(f"--- Begin Report of {book_path} ---")

    #print word count
    print(f"There are {word_count} words in the provided text.\n")

    #get sorted list of character counts
    sorted_chars = sort_dict(char_dict)

    #print each character count
    for char in sorted_chars:
        print(f"The '{char['char']}' character was found {char['num']} times.")

    print("--- End Report ---")

main()

