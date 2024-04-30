The following are modifications or improvements to original notebooks. Please refer to the authors' models for the published primary work. Built with Meta Llama 3.
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

@inproceedings{fang2023mol,
  author       = {Yin Fang and
                  Xiaozhuan Liang and
                  Ningyu Zhang and
                  Kangwei Liu and
                  Rui Huang and
                  Zhuo Chen and
                  Xiaohui Fan and
                  Huajun Chen},
  title        = {Mol-Instructions: {A} Large-Scale Biomolecular Instruction Dataset
                  for Large Language Models},
  booktitle    = {{ICLR}},
  publisher    = {OpenReview.net},
  year         = {2024},
  url          = {https://openreview.net/pdf?id=Tlsdsb6l9n}
} <br>
[META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/) <br>
