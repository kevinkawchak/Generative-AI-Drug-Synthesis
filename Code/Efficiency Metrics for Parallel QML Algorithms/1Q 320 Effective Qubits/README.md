The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work. 

320 1-Qubit quantum circuits were run in parallel to obtain Training and Validation results of 0.0000 Loss and 100.00% Accuracy each for the 'Turning quantum nodes into Torch Layers' Bromley, T. demo using the make moons dataset. This was achieved with multiple angle embedding gates and a higher learning rate at Epoch 8/20 on a High-RAM CPU with 2.4GB RAM. 

The significance of the results is that running many quantum circuits within PyTorch neural networks to reach more optimal results prevents exponential increases in RAM associated with high qubit single circuits. PennyLane's 'TorchLayer' is another developer tool that helps limit computational resources which is a similar approach taken with circuit cutting or tensor networks. 

The 01/11/24 [PDF](https://drive.google.com/file/d/1oU3jp9bSKiK1KMVby3YkAulKo7AY30x2/view?usp=sharing), [Seminar](https://www.youtube.com/watch?v=ZFADek7Z3Ak), and [Mobile](https://www.chemicalqdevice.com/efficiency-metrics-single-vs-parallel-qml-algorithms) Version are available online.
