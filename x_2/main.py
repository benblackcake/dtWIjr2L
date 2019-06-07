from importlib import reload
from module_x2 import M1
import time
import random

def loop():
    for i in range(0,9):
        print(M1.__Attr_X__)
        t=random.randint(1, 10)
        time.sleep(t)
        print("sleep",t,"s")
        reload(M1)

if __name__=='__main__':

    loop()