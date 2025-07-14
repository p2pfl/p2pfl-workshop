# 🔬 P2PFL Demo: Testing Variations on MNIST

This demo showcases how **P2PFL** enables rapid experimentation with different environment variations in a decentralized setup.

You can launch experiments directly from a YAML configuration file using the `p2pfl run` command. For example, if you're working with `mnist.yaml`, simply run:

```bash
cd DEMO-2
p2pfl run mnist.yaml
```

This command looks for a configuration file named `mnist.yaml` in the current directory and executes the workflow defined there. It's a quick and clean way to run individual experiments.

---

For more advanced experimentation, such as comparing multiple aggregators or training conditions, you can use the `run_variations.py` script to automate and batch these runs. Here's how:

## 🖥️ Command

```bash
python run_variations.py mnist.yaml --aggregators FedAvg FedMedian
```

This command runs two separate experiments using different aggregation algorithms (FedAvg and FedMedian) based on the configuration defined in mnist.yaml. Each run is executed sequentially, allowing for easy comparison of performance across variations in a reproducible manner.

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
You can modify the `mnist.yaml` file directly to fine-tune settings like batch sizes, number of rounds, or peer-specific behaviors for deeper personalization.

📈 Experiment with different aggregators, data partitioning strategies, network topologies, and models to uncover how each factor influences training dynamics and final performance. For more details on available components and configuration options, check out the [P2PFL documentation](https://p2pfl.github.io/p2pfl/).