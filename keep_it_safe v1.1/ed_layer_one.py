from read_write import inpop
class layer_one :
    @staticmethod  
    def get_key(argv) :
        key=""
        for i in argv:
            key=key+i
        key=sum([ord(i) for i in key])
        key=key%48  # arbitary mod
        return key 
    
    @staticmethod 
    def xor(file,key) :
        for index,value in enumerate(file):
            file[index]=value^key  # perfoming xor operation with every byte of data
        return file 
    
    @staticmethod 
    def edcrypt(argv,file_path):
        key = layer_one.get_key(argv)  # getting the key ( sum of passed number ) 
        #reading the data file 
        image=inpop.read_file(file_path)    # reading teh target file  
        image=bytearray(image)  # converting the target file into byte array 
        image = layer_one.xor(image,key)
        #writing data in  the file with the key itself
        inpop.write_file(file_path,image) # writing the file first 
        inpop.append_file(file_path,key) # appending the key at the end of the file 
    