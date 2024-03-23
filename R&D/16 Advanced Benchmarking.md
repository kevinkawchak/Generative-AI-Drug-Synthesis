[Advanced Benchmarking/Efficiency; PennyLane QML/QiML](https://www.chemicalqdevice.com/advanced-benchmarkingefficiency-pennylane-qmlqiml) PDF 11/28/23.

Purpose: The objective of this study was to extend on previous speed benchmarkings and gain new insight regarding additional configurations with cost, efficiency, and standard deviation metric considerations. 

Plan: Run 25 qubit permutation equivariant graph embeddings consisting of trainable qubit rotations by Schuld, M. with 17 Simulator/Colab hardware configurations 5 times each for a total of 85 runs. 

Experiment: The Google Colab IDE was utilized with notebooks varying in the A) Colab accelerator, B) Python quantum simulator installation packages, and C) PennyLane specific simulator adjustments through the ‘dev’ variable. Each of the runs were made available on GitHub. 

Results: The lightning.gpu A100 configuration had the fastest average runtime and lowest standard deviation of all runs (20.04s, 0.14). V100 and T4 variants had slower runtimes, but T4 was the most efficient gpu for this configuration. The low cost cpu option with cirq.qsim, lightning.qubit, or lightning.kokkos yielded high efficiencies, with lightning.kokkos CPU having the lowest cost and highest efficiency ($0.0001, 102.07). The lightning.kokkos TPU configuration was the fastest kokkos configuration. Additional speedups may be realized with further troubleshooting of the kokkos gpu documentation. 

Discussion: The majority of the devices achieved runtimes that were as expected based on marketed speedups for 25 qubits (For example: default.qubit < lightning.qubit < lightning.kokkos). Progress with gpu variants of qulacs.simulator and qiskit.aer have been documented by researchers, which were not able to be implemented. Cirq.qsim and lightning.qubit offered similar runtimes, with lightning.qubit CPU remaining the most viable option moving forward. Future studies will focus on more applications of different lightning.gpu and lightning.kokkos configurations in larger models with medical data.

Additional 2023 device benchmarkings have also been performed by Terra Quantum, and QED-C. 
