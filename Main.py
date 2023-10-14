from Transaction import Transaction
from Wallet import Wallet
from TrasactionPool import TransitionPool
from Block import Block
from Blockchain import Blockchain
import pprint

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    type = "TRANSFER"

    wallet = Wallet()
    fradulantWallet = Wallet()
    pool = TransitionPool()

    transaction = wallet.createTransaction(receiver, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    block = wallet.createBlock(pool.transactions, "lastHash", 1)
    blockchain = Blockchain()
    blockchain.addBlock(block)
    pprint.pprint(blockchain.toJson())
