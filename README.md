# Proof of Stake Blockchain Prototype

## Overview

This project implements a prototype of a Proof of Stake (PoS) blockchain system using Python. Proof of Stake is a consensus algorithm in which the creator of the next block(forger) is chosen based on probability which is proportional to the staking. Unlike Proof of Work, PoS does not require miners to solve complex mathematical problems, saving computational energy.

## Features

- **Staking:** Participants can lock a certain amount of cryptocurrency as stake to become eligible for block creation.

- **Block Creation:** The system selects a forger for the next block based on their stake. The forger constructs the block and adds it to the blockchain.

- **Transaction Validation:** Stakers validate transactions from the transaction pool and add them to the blockchain. Validators are chosen based on their stake.

- **P2P Communication:** Peer-to-peer Communication is used for interaction between the nodes and the nodes gets updated when lost connection or is newly joining the network.

## Prerequisites

- Python 3.x installed on your local machine
- Basic understanding of blockchain technology and Python programming
  
## Commands and interactions
- To run this code, open a new command terminal and navigate to this directory. enter: python main.py localhost 10001 5000
- to add a new node, do the same as above but with different port, api-port
- to run a transaction "python interaction.py"
- to view blockchain "host://api-port/blockchain"
- to add RSA keypairs to a node, you can include it when running the program(step 1) by including the relative path     of the file







