from random import randint

MY_MESSAGE = "It's time to create an original message !"
MY_VERY_LOOOOOOOOONG_MESSAGE = """It's time to create an original message !
I don't know what to say but I guess that it's important to write things to get a better result.
Don't you think ? Have a nice day. Maybe I should have used a lorem ipsum... crap. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
in culpa qui officia deserunt mollit anim id est laborum."""

# Create a random size list with random int values
my_key = [randint(0, 9) for _ in range(4)]

def encipher_message(message_to_encipher:str, key:list) -> str :
    """Encipher a given message and return the crypted message using the given key"""
    enciphered_message = ""
    key_index = 0
    for i in range(len(message_to_encipher)) :
        enciphered_message += chr(ord(message_to_encipher[i]) + key[key_index])
        key_index += 1
        if(key_index == len(key)) : key_index = 0
    return enciphered_message

def decipher_message(message_to_decipher:str, key:list) -> str :
    """Decipher a given message by using the given key and return the result"""
    
    # Correction : also possible to do : 
    # return encipher_message(message, [-elt for elt in key])
    
    deciphered_message = ""
    key_index = 0
    for i in range(len(message_to_decipher)) :
        deciphered_message += chr(ord(message_to_decipher[i]) - key[key_index])
        key_index += 1
        if(key_index == len(key)) : key_index = 0
        # Or : key_index = key_index % 4
    return deciphered_message

def decrypt_message(message_to_decrypt:str) -> str :
    """Decrypt a given message by finding its key (random list) and return the result"""
    decrypted_key = []
    for i in range(4) :
        character_frequency_dict = {}
        for character in range(i, len(message_to_decrypt), 4) :
            try :
                character_frequency_dict[message_to_decrypt[character]] += 1
            except :
                character_frequency_dict[message_to_decrypt[character]] = 1

        max_count = 0
        most_frequent_char = ""
        for character, value in character_frequency_dict.items() :
            if value > max_count :
                max_count = value
                most_frequent_char = character

        space_char_difference = ord(most_frequent_char) - ord(" ")
        decrypted_key.append(space_char_difference)
    return decipher_message(message_to_decrypt, decrypted_key)

"""my_enciphered_message = encipher_message(MY_MESSAGE, my_key)
print(my_enciphered_message)
my_deciphered_message = decipher_message(my_enciphered_message, my_key)
print(my_deciphered_message)"""

long_crypted_message = encipher_message(MY_VERY_LOOOOOOOOONG_MESSAGE, my_key)
print(decrypt_message(long_crypted_message))

# Pour décrypter des clés dont on ne connaît pas la taille (liste de 10 par exemple)
# Il faut réaliser une analyse de fréquence qui grandit progressivement et renvoyer le résultat
# à chaque fois.
# Conseil : ne pas dépasser 1/4 de la taille de la chaîne de caractères sinon les résultats
# sont trop instables.