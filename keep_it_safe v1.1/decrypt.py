from ed_layer_one import layer_one 
from ed_layer_two import layer_two 
from windows import get_window 
from sys import argv


def main():
    try :
        if len(argv)==1 :
            get_window.show("Error","No user key passed")
        else :
            p = get_window.path()
            layer_two.decrypt(p)
            layer_one.edcrypt(argv[1],p)
    except Exception as e :
        get_window.show("Error" , "Something went wrong .")
if __name__ == '__main__' : 
    main()

