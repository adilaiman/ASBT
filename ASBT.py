# Adi's Scuffed Bitcoin Tool (ASBT)
# Author: Adi Laiman
# Date: 01 March 2019 (01-03-2019)
# Email: laiman@posteo.de

# import bitcoin, qrcode modules duh? don't reinvent the wheel
# pip install bitcoin && pip install qrcode[pil]
import bitcoin
import qrcode as qr
import colorama # module to allow color output to console

# generates a private key (this is what you keep secret) and writes to txt file
def genPrivateKey():
    private_key = random_key()
    with open('privateKey.txt', 'w') as f:
        f.write(private_key)
    img = qr.make(private_key)
    img.save("privateKey.png")
    return private_key

# generates a public key using the already generated private key and writes to txt file
def genPublicKey(privateKey):
    public_key = privtopub(privateKey)
    with open('publicKey.txt', 'w') as f:
        f.write(public_key)
    return public_key

# generates a wallet address, this is the one you share to receive bitcoins, then writes to txt file and generates a qrcode png
def genWalletAddress(publicKey):
    walletAddress = pubtoaddr(publicKey)
    with open('walletAddress.txt', 'w') as f:
        f.write(walletAddress)
    img = qr.make(walletAddress)
    img.save("walletAddress.png")
    return walletAddress

# gets data from public blockchain and prints latest 10 transactions
def viewTransactions(walletAddress):

    # pull data from public block chain, stored as a list of dictionaries
    transactions = history(walletAddress)

    # Title
    print(Fore.GREEN + "\n---Transactional History---")

    # change satoshis into BTC and remove trailing string from block hash
    for transaction in transactions:
        transaction["value"] = transaction["value"]/(10**8)
        transaction["output"] = transaction["output"][:-2]


    if len(transactions) < 10:
        for counter, transaction in enumerate(transactions):
            print("\n---",counter+1,"---") # Title displaying the number of the transaction
            for k,v in transaction.items():
                # turn key, value pairs into string to output
                k_out = str(k)
                v_out = str(v)
                #format output
                if k == "value":
                    print("Amount: --> " + v_out + " BTC")
                elif k == "address":
                    print("Receive Address --> " + v_out)
                elif k == "output":
                    print("Block Hash --> " + v_out)
                elif k == "block_height":
                    print("Included In Blocks --> " + v_out)
                
        print(Style.RESET_ALL)
    else:
        for i in range(10):
            print("\n---",i+1,"---") # Title displaying the number of the transaction
            for k,v in transactions[i].items():
                # turn key, value pairs into string to output
                k_out = str(k)
                v_out = str(v)
                # format output
                if k == "value":
                    print("Amount: --> " + v_out + " BTC")
                elif k == "address":
                    print("Receive Address --> " + v_out)
                elif k == "output":
                    print("Block Hash --> " + v_out)
                elif k == "block_height":
                    print("Included In Blocks --> " + v_out)
        print(Style.RESET_ALL)

# get wallet balance
def getWalletBalance(walletAddress):

    # pull data from public block chain, stored as a list of dictionaries
    transactions = history(walletAddress)

    # change satoshis into BTC and remove trailing string from block hash
    for transaction in transactions:
        transaction["value"] = transaction["value"]/(10**8)

    balance = 0
    # if receive address is not equal to our wallet address, minus from total else add
    for transaction in transactions:
        if transaction["address"] == walletAddress:
            balance += transaction["value"]
        else:
            balance -= transaction["value"]

    return balance

# prompt to ask user what to do.
if __name__ == "__main__":
    init() # filter ANSI escape characters on windows
    loop = True
    while loop == True:
        print("<---Welcome to Adi's Scuffed Bitcoin Tool (ASBT)!--->")
        choice = input("(1) Generate Private Key. \n(2) Generate Public Key \n(3) Generate Wallet Address \n(4) View Transactions \n(5) Get Balance \n(6) Quit \nEnter your option: ")
        if choice == "1":
            print("\n" + Fore.GREEN + genPrivateKey() + Style.RESET_ALL + "\n")
        elif choice == "2":
            usersPrivateKey = input("Please enter your private key: ")
            print("\n" + Fore.GREEN +genPublicKey(usersPrivateKey) + Style.RESET_ALL + "\n")
        elif choice == "3":
            usersPublicKey = input("Please enter your public key: ")
            print("\n" + Fore.GREEN + genWalletAddress(usersPublicKey) + Style.RESET_ALL + "\n")
        elif choice == "4":
            usersWallet = input("Please enter your wallet address: ")
            viewTransactions(usersWallet)
        elif choice == "5":
            usersWallet = input("Please enter your wallet address: ")
            print("\n" + Fore.GREEN, getWalletBalance(usersWallet), Style.RESET_ALL + "\n")
        elif choice == "6":
            loop = False
            deinit()
        else:
            print("\n" + Fore.RED + "Invalid option, please choice an option between [1-6]" + Style.RESET_ALL + "\n")