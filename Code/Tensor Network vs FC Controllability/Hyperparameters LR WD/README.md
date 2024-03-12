The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work.

Controllability in machine learning refers to the degree to which a system's behavior can be directed or influenced by adjusting model variables. It is desirable to achieve predictable performance improvements in ways that are consistent with the problem being solved. To verify controllability between two models in practice, a Google TensorNetwork demo was modified for this second iteration.

In specific, six sets of studies were conducted to understand how models react to changes in parameters, hyperparameters, or inputs. The best overall loss for the neural network, NN, out of the 98 experiments was 2.72E-06 vs. the more controllable and further improved neural network/tensor network, NN/TN, with a loss of 2.73E-08. These results represent approximately 100x better hybrid performance, which typically had lower run times.

The Neural network and Neural network/Tensor network 'matrix product operator' were run using analogous tests with 30 total metrics based on loss, time, and standard deviations using the best model from the March 4 first iteration classification study. https://lnkd.in/gj5uwTz5, https://lnkd.in/gCA8CK3U

Parameters
a) NN Dense Layers and NN/TN TNLayers each varied from 1-6, with NN/TN having the lowest overall loss with 3 TNLayers. 
b) NN Dense Layer neurons and NN/TN matrix/neurons each varied using 10 different configurations with the hybrid standard deviation of loss 4 orders of magnitude better.

Hyperparameters
a) NN and NN/TN each varied by 9 different learning rates, and 5 different learning rate/weight decay combinations with the majority of the success going to the NN. 
b) NN and NN/TN each varied by 6 different batch sizes with all the best metrics going to NN/TN. 
c) NN and NN/TN each varied by 7 different epoch values again had NN/TN hybrid with all the best metrics, including the lowest overall loss of all studies at 2.73E-08.

Inputs
a) NN and NN/TN each varied by 6 Dataset sizes also had the TN/NN winning all metrics over NN, including lowest loss by two orders of magnitude.

Out of the 30 key metrics, the NN/TN model won 23 for greatest controllability, with the remainder 7 going to NN, as shown in the supplementary. The most limiting factor for NN/TN performance was that adding too many TNLayers caused the loss to rise unfavorably to 1. In addition, a high learning rate of 0.100 also caused a high loss of 1, whereas NN faired better. Future studies will incorporate similar head-to-head studies between neural networks, tensor networks, or hybrid combinations. Some model interpretations were assisted by OpenAI. Repository: https://lnkd.in/gW_VQfdq

--
Sincerely,
CEO Kevin Kawchak
