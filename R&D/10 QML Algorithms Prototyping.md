[Quantum ML Algorithms Prototyping for Neuroradiology](https://www.chemicalqdevice.com/quantum-ml-algorithms-prototyping-for-neuroradiology) PDF 7/24/23.

In general, brain images were first processed by the Resnet18 deep learning network, which outputs 512 image elements. Elements were dimensionally reduced and distributed across one of the 15 different quantum algorithms. The hybrid network runtimes for 1 Epoch ranged from several minutes to over one hour, depending on circuit complexity. Differences in quantum embedding and training layers allowed for the dataset to be mapped over qubits in unique ways - and therefore reaching a distribution of results, as shown on slide 1. Some algorithms were truncated from authors’ published results, and may also have been utilized in less than optimal ways. 

17 qubits were employed to accommodate the largest algorithm size possible to maximize performance, while accommodating GPU RAM and time restrictions associated with more gates. This July 24th study likely represents one of the largest quantum machine learning algorithm medical data comparison regarding several algorithms in literature (5), qubits (17), and classes (44). 

Top performing algorithms 6, 7, A, and B validation performances were further investigated for 10 Epochs:
Algorithm 6: Loss: 2.0379 Acc: 0.4776 
Algorithm 7: Loss: 2.0788 Acc: 0.5045
Algorithm A: Loss: 1.9580 Acc: 0.5242 
Algorithm B: Loss: 1.9759 Acc: 0.5183

The key benefit from the study was directly comparing several algorithms on a 44 class medical image dataset with 1000s of images and more qubits than other studies in literature. Future work will seek to gain additional fine tuning of quantum algorithms respective to challenging datasets and other Medical AI issues. The quantum computing method that was used is referred to as "gate model", while an emerging pulse programming method will likely be utilized to offer additional control over qubits, given some additional nuances. 

From the July 4th update, the quantum transfer learning model typically outperformed an analogous classical feature extraction model, but both models lack important "trainable" updates of the Resnet18 deep learning network that two other models benefited from. Top performing Algorithm A was slightly better when running on 20 qubits on the same dataset when compared to 17 qubits in the current study as seen in the July 12th update slide 3. The QTL model performance is highest with 2:1 qubits to classes; which 88 qubits for 44 classes would be ideal, however this ratio is not readily available.
