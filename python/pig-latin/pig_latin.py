"""Translate text to pig Latin."""

VOWELS = {"a", "e", "i", "o","u","A", "E", "I", "O", "U"}

def translate(text):
    consontant = ""
    
    if text[:2] == "xr" or text[:2] == "yt":
        return text + "ay"
        
    for letter in text:
        if is_consonant(letter):
            if letter != "y":
                VOWELS.add("y")
            if text[:2] == "qu":
                consontant += text[:2]
                text = text.replace(text[:2],"",1)
                break
            else:
                consontant += letter
                text = text.replace(text[0],"",1)
        else:
            break
    return str(text + consontant + "ay")

def is_consonant(letter):
    return not any (i in VOWELS for i in letter)
    
for word in ["yellow", "bob", "yellow"]:
    print(word, "-->", translate(word))
