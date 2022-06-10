"""
Learn Blockchains by Build One

https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
"""
import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    @property
    def last_block(self):
        return self.chain[-1]

    def new_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount,
            }
        )
        return self.last_block["index"] + 1

    @staticmethod
    def hash(block):
        # using sort_key=True, Hashes have inconsistency.
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


def main():
    x = 5
    y = 0

    # hash that has last char is 0 is correct
    # the proof of work algorithm is called 'Hashcash'
    while hashlib.sha256(f"{x*y}".encode()).hexdigest()[-2:] != "00":
        y += 1

    print("The solution is y = {}".format(y))


if __name__ == "__main__":
    main()
