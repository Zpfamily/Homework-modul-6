import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
trans = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    trans[ord(cyrillic)] = latin
    trans[ord(cyrillic.upper())] = latin.upper()
    
def normalize(name: str) -> str:
    translate_name = re.sub(r'\W', '_', name.translate(trans))
    translate_name = ".".join(translate_name.rsplit("_",1))
    return translate_name

# print(normalize("і32.....23$%E%вап.pptx"))