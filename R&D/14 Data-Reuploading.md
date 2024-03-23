[Data-Reuploading, Quantum Universal Classifier R&D](https://www.chemicalqdevice.com/data-reuploading-quantum-universal-classifier-rd) PDF 10/10/23.

“A single-qubit quantum circuit which can implement arbitrary unitary operations can be used as a universal classifier much like a single hidden-layer Neural Network.” Ahmed, S., Quantum Computing Researcher.

Introduction: A paper titled “Data re-uploading for a universal quantum classifier” by Pérez-Salinas, A., et al. in 2020 detailed how to load a higher dimensional data point represented by x, and breaking it into sets of parameters U(x). Matrix multiplication in circuits represent a linear component, while collapsing the quantum state into 0 or 1 represents the nonlinear component, analogous to classical neural networks. A cost function representing the sum of the fidelities can then be used with an optimizer for determination of optimal weights for classification.

Experimental: The author identified the appropriate layers for the model, and then likely adjusted the batch size and learning rate for the fastest run times (Tables 1-3). Adjusting layers did not improve the original method, but increasing the batch size improved accuracy by 2.7% (Table 2); while only decreasing the learning rate increased accuracy by 5.9% (Table 3). Increasing dataset size by 10x yielded similar results, while a 100x increase decreased accuracy, and increased runtime by several hours (Table 4). Triplicate studies were identical for the author’s model, and also for three runs in a revised method. Notebooks are available through GitHub Medical-Quantum-Machine-Learning, Code, PennyLane.

Action: The goal of using rich single qubit information to better classify datasets will likely require greater insight into how larger datasets interact with rotational gates. New PQC architectures and revisions to the way quantum parameters are trained likely also need improvements. The Ahmed, S. demo also detailed how more than one qubit can be used to create a Universal Function Approximator. Watch, N., et al. have also successfully used multi-dimensional qudits to “successfully learn highly non-linear decision boundaries of classification problems such as the MNIST digit recognition problem.” Single qubit (binary class) or single qudit (multi-class) methods deserve additional research, as limiting the number of qubits or qudits drastically reduces RAM and Runtime requirements in quantum simulators for larger dataset and classical model incorporations.

References:
[1](https://pennylane.ai/qml/demos/tutorial_data_reuploading_classifier/)
[2](https://docs.pennylane.ai/projects/lightning/en/v0.25.0/devices.html)
[3](https://arxiv.org/pdf/1907.02085.pdf)
[4](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/tree/main)
[5](https://link.springer.com/article/10.1007/s42484-023-00125-0) 
[6](https://github.com/nlwach/Data-Re-Uploading-on-Qudits) 
