# 🔬 P2PFL Demo: Testing Aggregator Variations on MNIST

This demo showcases how **P2PFL** enables rapid experimentation with different environment variations in a decentralized setup.

---

## 🖥️ Command

```bash
python run_variations.py mnist.yaml --aggregators FedAvg FedMedian
```

## 🧠 What This Does
- Script: run_variations.py
    - A utility for testing multiple configurations in a reproducible way.

- Config file: mnist.yaml
    - Defines the dataset, model architecture, training parameters, and peers.

- Aggregators: FedAvg, FedMedian
    - Specifies two different aggregation algorithms to evaluate during the experiment.

## 🧪 Try Your Own Combinations!
To fully explore the performance and behavior of different federated learning setups, try running the script with combinations of the parameters below:

```bash
python examples/run_variations.py examples/mnist/mnist.yaml \
  --aggregators <Aggregator1> <Aggregator2> ... \
  --seeds <Seed1> <Seed2> ... \
  --nodes <NodeCount1> <NodeCount2> ... \
  --rounds <RoundCount1> <RoundCount2> ... \
  --epochs <Epochs1> <Epochs2> ... \
  --topologies <Topology1> <Topology2> ... \
  --partitioning <Strategy1> <Strategy2> ... \
  --models <Model1> <Model2> ... \
  --batch-sizes <BatchSize1> <BatchSize2> ...
```

🛠️ Need more control?
You can modify the `mnist.yaml` file directly to fine-tune settings like learning rates, optimizers, model architectures, or peer-specific behaviors for deeper personalization.

📈 Experiment with different aggregators, data partitioning strategies, network topologies, and models to uncover how each factor influences training dynamics and final performance.