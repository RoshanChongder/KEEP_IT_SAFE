from windows import get_window 
class inpop :
    @staticmethod 
    def read_file(file_path) :
        try :
            fo=open(file_path,"rb")  # opening in reading binary mode 
            file = fo.read()     # reading teh target file 
            fo.close()   # closing the file 
            return file
        except Exception as e :
            get_window.show( file_path , "Error in file reading." )
            raise e 
    
    @staticmethod 
    def append_file(file_path,file) :
        try :
            fo=open(file_path,"a")  # opening in append mode  
            fo.write(str(file))   # overwriting file 
            fo.close()  # closing the file 
        except Exception as e :
            get_window.show(file_path , "Error in file writing.")
            raise e 

    
    
    @staticmethod 
    def write_file(file_path,file) :
        try :
            fo=open(file_path,"wb")  # opening in wb mode  
            fo.write(file)   # overwriting file 
            fo.close()  # closing the file 
        except Exception as e :
            get_window.show(file_path , "Error in file writing.")
            raise e 