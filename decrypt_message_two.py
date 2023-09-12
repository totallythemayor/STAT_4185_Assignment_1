encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

def decrypt_message_two(message):
    result = ""
    mess = list(message)
    mess_rev = mess[::-1]
    for i in range(len(mess_rev)):
        if i % 2 == 0:
            result += mess[i]
        else:
            result += mess_rev[i]
    return result


print(decrypt_message_two(encrypted_message))