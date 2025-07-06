# TranslateMe 😁

🎉 A fun CLI-based string converter that replaces all vowels with expressive emojis: `:D` for uppercase vowels, and `:/` for lowercase vowels. Also prints the author's name in a stylish way using `pyfiglet` and `termcolor`.

## ✨ Features

- Prints your alias in ASCII art (using `pyfiglet`)
- Colors the text using `termcolor`
- Converts vowels in user input to emoji-style representations
- Great for fun and beginner-level Python practice

## 🧠 How It Works

1. Displays the author's name (`CiND2R1`) in ASCII-art format (colored in blue).
2. Asks the user to enter a phrase.
3. Replaces each vowel:
   - Uppercase → `:D`
   - Lowercase → `:/`
4. Prints the transformed string.

### Example

Please Enter A phrase: Hello World!
Output: H:/ll/ W/:/rld!


## 📦 Requirements

- Python 3.x
- Libraries:
  ```bash
  pip install pyfiglet termcolor

## Run It
python TranslateME.py
