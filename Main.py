from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node

if __name__ == "__main__":
    node = Node()
    print(node.blockchain)
    print(node.transactionPool)
    print(node.wallet)
