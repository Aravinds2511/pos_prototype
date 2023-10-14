from Block import Block
from BlockchainUtils import BlockchainUtils


class Blockchain:
    def __init__(self):
        self.blocks = [Block.genesis()]

    def addBlock(self, block):
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data["blocks"] = jsonBlocks
        return data

    def blockCountValid(self, block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False

    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockchainUtils.hash(
            self.blocks[-1].payload()
        ).hexdigest()
        if latestBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False
