def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string


def is_palindrome(word: str) -> bool:
    to_remove = "áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ".lower()
    word = chr_remove(word, to_remove)
    word_separed = [char for char in word]
    word_reversed_list = word[::-1]
    word_reversed = "".join(word_reversed_list)
    if word == word_reversed:
        return True
    else:
        return False
    

def generate_structure(char_list: list) -> dict:
    structure = {}
    for char in char_list:
        structure[char] = char_list.count(char)
    return structure

def can_be_palindrome(word: str) -> bool:
    #NÃO ESTA FUNCIONANDO, DESISTI :(
    to_remove = "áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ".lower()
    word = chr_remove(word, to_remove)
    word_separed = [char for char in word]
    structure_word = generate_structure(word_separed)
    print(structure_word)
    if len(word) % 2 == 0:
        r = []
        for char, quantity in structure_word.items():
            if quantity % 2 != 0:
                r.append(False)
        if len(r) != 0:
            return False
    else:
        r = []
        for char, quantity in structure_word.items():
            if quantity % 2 == 0:
                r.append(False)
        if len(r) != 0:
            return False
    return True

print(is_palindrome("pedro"))
print(is_palindrome("tenet"))
print(is_palindrome("anna"))

    
    