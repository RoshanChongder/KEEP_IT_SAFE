import cryptography
from cryptography import *
from cryptography.fernet import Fernet
from read_write import inpop 

class layer_two :

    @staticmethod 
    def encrypt(file_path) :
        image = inpop.read_file(file_path)
        # generating a 128 bit key 
        key = Fernet.generate_key()   # generating very hard fernet key 128 bit key
        print(key)
        f = Fernet(key)   # creating the object of fernet by passing the key
        encrypted = f.encrypt(image) #encrypting the target file 
        inpop.write_file(file_path,encrypted) #overwriting the encrypted file 
        inpop.append_file(file_path,key)  # appending the key at the end of the file 
    
    @staticmethod 
    def decrypt(file_path) :
        image = inpop.read_file(file_path)
        key = bytes(image[-45:])   # last 128 bytes is the key 
        image = image[:-45]   # the target_file to decrypt 
        f = Fernet(key)  # getting the fernet object ready 
        decrypt = f.decrypt(image)
        inpop.write_file(file_path,decrypt) #storing the decrypted data 
