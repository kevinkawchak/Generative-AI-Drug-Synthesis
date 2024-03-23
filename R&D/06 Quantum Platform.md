[ChemicalQDevice Quantum Medical Image Analysis Platform](https://www.chemicalqdevice.com/chemicalqdevice-quantum-medical-image-analysis-platform) PDF 6/19/23.

Introduction: The purpose of the Platform is to develop, test, and implement quantum algorithms into more complex hybrid medical
image analysis models. This will be accomplished by utilizing quantum algorithm advancements, ML strategy, and industry resources. <br>

Project #1 introduced an increase in image classes to 44 and dataset size to 4478 compared to previous iterations, with challenges in
more complex data analysis. Several classes contained less than 20 images to train from, which may not provide a good
representation of the brain tumor type for validation of unseen images, as shown in Figure 1. The other limitation in the study was that
the number of available qubits and quantum circuit were limited to 20, which did not match the original model guidelines. <br>

The “Quantum transfer learning” model states a 2:1 ratio between number of qubits:image classes. For best performance in previous
works, 8 qubits were used for 4 classes and 20 qubits were used for 10 classes; with 20 qubits maxing available resources due to
model complexity. Therefore, the number of optimal qubits and quantum circuit qubits for 44 classes should be 88. Figure 2,
normalized confusion matrix, illustrates a vertical “striping” between classes 25 and 32 likely due to not using ideal qubit numbers.<br>

Figures 3, 4, 5 are different combinations of machine learning hyperparameters for the same quantum algorithm 1. “A” weight decay
hyperparameters yielded the best results. Variants B and C were prohibited in training likely due to a gamma lr scheduler value that
was too high when utilizing learning rate reduction after a given epoch. Figures 6 and 7 illustrate two other smaller algorithms with
identical results to each other, due to having the same subpar sinusoidal function as revealed in algorithm testing. <br>

Additional model performance for this dataset can be expected by implementing 1) tensor network quantum circuits, 2) hybrid state
vector/tensor network quantum circuits, or 3) state vector algorithms with information and operation being local - to reach 88 qubits.
These methods have restrictions on quantum circuit types, and may require collaboration with vendors. In addition, datasets with
similar or higher classes consisting of larger numbers of images can be substituted for improved model training. <br>

A focus is on integrating testing methods from leading platforms for better quantum algorithm candidates to use in upcoming models.
