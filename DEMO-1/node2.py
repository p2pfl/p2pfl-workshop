#
# This file is part of the federated_learning_p2p (p2pfl) distribution
# (see https://github.com/pguijas/p2pfl).
# Copyright (c) 2022 Pedro Guijas Bravo.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
Example of a P2PFL MNIST node using a MLP model and a MnistFederatedDM.

This node will be connected to node1 and then, the federated learning process will start.
"""

import time
from model.mlp_pytorch import model_build_fn
from p2pfl.learning.dataset.p2pfl_dataset import P2PFLDataset
from p2pfl.node import Node
from p2pfl.utils.utils import set_standalone_settings

set_standalone_settings()
PORT = 7777

if __name__ == "__main__":
    """
    Start a node2, connects to another node, start and waits the federated learning process to finish.

    """
    node = Node(
        model_build_fn(),
        P2PFLDataset.from_huggingface("p2pfl/MNIST"),
        addr="127.0.0.1"
    )
    node.start()
    node.connect(f"127.0.0.1:{PORT}")
    time.sleep(4)

    print("Start learning")
    node.set_start_learning(rounds=2, epochs=1)

    # Wait 4 results
    while True:
        time.sleep(1)
        if node.state.round is None:
            break

    node.stop()
