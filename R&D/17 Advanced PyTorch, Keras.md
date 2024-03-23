[Advanced PyTorch, Keras Deep Learning with QML/QiML](https://drive.google.com/file/d/1haT2_R3Ghkb1QlCCRA9WNx7yYCzfj-PB/view?usp=drive_link) PDF, [Mobile Version](https://www.chemicalqdevice.com/advanced-pytorch-keras-deep-learning-with-qmlqiml) 12/7/23. 

Incorporating many small quantum algorithms in parallel using PyTorch or Keras neural networks is a promising method to distribute high dimensional data from classical nodes across circuits. This is done to avoid exponential increases in RAM and Runtime associated with adding qubits to algorithms. 

Although Hilbert spaces are restricted for circuits with limited numbers of qubits, their small scale makes them easier to study, and the combined quantum effects may make parallelization a viable application for larger classifications vs. less exact quantum tensor networks.

In this study, a PyTorch neural network with 64 2-qubit quantum algorithms decreased model loss for 100% accuracy. Also, it was observed that having more parallel layers yielded faster processing times per layer than with less quantum algorithms. (Slide 09)

In addition, a Keras framework with 8 4-qubit algorithms achieved 100% accuracy on a more difficult dataset, making it the best overall tested neural network. (Slide 12) Future studies will focus on using more circuits in parallel, different algorithm combinations, and alternative architectures.

Many benchmarkings for Qiskit and PennyLane models revealed the need to fix high performance devices such as NVIDIA GPUs used with QiML libraries and PyTorch or Keras. A discussion is available through the startup video channel. 
