[Benchmarking Quantum Machine Learning Devices](https://www.chemicalqdevice.com/benchmarking-quantum-machine-learning-devices) PDF 9/19/23.

Introduction: Benchmarking a readily available graph quantum machine learning model using CPU and GPU quantum devices is practical for creating faster models. Here, permutation equivariant graph embeddings with trainable qubit rotations over the course of the run were successfully optimized. 

The quantum circuit size was increased to 25 qubits from 5 qubits to better distinguish single threaded CPU vs. single GPU speeds.
Pure states were utilized without quantum noise for convenient representations based on the surface of the “bloch sphere”. 
Adjoint differentiation was employed for time and memory efficient state vector circuits, likely through the diff_method='best' setting. 
Exact expectation values were obtained each time the circuit was assessed, which is suitable for Machine Learning workflows. 

Results: PennyLane Lightning.gpu had the fastest average runtimes by 5x over the closest CPU method. Lightning.qubit and Cirq.qsim experienced the best CPU quantum simulator runtimes. Qiskit.aer simulator was slightly slower than the simulators mentioned, which was then followed by Qulacs.simulator. Default.qubit was over twice as slow as any other cpu quantum simulator, but is currently PennyLane’s most compatible device.

Discussion: 5 runs with each quantum simulator clearly displayed time separations for the PennyLane “An equivariant graph embedding” demo without using multi-threading or multi-gpus on a 25 qubit quantum algorithm. Additional CPU benefits may be experienced with cirq.qsim’s advanced CPU in theory, however several models only run the slowest default.qubit simulator unless modifications to code are made or a new notebook is written. Faster and more compatible quantum simulators are probable, based on the frequency of device updates in platform release notes. Lightning.gpu was accessed through the Colab paid V100 GPU tier, according to installation instructions. CPU devices were installed using PennyLane-“Platform” in Colab with methods from the Devices and ecosystem documentation. 

Additional 2023 device benchmarkings were performed by Terra Quantum, and a comprehensive QED-C study was also published. 
