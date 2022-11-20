import os
import base64
import requests
from hashlib import md5
from time import time


class Initialization:
    def Info():
        print('''
___  ___       _____            _____  _____   __ 
|  \/  |      |  _  |          |  _  ||  _  | / _|
| .  . |  ___ | |/' |__      __| |/' || |/' || |_ 
| |\/| | / _ \|  /| |\ \ /\ / /|  /| ||  /| ||  _|
| |  | ||  __/\ |_/ / \ V  V / \ |_/ /\ |_/ /| |  
\_|  |_/ \___| \___/   \_/\_/   \___/  \___/ |_|  
 _____                           _  _             
/  ___|                         (_)| |            
\ `--.   ___   ___  _   _  _ __  _ | |_  _   _    
 `--. \ / _ \ / __|| | | || '__|| || __|| | | |   
/\__/ /|  __/| (__ | |_| || |   | || |_ | |_| |   
\____/  \___| \___| \__,_||_|   |_| \__| \__, |   
                                          __/ |   
                                         |___/    


        ''')
        print("CTF-Tools by Me0w00f Security Members!")
    
    def Version(file):
        f = open(file)
        print("Version: " + f.read())
    
    def OptionsTips():
        print('''

(0) Exit

[Crypto]
(1) Base64 To Text
(2) Text To Base64
(3) Base32 To Text
(4) Text To Base32
(5) MD5 Decrypto
(6) Generate password composed of numbers.
        ''')
        Selected = int(input("Please select a number:"))
        return Selected


class Crypto:
    def Base64ToText(raw):
        Text = base64.b64decode(raw).decode("utf-8")
        return Text

    def TextToBase64(Text):
        raw = base64.b64encode(Text.encode("utf-8"))
        return raw.decode("utf-8")

    def Base32ToText(raw):
        Text = base64.b32decode(raw).decode("utf-8")
        return Text

    def TextToBase32(Text):
        raw = base64.b32encode(Text.encode("utf-8"))
        return raw.decode("utf-8")
    
    def DecryptoMD5(raw, dicts, threads):
        os.system("python crackmd5.py " + raw + " " + dicts + " " + threads)

    def g4pass(filename):
        f = open(filename, 'x')
        for i in range(1000,10000):
            f.write(str(i) + "\n")
        f.close()
        print('File saved as:' + os.getcwd() + '/' + filename)
    
    def g5pass(filename):
        f = open(filename, 'x')
        for i in range(10000,100000):
            f.write(str(i) + "\n")
        f.close()
        print('File saved as:' + os.getcwd() + '/' + filename)

    def g6pass(filename):
        f = open(filename, 'x')
        for i in range(100000,1000000):
            f.write(str(i) + "\n")
        f.close()
        print('File saved as:' + os.getcwd() + '/' + filename)

    def g8pass(filename):
        f = open(filename, 'x')
        for i in range(10000000,100000000):
            f.write(str(i) + "\n")
        f.close()
        print('File saved as:' + os.getcwd() + '/' + filename)


if __name__ == '__main__':
    Initialization.Info()
    Initialization.Version("./.version")
    selected = Initialization.OptionsTips()
    if selected == 1:
        raw = input("Input the base64 String:")
        print("\n\n" + Crypto.Base64ToText(raw) + "\n\n")
    elif selected == 2:
        text = input("Input the text:")
        print("\n\n" + Crypto.TextToBase64(text) + "\n\n")
    elif selected == 3:
        raw = input("Input the base32 String:")
        print("\n\n" + Crypto.Base32ToText(raw) + "\n\n")
    elif selected == 4:
        text = input("Input the text:")
        print("\n\n" + Crypto.TextToBase32(text) + "\n\n")
    elif selected == 5:
        raw = input("Input MD5:")
        dicts = input("Input the filename of dictionary:")
        threads = input("Input the threads:")
        start = time()
        Crypto.DecryptoMD5(raw, dicts, threads)
        print("Time used: ", time() - start)
    elif selected == 6:
        filename = input("Please input the filename:")
        bits = int(input("How many bits do you want? (4,5,6,8):"))
        if bits == 4:
            start = time()
            Crypto.g4pass(filename)
            print("Time used: ", time() - start, "s")
        elif bits == 5:
            start = time()
            Crypto.g5pass(filename)
            print("Time used: ", time() - start, "s")
        elif bits == 6:
            start = time()
            Crypto.g6pass(filename)
            print("Time used: ", time() - start, "s")
        elif bits == 8:
            start = time()
            Crypto.g8pass(filename)
            print("Time used: ", time() - start, "s")
        else:
            print("Error! There's no type like this!")
    elif selected == 0:
        print("Exit, Bye~")
    else:
        print("Error Option!")
