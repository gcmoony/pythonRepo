def decodeMorse(morse_code):
    numbers = [chr(num + 48) for num in range(10)]
    numbersMorse = [".----", "..---", "...--", "....-", ".....",
                "-....", "--...", "---..", "----.", "-----"]
    numbersDict = dict(zip(numbersMorse, numbers))
    letters = [chr(letter + 65) for letter in range(26)]
    lettersMorse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                "-.--", "--.."]
    morseDict = dict(zip(lettersMorse, letters))
    morseDict.update(numbersDict)
    morseDict[' '] = " "
    print(morse_code.split())
    #text = [morseDict[item] for item in morse_code.split('    ')]
    #print(text)
    #return text

decodeMorse('.... . -.--   .--- ..- -.. .')