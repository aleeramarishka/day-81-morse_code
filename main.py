
morse_code_chart = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
            'G':'--.','H':'....','I':'..','J':'.---','K':'-.-',
            'L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
            'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--',
            'X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---',
            '3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
            '8':'---..','9':'----.','0':'-----'}


def convert_morse_code(text):
    morse_code = ""

    if text.replace(' ', '').isalnum():
        for char in text.replace(' ',''):
            morse_code += morse_code_chart[char]+' '
        print(morse_code)
    else:
        print("Only alphanumeric is allowed.")



msg = input("Type the message to morse code: ").upper()

convert_morse_code(msg)