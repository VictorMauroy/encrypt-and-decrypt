from random import randint

MY_MESSAGE = "It's time to create an original message !"
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
    deciphered_message = ""
    key_index = 0
    for i in range(len(message_to_decipher)) :
        deciphered_message += chr(ord(message_to_decipher[i]) - key[key_index])
        key_index += 1
        if(key_index == len(key)) : key_index = 0
    return deciphered_message

my_enciphered_message = encipher_message(MY_MESSAGE, my_key)
print(my_enciphered_message)
my_deciphered_message = decipher_message(my_enciphered_message, my_key)
print(my_deciphered_message)