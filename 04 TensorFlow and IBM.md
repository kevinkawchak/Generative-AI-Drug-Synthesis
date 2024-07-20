[Google TensorFlow and IBM Software Stacks](https://drive.google.com/file/d/1gR-JlNDo2WR5kDK_SW5mvgwd8ZNT-rxo/view?usp=share_link) PDF 5/1/23.

Quantum machine learning is showing potential to bring additional power for classical models "that have become more
sophisticated and expensive to train" over time. Qml software stacks for Google TensorFlow Quantum (TFQ) and IBM Qiskit
Quantum Machine Learning (QML) illustrate hybrid quantum-classical workflows which incorporate quantum algorithms with
TensorFlow and Pytorch (see attachments). The two diagrams are applicable to researchers who would like to commit to a qml
platform for machine learning type projects. <br>

Google's TensorFlow Quantum integrates quantum computing algorithms and logic designed in Google Cirq. Quantum
computers can then assist machine learning due to their increasing ability to perform fast linear algebra on a state space that
grows exponentially with the number of qubits. In general, the goals of using TFQ for qml are "to optimize over a parameterized
class of computations" to generate certain low energy wavefunction, learn to extract non-local information, and learn how to
generate a quantum distribution from data. <br>

At the top of the TensorFlow Quantum software stack attached begins with either classical data or quantum data. (both data
types are commonly interconverted, but can result in a reduction from max performance). Classical data is processed by
TensorFlow, while quantum circuits and quantum operators are processed by TFQ. Next, Keras Models process both classical
data which proceeds to TF Layers, and quantum data which proceeds to TFQ Layers and TFQ Differentiators. TF Ops and TFQ
Ops separately instantiatiate dataflow graphs. TFQ qsim quantum simulator processes data by quantum mechanics on a
classical computer, and Cirq is for creating quantum algorithms. TPUs, GPUs, CPUs, and QPUs are available for utilization at
the bottom of the stack. <br>
