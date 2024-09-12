import sys

alphabet = {
  'to_English': {
    'O.....': ['a', '1'],
    'O.O...': ['b', '2'],
    'OO....': ['c', '3'],
    'OO.O..': ['d', '4'],
    'O..O..': ['e', '5'],
    'OOO...': ['f', '6'],
    'OOOO..': ['g', '7'],
    'O.OO..': ['h', '8'],
    '.OO...': ['i', '9'],
    '.OOO..': ['j', 'O'],
    'O...O.': ['k'],
    'O.O.O.': ['l'],
    'OO..O.': ['m'],
    'OO.OO.': ['n'],
    'O..OO.': ['o', '>'],
    'OOO.O.': ['p'],
    'OOOOO.': ['q'],
    'O.OOO.': ['r'],
    '.OO.O.': ['s'],
    '.OOOO.': ['t'],
    'O...OO': ['u'],
    'O.O.OO': ['v'],
    '.OOO.O': ['w'],
    'OO..OO': ['x'],
    'OO.OOO': ['y'],
    'O..OOO': ['z'],
    '..OO.O': ['.'],
    '..O...': [','],
    '..O.OO': ['?'],
    '..OOO.': ['!'],
    '..OO..': [':'],
    '..O.O.': [';'],
    '....OO': ['-'],
    '.O..O.': ['/'],
    '.OO..O': ['<'],
    'O.O..O': ['('],
    '.O.OO.': [')'],
    '......': [' ']
  },
  'to_Braille': {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    'O': '.OOO..',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
    ' ': '......'
  }
}

# Helper Functions
def isBraille(s):
  distinct_chars = set(s)
  if distinct_chars == {'O', '.'} and len(s) % 6 == 0:
    return True
  return False

def splitBrailleIntoLetters(s):
  return [s[i:i + 6] for i in range(0, len(s), 6)]

def to_English(s):
  braille_letters = splitBrailleIntoLetters(s)
  english_text = ''
  capitalizeNext = False
  isNumeric = False

  for letter in braille_letters:

    if letter == '.....O':
      capitalizeNext = True
      continue
    if letter == '.O...O' or letter == '.O.OOO': 
      isNumeric = True
      continue
    
    if letter == '......':
      isNumeric = False
      english_letter = ' '
    
    if isNumeric and letter == 'O..OO.':
      english_letter = alphabet['to_English'][letter][1]
    else:
      english_letter = alphabet['to_English'][letter][0]
      if capitalizeNext:
        english_letter = english_letter.upper()
        capitalizeNext = False
    
    english_text += english_letter
  return english_text

def to_Braille(s):
  braille_text = ''
  readingNumeric = False

  for char in s:
    braille_letter = ''

    if char.isspace():
      if readingNumeric:
        readingNumeric = False
    
    if char == '.' and readingNumeric:
      braille_letter += '.O...O'

    if char.isnumeric():
      if not readingNumeric:
        readingNumeric = True
        braille_letter += '.O.OOO'

    if char.isupper():
      braille_letter += '.....O'
      char = char.lower()

    braille_letter += alphabet['to_Braille'][char]

    braille_text += braille_letter
    
  return braille_text


if __name__ == "__main__":
  if len(sys.argv) > 1:
    words = sys.argv[1:]
    original_text = ' '.join(words)
    if isBraille(original_text):
      translated_text = to_English(original_text)
    else:
      translated_text = to_Braille(original_text)
    
    print(translated_text)
  else:
    print("No string given")

