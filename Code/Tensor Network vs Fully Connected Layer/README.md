The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work. [Notebook.](https://github.com/google/TensorNetwork/blob/master/colabs/Tensor_Networks_in_Neural_Networks.ipynb)

Google's TensorNetwork repository includes a python demo that substitutes a tensor network layer in place of a 2nd fully connected layer for a classification task. The TNLayer matrix product operator used a significantly reduced number of parameters while producing much better loss 1.6x faster than utilizing a non-TN model. 
Here, loss and time evaluations were obtained by using random seeds for libraries, maximizing machine learning verbosity, and implementing start/stop timers for both models on a high-ram cpu. 

Modifying the number of parameters on the TN and non-TN models using a variety of techniques did not produce appreciably better results. However, increasing the number of consecutive TNLayers provided additional loss performance over the standard model. In specific, when TNLayers were increased from 1 to 3, the final epoch loss improved from 1.7180e-06 to 1.9317e-07 at a similar run time as the non-TN model that had a much higher loss of 7.6851e-04.  

Model interpretations were aided by OpenAI and a Stanford Quantum Tensor Network Workshop with Google X. 
