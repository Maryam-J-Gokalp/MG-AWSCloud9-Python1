{"filter":false,"title":"runCaesarCipherProgram().py","tooltip":"/runCaesarCipherProgram().py","undoManager":{"mark":53,"position":53,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":45},"action":"insert","lines":["Exercise 1: Creating a user-defined function"],"id":2}],[{"start":{"row":0,"column":45},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":3,"column":25},"action":"insert","lines":["def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet"],"id":4}],[{"start":{"row":3,"column":25},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]},{"start":{"row":4,"column":4},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["#"],"id":6}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":37},"action":"insert","lines":["Exercise 2: Encrypting a message"],"id":7}],[{"start":{"row":5,"column":37},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":8,"column":26},"action":"insert","lines":["def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt"],"id":9}],[{"start":{"row":8,"column":26},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":11},{"start":{"row":3,"column":25},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":25},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["#"],"id":14}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":37},"action":"insert","lines":["Exercise 3: Getting a cipher key"],"id":15}],[{"start":{"row":10,"column":37},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":13,"column":22},"action":"insert","lines":["def getCipherKey():","    shiftAmount = input( \"Please enter a key (whole number from 1-25): \")","    return shiftAmount"],"id":17}],[{"start":{"row":13,"column":22},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["#"],"id":20}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":37},"action":"insert","lines":["Exercise 4: Encrypting a message"],"id":21}],[{"start":{"row":15,"column":37},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":16,"column":4},"end":{"row":27,"column":27},"action":"insert","lines":["def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage"],"id":23}],[{"start":{"row":27,"column":27},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["€"],"id":25}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"remove","lines":["€"],"id":26}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["#"],"id":27}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":37},"action":"insert","lines":["Exercise 5: Decrypting a message"],"id":28}],[{"start":{"row":29,"column":37},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":32,"column":56},"action":"insert","lines":["def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)"],"id":30}],[{"start":{"row":32,"column":56},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":33,"column":4},"end":{"row":34,"column":0},"action":"insert","lines":["",""]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["#"],"id":32}],[{"start":{"row":34,"column":5},"end":{"row":34,"column":41},"action":"insert","lines":["Exercise 6: Creating a main function"],"id":33}],[{"start":{"row":34,"column":41},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":47,"column":52},"action":"insert","lines":["def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decypted Message: {myDecryptedMessage}')"],"id":35}],[{"start":{"row":47,"column":52},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":4},"end":{"row":49,"column":0},"action":"insert","lines":["",""]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":49,"column":4},"end":{"row":49,"column":28},"action":"insert","lines":["runCaesarCipherProgram()"],"id":37}],[{"start":{"row":49,"column":28},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":50,"column":4},"end":{"row":57,"column":29},"action":"insert","lines":["Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ","Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ","Please enter a message to encrypt: new message","new message","Please enter a key (whole number from 1-25): 4","4","Encrypted Message: RIA QIWWEKI","Decypted Message: NEW MESSAGE"],"id":39}],[{"start":{"row":57,"column":29},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":40}],[{"start":{"row":57,"column":29},"end":{"row":58,"column":0},"action":"remove","lines":["",""],"id":41}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":7},"action":"remove","lines":["def"],"id":42}],[{"start":{"row":6,"column":0},"end":{"row":8,"column":26},"action":"remove","lines":["     getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt"],"id":43},{"start":{"row":6,"column":0},"end":{"row":8,"column":26},"action":"insert","lines":["def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt"]}],[{"start":{"row":11,"column":0},"end":{"row":13,"column":22},"action":"remove","lines":["    def getCipherKey():","    shiftAmount = input( \"Please enter a key (whole number from 1-25): \")","    return shiftAmount"],"id":44},{"start":{"row":11,"column":0},"end":{"row":13,"column":22},"action":"insert","lines":["def getCipherKey():","    shiftAmount = input( \"Please enter a key (whole number from 1-25): \")","    return shiftAmount"]}],[{"start":{"row":16,"column":0},"end":{"row":27,"column":27},"action":"remove","lines":["    def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage"],"id":45},{"start":{"row":16,"column":0},"end":{"row":27,"column":27},"action":"insert","lines":["def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage"]}],[{"start":{"row":30,"column":0},"end":{"row":32,"column":56},"action":"remove","lines":["    def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)"],"id":46},{"start":{"row":30,"column":0},"end":{"row":32,"column":56},"action":"insert","lines":["def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)"]}],[{"start":{"row":35,"column":0},"end":{"row":47,"column":52},"action":"remove","lines":["    def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decypted Message: {myDecryptedMessage}')"],"id":47},{"start":{"row":35,"column":0},"end":{"row":47,"column":52},"action":"insert","lines":["def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decypted Message: {myDecryptedMessage}')"]}],[{"start":{"row":50,"column":0},"end":{"row":53,"column":11},"action":"remove","lines":["    Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ","Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ","Please enter a message to encrypt: new message","new message"],"id":48}],[{"start":{"row":50,"column":0},"end":{"row":54,"column":29},"action":"remove","lines":["","Please enter a key (whole number from 1-25): 4","4","Encrypted Message: RIA QIWWEKI","Decypted Message: NEW MESSAGE"],"id":49}],[{"start":{"row":49,"column":28},"end":{"row":50,"column":0},"action":"remove","lines":["",""],"id":50}],[{"start":{"row":48,"column":3},"end":{"row":49,"column":28},"action":"remove","lines":[" ","    runCaesarCipherProgram()"],"id":51},{"start":{"row":48,"column":2},"end":{"row":48,"column":3},"action":"remove","lines":[" "]},{"start":{"row":48,"column":1},"end":{"row":48,"column":2},"action":"remove","lines":[" "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":47,"column":52},"end":{"row":48,"column":0},"action":"remove","lines":["",""],"id":52}],[{"start":{"row":47,"column":52},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":28},"action":"insert","lines":["runCaesarCipherProgram()"],"id":54}]]},"ace":{"folds":[],"scrolltop":416,"scrollleft":0,"selection":{"start":{"row":48,"column":28},"end":{"row":48,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"start","mode":"ace/mode/python"}},"timestamp":1676397404263,"hash":"e98bc20d998463d2eb0b8e5316226642a351b5d6"}