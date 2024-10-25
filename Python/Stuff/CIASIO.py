def getkey():
    from datetime import datetime, timezone
    dt = datetime.now(timezone.utc)
    time = dt.strftime('%H:%M:%S')
    print(time)
    passkey = dt.strftime('%H%M%S')
    passkey = passkey[::-1]
    return passkey

def login(passkey):
    auth = False
    keytempt = str(input("Enter passkey: "))
    if passkey == keytempt:
        auth = True
        return auth
    
def run(auth):
    if auth == True:
        morsecode()

def morsecode():
            #Data Structure-Dictionary
            Morsedictionary = { "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F":"..-.", "G":"--.", "H":"....", "I":"..","J":".---","K":"-.-","L":".-..","M":"--",
                                    "N":"-.", "O":"---", "P":".--.","Q":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..", "1":".----","2":"..---",
                                    "3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}
            def MorseEncode(message):
                morse_code = ''
                for char in message.upper():
                    #Slection
                    if char in Morsedictionary:
                        morse_code += Morsedictionary[char] +' '
                #Return
                return morse_code
            def MorseDecode(morse_code):
                message = ''
                morse_code = morse_code.split(' ')
                for code in morse_code:
                    #Selection
                    for char, morse in Morsedictionary.items():
                        if morse == code:
                            message += char
                #Return
                return message
            def main():
                choice = input("Would you like to decode or encode: ")
                #Data Structure-Set
                O1 = {"Encode", "ENCODE", "encode"}
                O2 = {"Decode", "DECODE", "decode"}
                #Selection
                if choice in O1:
                    print()
                    message = input("Enter a mesage to be encoded: ")
                    morse_code = MorseEncode(message)
                    print(morse_code)
                    #Selection
                if choice in O2:
                    print()
                    morse_code = input("Enter a morse code sequence to be decoded: ")
                    message = MorseDecode(morse_code)
                    print(message)
                #Selection
                if choice not in O1 and O2:
                    print('Please try again')
                    main()


