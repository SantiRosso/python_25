# 16. Código Morse. Funciones para codificar y decodificar texto a código Morse y viceversa.

# Diccionario de traducción
morse_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.', 
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---', 
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---', 
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-', 
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--', 
    'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-', 
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ''
}

# Invertimos el diccionario para decodificar Morse
inv_morse_dict = {v: k for k, v in morse_dict.items()}

def texto_a_morse(texto):
    texto = texto.upper()
    morse = ''
    for letra in texto:
        if letra != ' ':
            morse += morse_dict.get(letra, '') + ' '
        else:
            morse += '  '  # Dos espacios entre palabras
    return morse.strip()

def morse_a_texto(morse):
    palabras = morse.split('  ')  # Separar palabras
    texto = ''
    for palabra in palabras:
        letras = palabra.split()
        for letra in letras:
            texto += inv_morse_dict.get(letra, '')
        texto += ' '
    return texto.strip()

def detectar_tipo(texto):
    if all(c in ['.', '-', ' '] for c in texto):
        return 'morse'
    else:
        return 'texto'

# Programa principal
entrada = input("Ingrese texto o código Morse: ")

tipo = detectar_tipo(entrada)

if tipo == 'texto':
    print("Texto a Morse:", texto_a_morse(entrada))
else:
    print("Morse a Texto:", morse_a_texto(entrada))
