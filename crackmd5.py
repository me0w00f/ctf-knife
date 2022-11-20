import threading
from hashlib import md5 as _md5

def MD5(bytes):
    m=_md5()
    m.update(bytes)
    return m.hexdigest()

class _PWDict:
    def __init__(self,filename):
        self.mutex = threading.Lock()
        self.fp = open(filename,'rb')

    def get(self):
        with self.mutex:
            bytes = self.fp.readline()
        return bytes.strip()

class _crackMD5:
    def __init__(self,md5,PWDict,func=None,threadQuantity=5):
        self.md5 = md5.lower()
        self.D = PWDict
        if func:
            self.func = func
        else:
            self.func = print

        self.threadQuantity = threadQuantity

        self.status = False
        self.T = []

    def _run(self):
        while self.status:
            bytes = self.D.get()
            if self.md5 == MD5(bytes):
                self.status = False
                self.func(bytes)
            
    def start(self):
        self.status = True
        for i in range(self.threadQuantity):
            thread = threading.Thread(target=self._run)
            thread.start()
            self.T.append(thread)

def main():
    import sys
    if len(sys.argv) < 3:
        print("usage:  crackmd5.py md5-hash dictionary_file [thread_quantity]")
        return

    md5 = sys.argv[1]

    if len(md5)!=32:
        print('只支持长度位32的MD5 HASH')
        return

    dict_file = sys.argv[2]

    try:
        D = _PWDict(dict_file)
    except Exception as e:
        print(e)
        return
    
    if len(sys.argv) >3:
        tc=int(sys.argv[3])
        if tc <1:
            print("错误的线程数.")
            return
    else:
        tc = 5

    def myPrint(v):
        print("[Done!]：",v.decode("utf-8"))

    crackMD5 = _crackMD5(md5,D,myPrint,tc)
    print('cracking ...')
    crackMD5.start()

if __name__ == '__main__':
    main()