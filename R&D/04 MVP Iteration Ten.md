[Minimum Viable Product Iteration Ten](https://www.chemicalqdevice.com/minimum-viable-product-iteration-ten) PDF 6/7/23.

The goal today of incorporating quantum algorithms into classical models using medical data is primarily to help improve performance. The six steps of MVP Iteration 10 below helped gain a better understanding regarding the hybrid nature of image related models, and also limit over fitting present in previous iterations, as explained by [machine learning mastery](https://machinelearningmastery.com/learning-curves-for-diagnosing-machine-learning-model-performance/).

Terminology [Hybrid: Classical-quantum computing, Circuit = quantum algorithm consisting of quantum gates, Quantum gate: Matrix that modifies the quantum bit (qubit) at a specific time point, Quantum depth: Increases with additional layers of quantum gates, Quantum width: Increases by adding more qubits, CNN = Convolutional Neural Network for image analysis, used in hybrid models]

A) The Pennylane "Tensor-network quantum circuits" tutorial explains how to convert common State Vector quantum algorithms into MPS tensor networks. Tensor network incorporation into the classical-quantum transfer learning model being developed is being troubleshooted. Correctly optimized tensor networks can utilize a relatively smaller number of qubits for potential new applications in medical image analysis. (1-2) 

B) The "Optimizing a quantum circuit with PennyLane" tutorial by Albornoz, C. details how to print sine wave functions of quantum circuits with variable width, depth, and gates. Several circuits were analyzed in order to gain a greater understanding of which algorithm to use for scaling with classical code. (3)

C) New algorithms were written to allow for a modular approach of individual quantum gates at each qubit, replacing conventional "for loops". The trade off was that for loops typically yielded faster run times for the same circuit coded gate-by-gate. 

D) The Pennylane Lightning.gpu quantum simulator continues to be troubleshooted. A single GPU combined with a tensor network, for instance, will likely open additional applications involving more classes while using less RAM than other hybrid methods. (4-5)

E) Studies were performed to evaluate GPU RAM requirements when adding more layers of quantum gates onto the Iteration 9 brain image model (NVIDIA A100 40gb). (6)

F) All PyTorch ResNet CNNs (18, 34, 50, 101, 152) have been tested at lower epochs, with ResNet18 consistently having the fastest run times (the smallest CNN of those mentioned). ResNet18 also had the best performance, and due to its smaller output should be the least prone to over fitting for this hybrid application. 
