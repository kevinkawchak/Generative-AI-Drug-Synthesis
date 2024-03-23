[Quantum Parameter Study for Quantum Inspired Machine Learning](https://www.chemicalqdevice.com/quantum-parameter-study-for-quantum-inspired-machine-learning) PDF 9/26/23.

Introduction: Classical deep neural networks must contain the correct number and configurations of trainable “weights and biases” ie. parameters to achieve the best accuracies. In an analogous way, quantum machine learning trainable parameters through the optimization of qubit rotations can be performed with gates such as Ry, Rx, and Rz. In this study, different numbers of trainable Ry layers were implemented in a ‘Quantum transfer learning’ model in order to study the effect increasing circuit parameters has on a single dataset, as well as any observable trends between datasets. 

A) Effect Increasing Parameters has on Validation Accuracy for 5 Epochs
1) 2-Class Hymenoptera as a Standard did not experience improvements in accuracy with more trainable quantum parameters
2) 10-Class Tumor MRI dataset experienced the largest increase in accuracies as the number of parameters were increased
3) 44-Class Tumor MRI dataset had small improvements in accuracy for lower number of trainable parameters

B) Parameter Trends Across Different Datasets on Validation Accuracy 
Although the Hymenoptera dataset did not appear to exhibit a positive response to additional trainable parameters, the 10-Class and 44-Class datasets both generally increased in accuracy for the first 20 trainable parameters. With less total number of tumor classes and a greater number of images per class, the 10-Class dataset yielded the best accuracy increases for the highest number of parameters. Settings: ResNet50: (2048, n_qubits), Classes: (n_qubits, 44) or 10 or 2.

Discussion: Differences between training and validation losses were the lowest for the 10-class set for 40 parameters, which may indicate less concerns of overfitting. As quantum inspired methods and devices will likely be able to optimize large numbers of parameters, a productive approach will likely be to find the minimum number of parameters needed to assist classical deep learning. This study provided insight into parameter selection when best quality datasets are used. This study builds from prior algorithm prototypings, benchmarking, and cost/efficiency studies. The larger tumor datasets were also independently analyzed w/ larger circuits in separate studies.
