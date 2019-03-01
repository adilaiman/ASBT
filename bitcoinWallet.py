#Adi's Scuffed Bitcoin Tool (ASBT)
#Author: Adi Laiman
#Email: laiman@posteo.de

#import bitcoin, qrcode modules duh? don't reinvent the wheel
#pip install bitcoin && pip install qrcode[pil]
from bitcoin import *
import qrcode as qr
from colorama import * # module to allow color output to console

#generates a private key (this is what you keep secret) and writes to txt file
def genPrivateKey():
    private_key = random_key()
    with open('privateKey.txt', 'w') as f:
        f.write(private_key)
    return private_key

#generates a public key using the already generated private key and writes to txt file
def genPublicKey(privateKey):
    public_key = privtopub(privateKey)
    with open('publicKey.txt', 'w') as f:
        f.write(public_key)
    return public_key

#generates a wallet address, this is the one you share to receive bitcoins, then writes to txt file and generates a qrcode png
def genWalletAddress(publicKey):
    walletAddress = pubtoaddr(publicKey)
    with open('walletAddress.txt', 'w') as f:
        f.write(walletAddress)
    img = qr.make(walletAddress)
    img.save("walletAddress.png")
    return walletAddress