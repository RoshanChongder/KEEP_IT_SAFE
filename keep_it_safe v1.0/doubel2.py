from tkinter import *
from tkinter import filedialog
from  cryptography import *
from cryptography.fernet import Fernet
from tkinter import messagebox
from sys import argv
import test as f

def enc1(argv,file_path):
    key=""
    for i in argv:
        key=key+i
    key=sum([ord(i) for i in key])
    key=key%48
    #print(key)

    #reading the data file
    #print(file_path)
    fo=open(file_path,"rb")
    image=fo.read()
    fo.close()

    image=bytearray(image)

    for index,value in enumerate(image):
        image[index]=value^key

    #writing data in  the file
    fo=open(file_path,"wb")
    fo.write(image)
    fo.close()

#function to provide a message
def show(s,t):
    window=Tk()
    window.withdraw()
    messagebox.showinfo(s, t)

#getting the path of the encrypted file
def path():
    root=Tk()
    root.withdraw()
    file_path=filedialog.askopenfilename()
    return file_path

try:
    show("SELECT LOCATION","Select The File To Decrypt")

    file_path=path()
    # reading the image file
    point=open(file_path,"rb")
    image=point.read()
    #print("image opened")
    point.close()

    # load the key
    show("SELECT","Select key To Decrypt")
    s=path()
    point=open(s , "rb" )
    key=point.read()
    #print("key opened")
    point.close()

    #decrypting  the message
    f2=Fernet(key)
    dec=f2.decrypt(image)

    image=dec
    #writitng the file
    point=open(file_path,"wb")
    point.write(image)
    point.close()
    #print(argv)
    #input()
    enc1(argv[1],file_path)
    show("NOTIFICATION","Decryption Successfull")
except :
    show("ERROR","Wrong key or Wrong file with respect to the key")






