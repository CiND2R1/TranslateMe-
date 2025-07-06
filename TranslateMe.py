import pyfiglet
import termcolor

Author = pyfiglet.figlet_format("CiND2R1")

print(termcolor.colored(Author, color="blue"))

vowel = "AIEOUaieou"

def translator(str):
    translator = ""
    termcolor.colored(translator, color="red")
    for letter in str:
        if letter in vowel:
            if letter.isupper():
                translator = translator + ":D"
            else:
                translator = translator + ":/"
        else: 
            translator = translator + letter
    return translator

print(translator(input("Please Enter A phrase: ")))