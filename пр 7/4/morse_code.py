MORSE_CODE_DICT = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
    'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.',
    'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
    'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '......', ',': '.-.-.-', ';': '-.-.-.', ':': '---...', '?': '..--..', '!': '--..--', '(': '-.--.', 
    '/': '-..-.', '«': '.-..-.', '-': '-....-'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '/ '
    return morse_code.strip()