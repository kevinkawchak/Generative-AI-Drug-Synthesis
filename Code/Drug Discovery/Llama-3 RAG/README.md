The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work.
[Cover Image](https://drive.google.com/file/d/1kXghQNdIzucYKEWj7i7BHxwojexr3ONd/view?usp=sharing)

According to NVIDIA: 'Retrieval-Augmented Generation', or RAG, is a technique for enhancing the accuracy and reliability of generative AI models using facts from a knowledge base. Large language models such as Llama 3 can respond to a wide variety of human queries, but RAG embeddings can deliver final authoritative answers combined with the power to cite sources. (1)

Here, meta-llama/Meta-Llama-3-8B-Instruct was used to provide good overall reasoning, while BAAI/bge-small-en-v1.5 was used to answer specific questions regarding the UCI Heart Disease dataset in a notebook by Sakil786. (2-5) The LLM+RAG model answered a battery of questions based on the small dataset with 4 databases very well, with examples shown below; notebook is available on github. 

Question: Briefly explain heart disease related to the study: 
Answer: The study is related to the diagnosis of heart disease using a dataset of 76 attributes, but only 14 of which are actually used. The dataset contains information from four locations: Cleveland Clinic Foundation, Hungarian Institute of Cardiology, V.A. Medical Center, and University Hospital, Zurich, Switzerland. The study aims to develop a probability algorithm for the diagnosis of coronary artery disease using logistic-regression-derived discriminant function...

Question: What are the key findings related to patient health?
Answer: The key findings related to patient health are not explicitly mentioned in the provided context information. However, based on the attribute information and the new.data file, the following can be inferred:
1. The dataset contains information about patients with heart disease, including demographic details, medical history, and test results...

A more specific question was answered correctly regarding the open-source 'Warning' file that was manually compared to the original cleveland.data file.
Question: What happened to the cleveland.data file?
Answer: The cleveland.data file was "messed up" when it was loaded on a different node, and the file processed.cleveland.data is a cleaned up version of the original file. The original file appears to be corrupted and the author will need to obtain a new copy from the donor.

The above results show the power of using RAG to answer very specific questions, as the model does not need fine-tuned, although RAG can be used in conjunction with a fine-tuned model; or used with larger LLMs due to no GPU training requirements. Future work will focus on further optimizing RAG methods with other LLM techniques when necessary, on Drug Discovery related datasets. 

1) NVIDIA, 2023: https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/
2) meta-llama/Meta-Llama-3-8B-Instruct, Llama3 license: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
3) BAAI/bge-small-en-v1.5, MIT license: https://huggingface.co/BAAI/bge-small-en-v1.5
4) Sakil786 RAG_using_Llama_3.ipynb, GPL-3.0 license: https://github.com/Sakil786/RAG_using_Llama-3/blob/main/RAG_using_Llama_3.ipynb
5) UCI/Heart Disease, CC BY 4.0 license: https://archive.ics.uci.edu/dataset/45/heart+disease
