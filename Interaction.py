from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(receiver.publicKeyString(), amount, type)
    url = "http://localhost:5000/transaction"
    package = {"transaction": BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)


if __name__ == "__main__":
    bob = Wallet()
    alice = Wallet()
    alice.fromKey("keys/stakerPrivateKey.pem")
    exchange = Wallet()
    john = Wallet()

    # forger: genesis
    postTransaction(exchange, alice, 100, "EXCHANGE")
    postTransaction(exchange, bob, 100, "EXCHANGE")
    postTransaction(alice, alice, 25, "STAKE")

    # forger: chosen by pos
    postTransaction(bob, john, 1, "TRANSFER")
