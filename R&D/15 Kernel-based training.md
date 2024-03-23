[Kernel-based training parameter study](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/PennyLane/Quantum%20Parameters%20II/Kernel-based%20training%20parameter%20study%2011-16-23.pdf) PDF 11/16/23.

Purpose: Thoroughly analyze the effects adding quantum parameters has on model performance <br>

Plan: <br>
1) Improve runtimes by switching from lightning.qubit to lightning.gpu quantum device
2) Improve runtimes by switching from parameter-shift to adjoint differentiation method
3) Run 3 sets of 10 experiments: Increasing Layers 1-10 for ‘CNOT’, ‘CZ’, and ‘CY’ imprimitives <br>

Experimental: Using a Python IDE, 30 experiments were completed to determine accuracies of the Iris
2 Class dataset, the test loss, and model runtimes <br>

Results: All experiments with at least 4 Ansatz Layers achieved 100% Test Accuracy. The CY based
circuit with 8 Layers achieved the best Loss minimum of 0.035. Runtimes for 10 Layers favored
‘CNOT’ at 95.8s, followed by ‘CY’ at 104.2s, and ‘CZ’ at 104.2s. A separate embedding quantum
circuit in the demonstration also achieved perfect test accuracy 
