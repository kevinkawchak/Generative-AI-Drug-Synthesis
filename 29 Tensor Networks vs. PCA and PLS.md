[Tensor Networks vs. PCA and PLS for High Dimensional Medical Datasets](https://www.chemicalqdevice.com/tensor-networks-vs-pca-and-pls) Event Seminar and PDF 03/21/24.

A single patient with many medical tests yields high dimensional data which can be challenging to process, analyze, and visualize. Principal component analysis (PCA), Partial least squares (PLS), and Tensor networks (TNs) share similar approaches of matrix approximations utilizing Singular Value Decomposition (SVD), but vary in the types of problems they can solve.

PCA makes use of different components that are ordered based on variance. The first component has the largest variance, and is typically the most important component under study. Subsequent components have smaller variance and contain less valuable information. The PCA method achieves dimensionality reduction of the data while preserving the most significant information, Slides 10-12.

PLS regression is used to reduce the number of explanatory variables to a smaller set of uncorrelated variables. PLS is often used in situations where traditional regression methods might not perform well due to multicollinearity. PLS is also used when PCA is not able to include the dependent variable to be utilized as a prediction model later in the process, Slides 13-19.

Tensor networks can represent high-dimensional data in terms of interconnected tensors. These high dimensional tensors are then further decomposed into a network of smaller tensors that aim to retain only the most important features. Solutions to complex problems using hybrid NNs/TNs, large quantum circuits, or other tensorizations are expected to see further improvements in functionality and performance, Slides 21-24. Some explanations aided by OpenAI. 
