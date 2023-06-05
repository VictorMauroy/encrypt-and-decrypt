from random import randint
my_message = "It's time to create an original message !"
my_key = randint(0, 26)
antoine_message = ']\x8a\x89\x85\x8a\x90\x8d;\x88\x80\x8e;\x8f\x8dă\x8e;~\x83\x80\x8d\x8e;|\x8b\x8b\x8d\x80\x89|\x89\x8f\x8eI;aĄ\x87\x84~\x84\x8f|\x8f\x84\x8a\x89\x8e;û;\x91\x8a\x90\x8eG;\x91\x8a\x90\x8e;|\x91\x80\x95;\x8dĄ\x90\x8e\x8e\x84;û;~|\x8e\x8e\x80\x8d;~\x80;~\x8a\x7f\x80;<;e\x80;\x8e\x90\x84\x8e;\x81\x84\x80\x8d;\x7f\x80;\x91\x8a\x90\x8eI;h|\x84\x89\x8f\x80\x89|\x89\x8fG;\x91\x8a\x90\x8e;\x8b\x8a\x90\x91\x80\x95;~\x8a\x88\x88\x80\x89~\x80\x8d;\x87\x80;~\x8a\x7f\x80;\x7f\x80;q\x84\x82\x80\x89ă\x8d\x80'

# Useful functions : 
#   - ord('char') : take a Unicode character and return the corresponding Unicode integer 
#   - chr(my_int) : take an integer and return the corresponding Unicode character

def encipher_message(message_to_encipher:str, key:int) -> str :
    """Encipher a given message and return the crypted message using the given key

    Returns:
        str: Enciphered message
    """
    enciphered_message = ""
    for i in range(len(message_to_encipher)) :
        enciphered_message += chr(ord(message_to_encipher[i]) + key)
    return enciphered_message

def decipher_message(message_to_decipher:str, key:int) -> str :
    """Decipher a given message by using the given key and return the result

    Returns:
        str: deciphered message
    """
    deciphered_message = ""
    for i in range(len(message_to_decipher)) :
        deciphered_message += chr(ord(message_to_decipher[i]) - key)
    return deciphered_message

def decrypt_message_for_caesar(message_to_decrypt:str) -> str :
    """Decrypt a given message by finding its key and return the result

    Returns:
        str: decrypted message
    """
    character_frequency_dict = {}
    for character in message_to_decrypt :
        try :
            character_frequency_dict[character] += 1
        except :
            character_frequency_dict[character] = 1
    
    max_count = 0
    most_frequent_char = ""
    for character, value in character_frequency_dict.items() :
        if value > max_count :
            max_count = value
            most_frequent_char = character

    space_char_difference = ord(most_frequent_char) - ord(" ")
    #print(f"Difference between most frequent char and basic space char : {space_char_difference}")
    return decipher_message(message_to_decrypt, space_char_difference)

"""my_enciphered_message = encipher_message(my_message, my_key)
print(my_enciphered_message)
my_deciphered_message = decipher_message(my_enciphered_message, my_key)
print(my_deciphered_message)"""

print(f"Antoine's message is : {decrypt_message_for_caesar(antoine_message)}")