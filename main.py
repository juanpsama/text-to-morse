#Using the international morse code
#found on https://en.wikipedia.org/wiki/Morse_code
morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.', ' ':' '
}

def morse_to_text():
    print('Please enter dots as "." and dashes as "-" and separate the letters with a blank space " "')
    print('all words not found in the International Morse Code will be ignored')
    text_to_convert = input('Enter your Code\n')
    text_converted = ''
    letter_list = text_to_convert.split()
    for letter in letter_list:
        # Value to search for
        value_to_find = letter
        # Iterate through the dictionary to find the key
        for key, value in morse_code_dict.items():
            if value == value_to_find:
                text_converted += key
                break  # Break the loop once the key is found
    print(text_converted)

def text_to_morse():
    print('All special symbols will be ignored, please enter only common letters an numbers')
    text_to_convert = input('Enter your Text\n').upper()
    text_clean = '' 
    morse_code = ''
    for letter in text_to_convert:
        if letter in morse_code_dict:#Cleaning the data of special chars
            morse_code += morse_code_dict[letter]
            morse_code += ' '
            #Text to show the cleaned data 
            text_clean += letter

    print(f'Entered Text: {text_clean}')
    print(f'The morse code for the entered text is:\n{morse_code}')

print('1: Morse to Text, 2: Text to Morse')
print('Enter an option 1 or 2:')
try:
    option = int(input('Option: '))
except:
    print('You enter an invalid option code')
else:
    if option == 1:
        morse_to_text()
    else:
        text_to_morse()
