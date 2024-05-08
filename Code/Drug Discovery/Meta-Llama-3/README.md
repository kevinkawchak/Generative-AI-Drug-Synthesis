## May 07, 2024: Additional Fine-tunings, Built with Meta Llama 3 <br>

- **Developed by:** kevinkawchak
- **License:** llama3
- **Finetuned from model :** gradientai/Llama-3-8B-Instruct-Gradient-1048k
- **Finetuned using dataset :** zjunlp/Mol-Instructions, cc-by-4.0
- **Dataset identification:** Molecule-oriented Instructions
- **Dataset function:** Description guided molecule design

1) gradientai/Llama-3-8B-Instruct-Gradient-1048k [Model](https://huggingface.co/gradientai/Llama-3-8B-Instruct-Gradient-1048k) <br>
Llama 3 8B update: 1040K context length from 8K, and highest RAM consumption<br>
"What is the structure for adenine?" Verbose SELFIES structure, but logical<br>
[Fine-tuned](https://huggingface.co/kevinkawchak/gradientai-Llama-3-8B-Instruct-Gradient-1048k-Molecule16) on Mol-Instructions, float16, [GitHub](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Llama-3-8B-Instruct-Gradient-1048k-Molecule.ipynb), 610 seconds, A100 40GB <br>

2) NousResearch/Hermes-2-Pro-Llama-3-8B [Model](https://huggingface.co/NousResearch/Hermes-2-Pro-Llama-3-8B)<br>
Llama 3 8B update: Cleaned OpenHermes 2.5, new Function Calling, JSON Mode dataset<br>
"What is the structure for adenine?" Concise SELFIES structure, but less logical <br>
[Fine-tuned](https://huggingface.co/kevinkawchak/NousResearch-Hermes-2-Pro-Llama-3-8B-Molecule16) on Mol-Instructions, float16, [GitHub](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Hermes-2-Pro-Llama-3-8B-Molecule.ipynb), 599 seconds, A100 40GB <br>

3) nvidia/Llama3-ChatQA-1.5-8B [Model](https://huggingface.co/nvidia/Llama3-ChatQA-1.5-8B)<br>
Llama 3 8B update: ChatQA-1.5 to enhance tabular and arithmetic calculation capability<br>
"What is the structure for adenine?" Verbose SELFIES structure and less logical <br>
[Fine-tuned](https://huggingface.co/kevinkawchak/nvidia-Llama3-ChatQA-1.5-8B-Molecule16) on Mol-Instructions, float16, [GitHub](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Llama3-ChatQA-1.5-8B-Molecule.ipynb), 599 seconds, A100 40GB <br>

Responses were verified against the Wikipedia [Adenine](https://en.wikipedia.org/wiki/Adenine) SMILES format and a SMILES to SELFIES python notebook estimated [generator](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/SMILES%20to%20SELFIES%20estimator.ipynb). <br>
Fine-tunings were performed using the Apache-2.0 unsloth 'Alpaca + Llama-3 8b full example' Colab [notebook](https://colab.research.google.com/drive/135ced7oHytdxu3N2DNe1Z0kqjyYIkDXp?usp=sharing).

## 2nd Study
The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work.
[Cover Image](https://drive.google.com/file/d/1J-spZMzLlPxkqfMrPxvtMZiD2_hfcGyr/view?usp=sharing). [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/). Built with Meta Llama 3.  <br>

A 4-bit quantization of Meta-Llama-3-8B-Instruct was used to reduce training memory requirements when fine-tuning on the zjunlp/Mol-Instructions dataset. (1-2) In addition, the minimum LoRA rank value was utilized to reduce the overall size of created models. In specific, the molecule-oriented instructions description guided molecule design was implemented to answer general questions and general biochemistry questions. General questions were answered with high accuracy, while biochemistry related questions returned 'SELFIES' structures but with limited accuracy. 

The notebook featured Torch and Hugging Face libraries using the Unsloth llama-3-8b-Instruct-bnb-4bit quantization model. Training loss decreased steadily from 1.97 to 0.73 over 60 steps. Additional testing regarding the appropriate level of compression or hyperparameter adjustments for accurate SELFIES chemical structures outputs is relevant, as shown in the GitHub notebook for research purposes (3). A 16-bit and reduced 4-bit size were uploaded to Hugging Face. (4-5)

Update 04/24: The number of training steps were increased to further decrease loss, while maintaining reduced memory requirements through quantization and reduced size through LoRA. This allowed for significantly improved responses to biochemistry related questions, and were saved at the following LLM Model sizes: [8.03B](https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-Molecule16), [4.65B](https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-Molecule04). [github](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Meta-Llama-3-8B-Instruct-Molecule.ipynb).

References:
1) unsloth: https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit
2) zjunlp: https://huggingface.co/datasets/zjunlp/Mol-Instructions
3) github: https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Meta-Llama-3-8B-Instruct-Mol.ipynb
4) hugging face: https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-LoRA-Mol16
5) hugging face: https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-LoRA-Mol04

@inproceedings{fang2023mol, <br>
  author       = {Yin Fang and<br>
                  Xiaozhuan Liang and<br>
                  Ningyu Zhang and<br>
                  Kangwei Liu and<br>
                  Rui Huang and<br>
                  Zhuo Chen and<br>
                  Xiaohui Fan and<br>
                  Huajun Chen},<br>
  title        = {Mol-Instructions: {A} Large-Scale Biomolecular Instruction Dataset<br>
                  for Large Language Models},<br>
  booktitle    = {{ICLR}},<br>
  publisher    = {OpenReview.net},<br>
  year         = {2024},<br>
  url          = {https://openreview.net/pdf?id=Tlsdsb6l9n}}<br>





## Primary Study: The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work. Built with Meta Llama 3.
[Cover Image](https://drive.google.com/file/d/1J-spZMzLlPxkqfMrPxvtMZiD2_hfcGyr/view?usp=sharing) <br>

A 4-bit quantization of Meta-Llama-3-8B-Instruct was used to reduce training memory requirements when fine-tuning on the zjunlp/Mol-Instructions dataset. (1-2) In addition, the minimum LoRA rank value was utilized to reduce the overall size of created models. In specific, the molecule-oriented instructions description guided molecule design was implemented to answer general questions and general biochemistry questions. General questions were answered with high accuracy, while biochemistry related questions returned 'SELFIES' structures but with limited accuracy. 

The notebook featured Torch and Hugging Face libraries using the Unsloth llama-3-8b-Instruct-bnb-4bit quantization model. Training loss decreased steadily from 1.97 to 0.73 over 60 steps. Additional testing regarding the appropriate level of compression or hyperparameter adjustments for accurate SELFIES chemical structures outputs is relevant, as shown in the GitHub notebook for research purposes (3). A 16-bit and reduced 4-bit size were uploaded to Hugging Face. (4-5)

Update 04/24: The number of training steps were increased to further decrease loss, while maintaining reduced memory requirements through quantization and reduced size through LoRA. This allowed for significantly improved responses to biochemistry related questions, and were saved at the following LLM Model sizes: [8.03B](https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-Molecule16), [4.65B](https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-Molecule04). [github](https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Meta-Llama-3-8B-Instruct-Molecule.ipynb) 

References:
1) unsloth, apache-2.0: https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit
2) zjunlp, cc-by-4.0: https://huggingface.co/datasets/zjunlp/Mol-Instructions
3) github: https://github.com/kevinkawchak/Medical-Quantum-Machine-Learning/blob/main/Code/Drug%20Discovery/Meta-Llama-3/Meta-Llama-3-8B-Instruct-Mol.ipynb
4) hugging face: https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-LoRA-Mol16
5) hugging face: https://huggingface.co/kevinkawchak/Meta-Llama-3-8B-Instruct-LoRA-Mol04 <br>

@inproceedings{fang2023mol, <br>
  author       = {Yin Fang and<br>
                  Xiaozhuan Liang and<br>
                  Ningyu Zhang and<br>
                  Kangwei Liu and<br>
                  Rui Huang and<br>
                  Zhuo Chen and<br>
                  Xiaohui Fan and<br>
                  Huajun Chen},<br>
  title        = {Mol-Instructions: {A} Large-Scale Biomolecular Instruction Dataset<br>
                  for Large Language Models},<br>
  booktitle    = {{ICLR}},<br>
  publisher    = {OpenReview.net},<br>
  year         = {2024},<br>
  url          = {https://openreview.net/pdf?id=Tlsdsb6l9n}} <br>
<br>
[META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/) <br>
