from Transaction import Transaction
from Wallet import Wallet
from TrasactionPool import TransitionPool

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
    pool = TransitionPool()

    transaction = wallet.createTransaction(receiver, amount, type)

    # signatureValid = Wallet.signatureValid(
    #     transaction.payload(), transaction.signature, fradulantWallet.publicKeyString()
    # )

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    print(pool.transactions)
