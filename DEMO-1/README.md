# 🔬 P2PFL Demo: Running Node1 and Node2

This demo shows how to run a simple **P2PFL** example using the MNIST dataset. It uses two nodes that collaborate to train a model without sharing raw data.

---

## ⚙️ Step-by-Step Instructions

### 🖥️ Terminal 1: Start Node 1

```bash
cd DEMO-1
python node1.py
```

- What it does:
Starts the first federated learning node.

- Details:
    - Runs `node1.py`, which initializes the peer and waits for the other node to connect.
    - Listens on port `7777` for incoming peer connections.

### 🖥️  Terminal 2: Start Node 2

```bash
cd DEMO-1
python node2.py
```

- What it does:
Starts the second federated learning node.

- Details:
    - Runs `node2.py`, which initializes the peer and begins FL training.
    - Connects to port `7777` of node1.

### 🔁 What Happens Next
- Both nodes train models locally on their respective MNIST datasets.
- They communicate through port 7777, exchanging model updates.
