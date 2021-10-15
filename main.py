from flask import Flask
app = Flask(__name__)

@app.route("/")
def main_page():
    return "<h1>welcome to the Morse code converter</h1>"

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'," ": "|"}

@app.route('/decrypt/<user_message>')
def decrypt(user_message):
    cipher = " "
    for letter in user_message:
        cipher += MORSE_CODE_DICT[letter] + " "
    return f'<h2>Your morse code is: {cipher}</h2>'


@app.route('/encrypt/<user_message>')
def encrypt(user_message):
    cipher = ""
    mylist = []
    message = ""

    for letter in user_message:
        cipher += letter
        mylist = cipher.split()
    for i in mylist:
        for key in MORSE_CODE_DICT:
            if i == MORSE_CODE_DICT[key]:
                message += key
    return f'<h2>Your morse code is: {message}</h2>'


if __name__ == '__main__':
    app.run(debug=True,port=1800)