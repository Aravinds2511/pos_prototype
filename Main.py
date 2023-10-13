from Transaction import Transaction
from Wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    type = "TRANSFER"

    # transaction = Transaction(sender, receiver, amount, type)
    # wallet = Wallet()
    # signature = wallet.sign(transaction.toJson())
    # transaction.sign(signature)
    # signatureValid = Wallet.signatureValid(
    #     transaction.payload(), signature, wallet.publicKeyString()
    # )
    # print(signatureValid)

    wallet = Wallet()
    fradulantWallet = Wallet()

    transaction = wallet.createTransaction(receiver, amount, type)

    signatureValid = Wallet.signatureValid(
        transaction.payload(), transaction.signature, fradulantWallet.publicKeyString()
    )
    print(signatureValid)
