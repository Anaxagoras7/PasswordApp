from cryptography.fernet import Fernet    

#DURING REGISTRATION
def create_userfile(username):
    directory = "Files\\"
    filename = directory + username + ".txt"
    fileop = open(filename,'w+')
    return filename

#ADD SERVICE
def append_new_service(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)

#UPDATE A SERVICE
def update_service(file_name, modify_service, new_password):
    a_dictionary = {}
    a_file = open(file_name,'r+')
    for line in a_file:
        key, value = line.split()
        a_dictionary[key] = value

    a_dictionary[modify_service]=new_password
    a_file = open(file_name,'w+')
    for i in a_dictionary.keys():
        text_to_append = i+" "+a_dictionary[i]
        append_new_service(file_name, text_to_append)

#DELETE A SERVICE
def delete_service(file_name, del_service):
    a_dictionary = {}
    a_file = open(file_name,'r+')
    for line in a_file:
        key, value = line.split()
        a_dictionary[key] = value

    del a_dictionary[del_service]
    a_file = open(file_name,'w+')
    for i in a_dictionary.keys():
        text_to_append = i+" "+a_dictionary[i]
        append_new_service(file_name, text_to_append)

#Display file content to dictionary
a_dictionary = {}
a_file = open("text.txt", 'w+')
for line in a_file:
    key, value = line.split()
    a_dictionary[key] = value

#RLE ENCODE
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding

#RLE DECODE
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    return decode

#ENCRYPT FILE
def encryptFile(username):
    directory = "Files\\"
    keyfile = directory+username+".key"
    file = directory+username+".txt" 

    #read the key from the key file
    with open(keyfile, 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(file, 'rb') as file:
        original = file.read()
        
    # encrypting the file
    encrypted = fernet.encrypt(original)
    
    # opening the file in write mode and 
    # writing the encrypted data
    file = directory+username+".txt"
    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

#DECRYPT FILE
def decryptFile(username):
    
    directory = "Files\\"
    keyfile = directory+username+".key"
    file = directory+username+".txt" 

    #read the key from the key file
    with open(keyfile, 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # opening the encrypted file
    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    file = directory+username+".txt" 
    # opening the file in write mode and
    # writing the decrypted data
    with open(file, 'wb') as dec_file:
        dec_file.write(decrypted)

#Class
class Service:
    id=0
    service=""
    password=""