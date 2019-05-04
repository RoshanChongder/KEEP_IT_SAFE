import tkinter
import cryptography
import sys
from tkinter import *
from tkinter import filedialog
from cryptography import *
from cryptography.fernet import Fernet
from tkinter import messagebox
from sys import argv
import test
from test import *

#first encryption
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

#function to store the key
def store_key(key,s):
    #print(type(key))
    s = s[:s.index('.')]
    s=s+".txt"
    point = open(s, 'bw')
    point.write(key)
    point.close()

#function to provide a message
def show(s,t):
    window=Tk()
    window.withdraw()
    messagebox.showinfo(s,t)

# getting the path of the file
def path():
    root=Tk()
    root.withdraw()
    file_path=filedialog.askopenfilename()
    return file_path

try:
    show("SELECT LOCATION","Select The File To Encrypt")
    file_path=path()
    #print(argv)
    #input()
    enc1(argv[1],file_path)
    # reading the image file
    point=open(file_path,"rb")
    image=point.read()
    #print("imge opened")
    point.close()

    #generating a key
    key =Fernet.generate_key()
    #print(key )
    #print('key lenght is ',len(key))

    # storing the key
    store_key(key,file_path)

    encoded=image   # to encode
    #encrypting the message
    f=Fernet(key)   # creating the obkect of ferne by passing the key
    encrypted=f.encrypt(encoded)
    #storing the image

    image=encrypted
    point=open(file_path,  "wb")
    point.write(image)
    point.close()
    show("NOTIFICATION","TAKE THE KEY FROM LOCATION :"+file_path+" AND KEEP A SEPARATE OF THE ENCRYPTED FILE ")

except :
    show("ERROR","Some thing went wrong.Either the password is wrong or problem wiht the file")
