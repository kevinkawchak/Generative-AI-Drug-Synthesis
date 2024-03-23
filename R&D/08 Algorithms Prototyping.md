[Quantum Algorithms Prototyping for Neuroradiology](https://www.chemicalqdevice.com/quantum-algorithms-prototyping-for-neuroradiology) PDF 7/12/23.

How can quantum computing algorithms be used in healthcare? Algorithms can be used for theoretical speedups and/or utilizing the physics of quantum bits to process datasets in a different and advantageous way. Based on literature, the near term approach for quantum benefit appears to be with the latter - which includes separating classical dataset classes over qubits; and obtaining greater performance separations between classical and quantum algorithms. 

Here, ChemicalQDevice builds on the July 5th 4400+ brain tumor image/44 class study by creating, testing, and pairing different quantum algorithms into the Pennylane quantum transfer learning model. In specific, the previously utilized Algorithm 1 was compared against three new candidate algorithms, which were first verified by their corresponding sine functions. Due to the increased complexity and runtimes for some of the algorithms, rapid prototyping on a high performance NVIDIA gpu was used to perform 4 separate 10 epoch runs.

Algorithm 1: A previously optimized embedding layer consisting of quantum "gates"
Algorithm 2: The quantum gates in Algorithm 1 were coded in the reverse order
Algorithm 3: Two additional rotational gates were added to the embedding layer of Algorithm 1
Algorithm 4: Same embedding as Algorithm 1, but with two rotational gates in the variational layer

Results: The short runs yielded separations in Performance, Runtime, and GPU ram usage across the algorithms. Algorithms 3 and 4 had similar longer runtimes, but the arrangement of rotational gates in the variational layer was preferred for performance over adding gates to the embedding layer, as shown in Figure 4. Overall runtime favored Algorithm 1, as it contained a more conventional arrangement of quantum gates when compared to Algorithm 2, Figure 1. Gpu ram favored smaller Algorithms 1 and 2, with top performing Algorithm 4 using the most ram, due to the rotational gate parameters updating throughout the run. Algorithms are expected to yield higher performance w/ more epochs.

ChemicalQDevice vs. Best QML Medical Image Studies:
Number of Classes: 44, ChemicalQDevice 
Number of Medical Images: 9500, Microsoft 
Total Number of Qubits: 20, ChemicalQDevice 
Accuracy (Non-binary): 4 Class, Chongqing Normal U., 97.8% 
