from ed_layer_one import layer_one 
from ed_layer_two import layer_two 
from windows import get_window 
from sys import argv


def main():
    try :
        get_window.show("Notification" ,"Keep a copy of the file")
        if len(argv)==1 :
            get_window.show("Error","No user key passed")
        else :
            p = get_window.path()
            layer_one.edcrypt(argv[1],p)
            layer_two.encrypt(p)
    except Exception as e :
        print(e)
        get_window.show("Error","Some thing went wrong .")

if __name__ == '__main__' : 
    main()

