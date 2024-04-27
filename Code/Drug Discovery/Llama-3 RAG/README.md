The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work.

## Meta-Llama-3-70B-Instruct RAG
[Cover Image](https://drive.google.com/file/d/1MNSNh9yLPzqHShuTctOUgTf1uj18uDOg/view?usp=sharing)

The results indicate that using Retrieval-Augmented Generation (RAG) is important for answering questions from a specific public dataset, even when Meta AI had knowledge of the dataset. Although modern pre-trained LLMs use RAG techniques, it will likely also be necessary to point to specific local or online datasets to answer questions at high accuracy.

The 70B RAG LLM had the most concise answer to the question 'What happened to the cleveland.data file?', citing relevant 'node ics' and 'node cip2' information found in the original dataset shown below. The 8B RAG LLM was less concise, but had factual information regarding the 'need to obtain a new copy from the donor'. The Meta AI web interface based on 70B Llama 3 needed additional context to provide a lengthy answer that included a doctor's name found in a different file.

In order to load and transfer 70,000,000,000 parameters from the pre-trained 147GB 70B LLM to RAM, a Colab TPU v2 with 225GB Disk space and 335GB RAM was used that was not optimized for speed. The same Sakil786 notebook settings and UCI heart disease dataset were implemented for the 16GB 8B LLM using a Colab A100 GPU, although no training was necessary for either LLM. LLM chatbots use RAG to cite sources, but unless users have the insight to specify where their information is on the web, there are limited accuracy improvements. In summary, using a local LLM with local or online RAG appears to be the safe and effective way to process information related to medical data. 

Original File <br>
"The file cleveland.data has been unfortunately messed up when we lost <br>
node cip2 and loaded the file on node ics. The file processed.cleveland.data <br>
seems to be in good shape and is useable (for the 14 attributes situation). <br>
I'll clean up cleveland.data as soon as possible. <br>

Bad news: my original copy of the database appears to be corrupted. <br>
I'll have to go back to the donor to get a new copy. <br>

David Aha" <br>

Q: What happened to the cleveland.data file? <br>
Meta-Llama-3-70B-Instruct RAG <br>
A: The cleveland.data file was messed up when it was loaded on node ics after node cip2 went down. <br>
Meta-Llama-3-8B-Instruct RAG <br>
A: The cleveland.data file was "messed up" when it was loaded on a different node, and the file processed.cleveland.data is a cleaned up version of the original file. The original file appears to be corrupted and the author will need to obtain a new copy from the donor.

Q: In specific, What happened to the cleveland.data file regarding the UCI heart disease dataset in the “warning” file name? <br>
Meta AI (Llama 3 8B, general use) <br>
A: According to the "warning" file, the Cleveland.data file was replaced by the "processed.cleveland.data" file due to errors and <br> inconsistencies in the original file. Specifically, the warning file states: <br>
"Dr. Detrano (the original collector.. <br>

UCI, CC BY 4.0 license: https://archive.ics.uci.edu/dataset/45/heart+disease <br>
Llama 3 70B, META LLAMA 3 COMMUNITY LICENSE: https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct <br>
Meta AI, META LLAMA 3 COMMUNITY LICENSE: meta.ai <br>
Sakil786, GPL-3.0 license: https://github.com/Sakil786/RAG_using_Llama-3/blob/main/RAG_using_Llama_3.ipynb <br>

## Meta-Llama-3-8B-Instruct RAG
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
2) meta-llama/Meta-Llama-3-8B-Instruct, META LLAMA 3 COMMUNITY LICENSE: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
3) BAAI/bge-small-en-v1.5, MIT license: https://huggingface.co/BAAI/bge-small-en-v1.5
4) Sakil786 RAG_using_Llama_3.ipynb, GPL-3.0 license: https://github.com/Sakil786/RAG_using_Llama-3/blob/main/RAG_using_Llama_3.ipynb
5) UCI/Heart Disease, CC BY 4.0 license: https://archive.ics.uci.edu/dataset/45/heart+disease
