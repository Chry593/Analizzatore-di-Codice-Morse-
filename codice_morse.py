#creiamo diz di traduzione
from numpy import tracemalloc_domain


diz = {
    ".-" : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.." : "D",
    "." : "E",
    "..-." : "F",
    "--." : "G",
    "...." : "H",
    ".." : "I",
    ".---" : "J",
    "-.-" : "K",
    ".-.." : "L",
    "--" : "M",
    "-." : "N",
    "---" : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-." : "R",
    "..." : "S",
    "-" : "T",
    "..-" : "U",
    "...-" : "V",
    ".--" : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z",
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "...." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9",
    "-----" : "0",
    "/" : " ",      #per lo spazio fra una parola e l'altra
    ".-.-.-" : ".",
    "--..--" : ",",
    "---..." : ":",
    "..--.." : "?",
    "-...-"  : "=",
    "-....-" : "-",
    "-.--."  : "(",
    "-.--.-" : ")",
    ".-..-." : '"',
    ".----." : "'"
    


}


def traduzione_morse_to_normal(diz_trad , stringa_morse: str) -> str:
    return "".join([diz[morse] for morse in stringa_morse.split() if morse in diz])

#trad da morse a testo
morse ="-.-. .. .- --- / -.-. --- -- . / ... - .- ..--.. / ... .--. . .-. --- / - ..- - - --- / -... . -. . --..-- / --- --. --. .. / ... .. .- -- --- / ... - .- - .. / .- .-.. / -- .- .-. . / . / .- -... -... .. .- -- --- ---... / .---- / -- .- -. --. .. .- - --- --..-- / ..--- / ..-. .- - - --- / .. .-.. / -... .- --. -. --- .-.-.-"
print(traduzione_morse_to_normal(diz,morse))


def traduzione_normal_to_morse(diz_trad , stringa_nomale: str):
    
    tradotto = []
    for lettera in list(stringa_nomale):
        for morse,normale in diz.items():
            
            if lettera == normale:
                
                tradotto.append(morse)
                tradotto.append(" ") #spazio fra un codice e l'altro
    return "".join(tradotto) 

normale ="ciao come stai? spero tutto bene, oggi siamo stati al mare e abbiamo: 1 mangiato, 2 fatto il bagno."
print(traduzione_normal_to_morse(diz,normale.upper()))


   